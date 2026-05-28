"""V15 — PROBE TOTAL EMPTY: TUDO 'Not Applicable'. Baseline de zero predicao."""
from common import load_data
import pandas as pd


def main():
    cond_df, _ = load_data()
    out = pd.DataFrame({
        "Condition": cond_df["Condition"],
        "KEEP": ["Not Applicable"] * len(cond_df),
        "ASSOCIATION": ["Not Applicable"] * len(cond_df),
        "DIFF": ["Not Applicable"] * len(cond_df),
    })
    out.to_csv("submissions/v15_empty.csv", index=False)
    print("Wrote submissions/v15_empty.csv")


if __name__ == "__main__":
    main()
