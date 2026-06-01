"""V34 — Plano D LOCAL: LLM classifier usando qwen3:14b via Ollama (sem API key/custo).
Para cada condition, pega top-N candidatos BioBERT e pede ao LLM classificar em KEEP/IRRELEVANT.
ASSOC/DIFF deixados vazios (gold quase sempre vazio).
"""
import json
import time
import numpy as np
import requests
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

CACHE = Path("data/icd_embeddings.npy")
MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
TOP_N = 200  # candidatos por condicao
OLLAMA_MODEL = "qwen2.5:7b"
OLLAMA_URL = "http://localhost:11434/api/chat"

PROMPT = """You are a senior clinical coder. Classify each ICD-10-CM code below.

CONDITION: {condition}

For each code, label:
- KEEP: code IS the condition or any specific subtype/variant (including different sites, severities, complications WITH the condition like "diabetes with nephropathy")
- IRRELEVANT: code is a different disease, complication only, comorbidity, or unrelated

Be INCLUSIVE on KEEP (all variants of the disease count). Be CONSERVATIVE on IRRELEVANT.

CODES:
{candidates}

Output ONLY a JSON array, one object per code: [{{"code":"X","label":"KEEP"}},...]. No prose, no markdown."""


def build_candidates(cond_df, icd, icd_emb, model):
    queries = [c + " " + " ".join(SYN_EXP.get(c, [c])) for c in cond_df["Condition"]]
    q_embs = model.encode(queries, normalize_embeddings=True)
    sims_all = q_embs @ icd_emb.T

    cands = {}
    for ci, cond in enumerate(cond_df["Condition"]):
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        kws = SYN_EXP.get(cond, [cond])
        seed = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws))
        order = np.argsort(-sims_all[ci])
        cs = set(seed)
        for i in order:
            cs.add(int(i))
            if len(cs) >= TOP_N:
                break
        cands[cond] = [(icd.iloc[i]["icd_code"], icd.iloc[i]["long_title"])
                       for i in sorted(cs, key=lambda j: -sims_all[ci][j])[:TOP_N]]
    return cands


def call_ollama(prompt: str, retries=2) -> str:
    for attempt in range(retries + 1):
        try:
            r = requests.post(OLLAMA_URL, json={
                "model": OLLAMA_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False,
                "options": {"temperature": 0.0, "num_ctx": 16384},
            }, timeout=600)
            r.raise_for_status()
            return r.json()["message"]["content"]
        except Exception as e:
            if attempt < retries:
                print(f"  retry {attempt+1}: {e}")
                time.sleep(2)
                continue
            raise


def parse_keep(text: str, valid_codes: set) -> list:
    """Robusto: tenta extrair array JSON do texto."""
    text = text.strip()
    # remove <think>...</think>
    if "</think>" in text:
        text = text.split("</think>", 1)[1].strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    # encontra primeiro [
    i = text.find("[")
    j = text.rfind("]")
    if i < 0 or j < 0:
        return []
    try:
        arr = json.loads(text[i:j+1])
    except json.JSONDecodeError:
        return []
    out = []
    for item in arr:
        if not isinstance(item, dict):
            continue
        code = str(item.get("code", "")).strip()
        label = str(item.get("label", "")).strip().upper()
        if code in valid_codes and label == "KEEP":
            out.append(code)
    return out


def chunked(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]


def main():
    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    print("Building candidates...")
    cands = build_candidates(cond_df, icd, icd_emb, model)
    valid_codes_per_cond = {c: set(x[0] for x in v) for c, v in cands.items()}

    print(f"Calling {OLLAMA_MODEL}...")
    rows = []
    for cond in cond_df["Condition"]:
        cs = cands[cond]
        print(f"\n=== {cond} ({len(cs)} cands) ===")
        keep_codes = []
        # 50 codes per chunk to fit context
        for chunk in chunked(cs, 50):
            cand_str = "\n".join(f"- {c}: {t}" for c, t in chunk)
            prompt = PROMPT.format(condition=cond, candidates=cand_str)
            t0 = time.time()
            try:
                resp = call_ollama(prompt)
            except Exception as e:
                print(f"  ERROR: {e} - skipping chunk")
                continue
            keeps = parse_keep(resp, valid_codes_per_cond[cond])
            keep_codes.extend(keeps)
            print(f"  chunk {len(chunk)}: kept {len(keeps)} ({time.time()-t0:.1f}s)")
        keep_codes = list(dict.fromkeys(keep_codes))  # dedup preservando ordem
        print(f"  TOTAL KEEP: {len(keep_codes)}")
        rows.append((cond, keep_codes, [], []))

    write_submission(rows, "submissions/v34_ollama.csv")


if __name__ == "__main__":
    main()
