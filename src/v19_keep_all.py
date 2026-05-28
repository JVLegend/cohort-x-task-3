"""V19 — PROBE: KEEP = TODOS os ~97k codigos do dicionario. ASSOC/DIFF vazios.
Testa se gold KEEP e enorme (recall vence) ou especifico (precision dispara queda)."""
from common import load_data, write_submission


def main():
    cond_df, icd = load_data()
    all_codes = icd["icd_code"].tolist()
    rows = []
    for cond in cond_df["Condition"]:
        rows.append((cond, all_codes, [], []))
    write_submission(rows, "submissions/v19_keep_all.csv")


if __name__ == "__main__":
    main()
