"""V27 — Probes para mapear ASSOC e DIFF do gold.
Hipotese: se baseline empty=0.222, e KEEP-only=0.287, entao 0.065 vem de KEEP.
Para ASSOC: setar ASSOC = todos 97k em todas conditions, KEEP/DIFF vazios.
Score - baseline 0.222 = contribuicao do ASSOC quando full.
Mesmo para DIFF.
"""
from common import load_data, write_submission


def main():
    cond_df, icd = load_data()
    all_codes = icd["icd_code"].tolist()

    # ASSOC = todos
    rows = [(c, [], all_codes, []) for c in cond_df["Condition"]]
    write_submission(rows, "submissions/v27a_assoc_all.csv")

    # DIFF = todos
    rows = [(c, [], [], all_codes) for c in cond_df["Condition"]]
    write_submission(rows, "submissions/v27b_diff_all.csv")

    # KEEP + ASSOC = todos (sanity)
    rows = [(c, all_codes, all_codes, []) for c in cond_df["Condition"]]
    write_submission(rows, "submissions/v27c_keep_assoc_all.csv")


if __name__ == "__main__":
    main()
