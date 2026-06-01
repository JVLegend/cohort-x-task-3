"""V36 — Usa LLM para LISTAR prefixos ICD-10 canonicos por condition.
Pega prefixos -> expande para todos terminais 5+ char do dicionario.
Combina com v33 (retrieval best) por uniao.
"""
import json
import time
import requests
import pandas as pd
from common import load_data, write_submission
from v33_obscure import KEEP_EXTRA  # ja tem extras


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:7b"

PROMPT = """List the canonical ICD-10-CM root codes (3-character categories like "J44", "E11") that represent the medical condition below. Include ALL root codes that ARE this condition or its specific subtypes (not just related conditions).

CONDITION: {condition}

Examples of correct answers:
- For "Pneumonia": ["J12","J13","J14","J15","J16","J17","J18"]
- For "Heart Failure": ["I50","I110","I130","I132"]
- For "Diabetes": ["E08","E09","E10","E11","E13","O24"]

Output ONLY a JSON array of code strings. No prose."""


def call(prompt):
    r = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.0, "num_ctx": 4096},
    }, timeout=120)
    return r.json()["message"]["content"]


def parse(txt):
    txt = txt.strip()
    if "</think>" in txt:
        txt = txt.split("</think>", 1)[1].strip()
    if txt.startswith("```"):
        txt = txt.split("```")[1]
        if txt.startswith("json"):
            txt = txt[4:]
        txt = txt.strip()
    i = txt.find("[")
    j = txt.rfind("]")
    if i < 0:
        return []
    try:
        arr = json.loads(txt[i:j+1])
    except Exception:
        return []
    return [str(x).strip() for x in arr if isinstance(x, str) and len(str(x).strip()) >= 3]


def main():
    cond_df, icd = load_data()
    prefixes_per_cond = {}
    for cond in cond_df["Condition"]:
        t0 = time.time()
        try:
            txt = call(PROMPT.format(condition=cond))
            prefixes = parse(txt)
        except Exception as e:
            print(f"  ERROR {cond}: {e}")
            prefixes = []
        # adiciona extras manuais
        prefixes = list(dict.fromkeys(prefixes + KEEP_EXTRA.get(cond, [])))
        prefixes_per_cond[cond] = prefixes
        print(f"{cond:42s} prefixes={prefixes} ({time.time()-t0:.1f}s)")

    # Expande cada prefixo para todos os codigos do dict
    rows = []
    v33 = pd.read_csv("submissions/v33_obscure.csv")
    for cond in cond_df["Condition"]:
        keep_idx = []
        for p in prefixes_per_cond[cond]:
            mask = icd["icd_code"].astype(str).str.startswith(p)
            keep_idx.extend(icd[mask].index.tolist())
        # uniao com v33 KEEP
        v33_keep = v33[v33["Condition"] == cond]["KEEP"].iloc[0]
        v33_codes = set() if v33_keep == "Not Applicable" else set(
            c.strip() for c in str(v33_keep).split(";") if c.strip())
        llm_codes = set(icd.iloc[keep_idx]["icd_code"])
        final_codes = sorted(v33_codes | llm_codes)
        rows.append((cond, final_codes, [], []))
        print(f"{cond:42s} v33={len(v33_codes)} +llm={len(llm_codes)} union={len(final_codes)}")

    write_submission(rows, "submissions/v36_llm_prefixes.csv")


if __name__ == "__main__":
    main()
