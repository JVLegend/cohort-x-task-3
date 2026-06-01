"""V38 — INTERSECT v33 (retrieval) ∩ v34 (LLM): so codigos que ambos selecionaram."""
import pandas as pd


def parse(s):
    if pd.isna(s) or s == "Not Applicable":
        return []
    return [c.strip() for c in str(s).split(";") if c.strip()]


def main():
    a = pd.read_csv("submissions/v33_obscure.csv")
    b = pd.read_csv("submissions/v34_ollama.csv")
    out = []
    for _, ra in a.iterrows():
        cond = ra["Condition"]
        rb = b[b["Condition"] == cond].iloc[0]
        keep = sorted(set(parse(ra["KEEP"])) & set(parse(rb["KEEP"])))
        if not keep:
            # fallback: pega top do retrieval
            keep = parse(ra["KEEP"])[:5]
        out.append({
            "Condition": cond,
            "KEEP": "; ".join(keep) if keep else "Not Applicable",
            "ASSOCIATION": "Not Applicable",
            "DIFF": "Not Applicable",
        })
        print(f"{cond:42s} K={len(keep):3d}")
    pd.DataFrame(out).to_csv("submissions/v38_intersect.csv", index=False)


if __name__ == "__main__":
    main()
