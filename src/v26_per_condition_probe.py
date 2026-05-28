"""V26 — Isolated probe: para cada condition, KEEP=todos os codigos do dict, others=[].
Isso da F1 perfeito naquela condition (recall=1, mas precision=0). Score nao serve
direto, mas COMPARAR com baseline empty (0.222) diz se essa condition tem gold KEEP grande.

Submeter 1-2 por dia: para cada condition que estamos errando, podemos isolar.

Alternativa: 1 SUBMISSION com KEEP cheio em UMA condition, vazio nas outras.
"""
import sys
from common import load_data, write_submission


def main(target_cond_idx: int):
    cond_df, icd = load_data()
    all_codes = icd["icd_code"].tolist()
    rows = []
    for ci, cond in enumerate(cond_df["Condition"]):
        if ci == target_cond_idx:
            rows.append((cond, all_codes, [], []))
        else:
            rows.append((cond, [], [], []))
    write_submission(rows, f"submissions/v26_probe_cond{target_cond_idx:02d}.csv")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
