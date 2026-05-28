"""V28 — Plano D: LLM-as-classifier. Para cada condition, manda top-N candidatos
BioBERT para Claude/GPT e pede para classificar em KEEP/IRRELEVANT.
ASSOC/DIFF deixados vazios (baseline empty alto).

Uso:
  export ANTHROPIC_API_KEY=...
  python src/v28_llm_classifier.py

Custo estimado: 23 conds x ~200 codes x ~80 tokens = ~370k tokens input + ~50k output
  ~$1.20 com Claude Sonnet 4.5, ou ~$0.20 com Haiku.
"""
import os
import json
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer
from common import load_data, write_submission
from v10_clinical_prefixes import RULES, codes_matching
from v4_quickwin import find_by_keywords
from v21_keep_expanded import SYN_EXP

MODEL_NAME = "pritamdeka/S-PubMedBert-MS-MARCO"
CACHE = Path("data/icd_embeddings.npy")
TOP_N = 200  # candidatos por condicao para LLM avaliar

PROMPT_TEMPLATE = """You are a senior clinical coder reviewing ICD-10-CM codes for a medical condition.

CONDITION: {condition}

For each ICD-10-CM code below, classify it as either:
- KEEP: the code IS the condition or a direct subtype/specific variant of it
- IRRELEVANT: the code is related/different/complication/comorbid but NOT the condition itself

Be inclusive on KEEP: include all variants (anatomic site, severity, complications WITH the condition like "diabetes with nephropathy").
Be strict on IRRELEVANT: only if the code is clearly a different disease.

CANDIDATES:
{candidates}

Reply with a JSON array of objects: [{{"code": "X", "label": "KEEP"}}, ...]
Output ONLY the JSON, no other text."""


def build_candidates(cond_df, icd, icd_emb, model):
    candidates_by_cond = {}
    queries = [c + " " + " ".join(SYN_EXP.get(c, [c])) for c in cond_df["Condition"]]
    q_embs = model.encode(queries, normalize_embeddings=True)
    sims_all = q_embs @ icd_emb.T

    for ci, cond in enumerate(cond_df["Condition"]):
        keep_p, _, _ = RULES.get(cond, ([cond.lower()], [], []))
        kws = SYN_EXP.get(cond, [cond])
        # Uniao prefix + keyword + top BioBERT
        seed = set(codes_matching(icd, keep_p)) | set(find_by_keywords(icd, kws))
        # Top N por similaridade (incluindo seed)
        order = np.argsort(-sims_all[ci])
        cand_set = set(seed)
        for i in order:
            cand_set.add(int(i))
            if len(cand_set) >= TOP_N:
                break
        candidates_by_cond[cond] = [
            (icd.iloc[i]["icd_code"], icd.iloc[i]["long_title"]) for i in sorted(cand_set)
        ]
    return candidates_by_cond


def classify_with_claude(condition: str, candidates: list) -> list:
    from anthropic import Anthropic
    client = Anthropic()
    cand_str = "\n".join(f"- {c}: {t}" for c, t in candidates)
    msg = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": PROMPT_TEMPLATE.format(
            condition=condition, candidates=cand_str)}],
    )
    txt = msg.content[0].text.strip()
    if txt.startswith("```"):
        txt = txt.split("```")[1].lstrip("json").strip()
    parsed = json.loads(txt)
    return [item["code"] for item in parsed if item.get("label") == "KEEP"]


def classify_with_openai(condition: str, candidates: list) -> list:
    from openai import OpenAI
    client = OpenAI()
    cand_str = "\n".join(f"- {c}: {t}" for c, t in candidates)
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": PROMPT_TEMPLATE.format(
            condition=condition, candidates=cand_str)}],
        response_format={"type": "json_object"},
    )
    txt = resp.choices[0].message.content
    parsed = json.loads(txt)
    arr = parsed if isinstance(parsed, list) else parsed.get("classifications", [])
    return [item["code"] for item in arr if item.get("label") == "KEEP"]


def main():
    if not os.getenv("ANTHROPIC_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        print("ERROR: set ANTHROPIC_API_KEY or OPENAI_API_KEY")
        return
    use_claude = bool(os.getenv("ANTHROPIC_API_KEY"))

    cond_df, icd = load_data()
    icd_emb = np.load(CACHE)
    model = SentenceTransformer(MODEL_NAME)

    print("Building candidates...")
    cands = build_candidates(cond_df, icd, icd_emb, model)

    rows = []
    for cond in cond_df["Condition"]:
        print(f"Classifying {cond} ({len(cands[cond])} cands)...")
        try:
            if use_claude:
                keep_codes = classify_with_claude(cond, cands[cond])
            else:
                keep_codes = classify_with_openai(cond, cands[cond])
        except Exception as e:
            print(f"  ERROR: {e} - falling back to all candidates")
            keep_codes = [c for c, _ in cands[cond]]
        rows.append((cond, keep_codes, [], []))
        print(f"  -> {len(keep_codes)} KEEP")

    write_submission(rows, "submissions/v28_llm.csv")


if __name__ == "__main__":
    main()
