"""V42 — Gemini 3 Pro Preview classifier. TOP_N=500 candidates, chunks=50.
Mais inteligente + mais candidatos + rate limit safer.
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
TOP_N = 400
CHUNK = 50
SLEEP_BETWEEN = 1  # seconds between API calls

PROMPT = """You are a senior clinical ICD-10-CM coder doing inclusion classification.

CONDITION: {condition}

For each ICD-10-CM code below, classify:
- KEEP: code IS the condition OR any subtype/variant (anatomic sites, severities, complications WITH the condition like "diabetes WITH nephropathy", congenital/neonatal/iatrogenic/obstetric forms of the SAME disease, all the specific subcodes of the condition's category).
- IRRELEVANT: ONLY if the code is a clearly DIFFERENT disease entity.

Default to KEEP when in doubt. Be EXTREMELY INCLUSIVE: include all variants, all complications, all anatomic specifications, all severities.

CODES:
{candidates}

Output a JSON array, one object per code: [{{"code":"X","label":"KEEP"}},{{"code":"Y","label":"IRRELEVANT"}}]. ONLY JSON, no prose."""


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


def call_gemini(prompt, retries=5):
    for attempt in range(retries):
        try:
            r = requests.post(URL, headers={
                "Content-Type": "application/json",
                "X-goog-api-key": API_KEY,
            }, json={
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.0, "maxOutputTokens": 16384},
            }, timeout=180)
            r.raise_for_status()
            d = r.json()
            return d["candidates"][0]["content"]["parts"][0]["text"]
        except requests.exceptions.HTTPError as e:
            if r.status_code == 429:
                wait = 5 + attempt * 5
                print(f"  rate limit, wait {wait}s")
                time.sleep(wait)
            elif attempt < retries - 1:
                time.sleep(2)
            else:
                raise
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
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
            if isinstance(it, dict) and str(it.get("code","")).strip() in valid
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
        for start in range(0, len(cs), CHUNK):
            chunk = cs[start:start+CHUNK]
            cand_str = "\n".join(f"- {c}: {t}" for c, t in chunk)
            prompt = PROMPT.format(condition=cond, candidates=cand_str)
            t0 = time.time()
            try:
                resp = call_gemini(prompt)
                ks = parse_keep(resp, valid)
                keep_codes.extend(ks)
                print(f"  {cond[:30]:30s} chunk {len(chunk):3d} -> {len(ks):3d} ({time.time()-t0:.1f}s)")
            except Exception as e:
                print(f"  ERROR {cond}: {e}")
            time.sleep(SLEEP_BETWEEN)
        keep_codes = list(dict.fromkeys(keep_codes))
        rows.append((cond, keep_codes, [], []))
        print(f"  TOTAL {cond}: {len(keep_codes)}\n")

    write_submission(rows, "submissions/v44_flash_deep.csv")


if __name__ == "__main__":
    main()
