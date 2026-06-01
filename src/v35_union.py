"""V35 — UNION v33 (retrieval best 0.366) + v34 (LLM qwen 0.286).
Hipotese: LLM acerta alguns codigos que retrieval perdeu (e vice-versa).
"""
import pandas as pd


def parse_cell(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def main():
    a = pd.read_csv("submissions/v33_obscure.csv")
    b = pd.read_csv("submissions/v34_ollama.csv")
    assert list(a["Condition"]) == list(b["Condition"])

    out = []
    for _, ra in a.iterrows():
        cond = ra["Condition"]
        rb = b[b["Condition"] == cond].iloc[0]
        keep = sorted(set(parse_cell(ra["KEEP"])) | set(parse_cell(rb["KEEP"])))
        out.append({
            "Condition": cond,
            "KEEP": "; ".join(keep) if keep else "Not Applicable",
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
        print(f"{cond:42s} K={len(keep):3d}")
    pd.DataFrame(out).to_csv("submissions/v35_union.csv", index=False)


if __name__ == "__main__":
    main()
