"""V41 — Gemini Flash classifier. Top-200 BioBERT candidates per condition.
ASSOC/DIFF vazios (gold quase sempre vazio nessas categorias).
"""
import os
import json
import time
import requests
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

# Load .env
env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

API_KEY = os.environ["GEMINI_API_KEY"]
MODEL = "gemini-flash-latest"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

CACHE = Path("data/icd_embeddings.npy")
BIO = "pritamdeka/S-PubMedBert-MS-MARCO"
TOP_N = 250

PROMPT = """You are a senior clinical ICD-10-CM coder.

CONDITION: {condition}

Classify each ICD-10-CM code below:
- KEEP: the code IS the condition OR any specific variant (different anatomic sites, severity, complications WITH the condition like "diabetes with nephropathy", congenital/neonatal/obstetric/iatrogenic forms of the SAME disease).
- IRRELEVANT: only if the code represents a clearly different disease entity.

Be INCLUSIVE: when in doubt, KEEP. Include all subtypes, all anatomic variations, all severities.

CODES:
{candidates}

Output a JSON array, one object per code: [{{"code":"X","label":"KEEP"}},...]. ONLY JSON, no prose."""


def build_cands(cond_df, icd, icd_emb, model):
    qs = [c + " " + " ".join(SYN_EXP.get(c, [c])) for c in cond_df["Condition"]]
    q_embs = model.encode(qs, normalize_embeddings=True)
    sims = q_embs @ icd_emb.T

    cands = {}
    for ci, cond in enumerate(cond_df["Condition"]):
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        kws = SYN_EXP.get(cond, [cond])
        seed = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws))
        cs = set(seed)
        for i in np.argsort(-sims[ci]):
            cs.add(int(i))
            if len(cs) >= TOP_N:
                break
        cs_sorted = sorted(cs, key=lambda j: -sims[ci][j])[:TOP_N]
        cands[cond] = [(icd.iloc[i]["icd_code"], icd.iloc[i]["long_title"]) for i in cs_sorted]
    return cands


def call_gemini(prompt, retries=3):
    for attempt in range(retries):
        try:
            r = requests.post(URL, headers={
                "Content-Type": "application/json",
                "X-goog-api-key": API_KEY,
            }, json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.0, "maxOutputTokens": 8192},
            }, timeout=120)
            r.raise_for_status()
            d = r.json()
            return d["candidates"][0]["content"]["parts"][0]["text"]
        except Exception as e:
            if attempt < retries - 1:
                print(f"  retry {attempt+1}: {e}")
                time.sleep(2 * (attempt + 1))
            else:
                raise


def parse_keep(text, valid):
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    i = text.find("[")
    j = text.rfind("]")
    if i < 0:
        return []
    try:
        arr = json.loads(text[i:j+1])
    except Exception:
        return []
    return [str(it["code"]).strip() for it in arr
            if isinstance(it, dict) and str(it["code"]).strip() in valid
            and str(it.get("label", "")).strip().upper() == "KEEP"]


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(BIO)
    print("Building candidates...")
    cands = build_cands(cond_df, icd, icd_emb, model)

    rows = []
    for cond in cond_df["Condition"]:
        cs = cands[cond]
        valid = set(c for c, _ in cs)
        keep_codes = []
        # 100 codes per chunk (Gemini Flash handles big context)
        for start in range(0, len(cs), 100):
            chunk = cs[start:start+100]
            cand_str = "\n".join(f"- {c}: {t}" for c, t in chunk)
            prompt = PROMPT.format(condition=cond, candidates=cand_str)
            t0 = time.time()
            try:
                resp = call_gemini(prompt)
            except Exception as e:
                print(f"  ERROR {cond} chunk: {e}")
                continue
            ks = parse_keep(resp, valid)
            keep_codes.extend(ks)
            print(f"  {cond[:30]:30s} chunk {len(chunk)} -> {len(ks)} KEEP ({time.time()-t0:.1f}s)")
        keep_codes = list(dict.fromkeys(keep_codes))
        rows.append((cond, keep_codes, [], []))
        print(f"  TOTAL {cond}: {len(keep_codes)}")

    write_submission(rows, "submissions/v41_gemini.csv")


if __name__ == "__main__":
    main()
