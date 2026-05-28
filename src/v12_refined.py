"""V12 — Refinamento cirurgico em cima de v11 (best 0.245).
Foco: estreitar DIFFs inflados, expandir ASSOCs rasos. Restante = v11 (RULES).
"""
from common import load_data, write_submission
from v10_clinical_prefixes import RULES as RULES_V11, codes_matching

# Override sobre RULES_V11
OVERRIDES = {
    # DIFF inflado: M11 (pseudogota) + M12 — restringir aos terminais nao gota
    "Gout": (
        ["M10", "M1A"],
        ["E790", "E791"],
        ["M11"],  # so pseudogota, sem M12 (outras artropatias por cristais difusas)
    ),
    # DIFF G44 explode em variantes de cefaleia — restringir
    "Intracranial Pressure": (
        ["G932", "G935", "G936"],
        ["G931", "G938", "G939", "G937", "G910", "G911", "G912", "G913", "G919", "G94"],
        ["G43", "R51", "H470"],  # tirar G440/G441/G442 (cefaleia inflada)
    ),
    # ASSOC raso — expandir com I40, I47, I49 (outras cardiopatias relacionadas)
    "Heart Failure": (
        ["I50", "I110", "I130", "I132"],
        ["I40", "I41", "I420", "I421", "I422", "I425", "I428", "I429", "I43",
         "I255", "I250", "I252", "I472", "I490"],
        ["I21", "I22"],  # so IAM como diff (tirar arritmias gerais)
    ),
    # ASSOC raso
    "Hyperparathyroidism": (
        ["E210", "E211", "E212", "E213"],
        ["E215", "E834", "E835", "E218"],  # +hipo/hipercalcemia/magnesemia
        ["E20", "E893"],
    ),
    "Hypoparathyroidism": (
        ["E200", "E201", "E208", "E209", "E893"],
        ["E834", "E835", "E58", "E83518"],  # hipocalcemia, hipomagn, def Ca
        ["E21"],
    ),
    # DIFF inflado por J84/J47
    "Bronchitis": (
        ["J20", "J21", "J40", "J41", "J42"],
        ["J22"],
        ["J18", "J44"],  # so pneumonia e COPD (asma fica fora pois pode ser KEEP em outras)
    ),
    # DIFF inflado por L20-L40 (todos eczemas) — restringir
    "Dermatomycosis": (
        ["B35", "B36"],
        ["B37"],
        ["L20", "L40"],  # so dermatite atopica + psoriase
    ),
    # Hypothyroidism DIFF E04 + E07 muito amplo — restringir
    "Hypothyroidism": (
        ["E03", "E890"],
        ["E02", "E000", "E001", "E002", "E009"],
        ["E05", "E06"],
    ),
    # Pneumonia DIFF amplo — restringir
    "Pneumonia": (
        ["J12", "J13", "J14", "J15", "J16", "J17", "J18", "J851", "J690"],
        ["J20", "J21", "J22", "J86", "J85", "B012"],
        ["J45", "J44", "J90", "A15"],
    ),
    # CKD DIFF inflado (N00-N05 muitos)
    "CKD": (
        ["N18", "N19"],
        ["N083", "I12", "I13", "Z992", "Z9115"],
        ["N17"],  # so AKI (real differential clinico)
    ),
}

RULES = {**RULES_V11, **OVERRIDES}


def term_filter(icd, idxs):
    return [i for i in idxs if len(str(icd.iloc[i]["icd_code"])) >= 5]


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, assoc_p, diff_p = RULES.get(cond, ([cond.lower()], [], []))
        keep_idx = term_filter(icd, codes_matching(icd, keep_p))
        if not keep_idx:
            keep_idx = codes_matching(icd, keep_p)[:3]
        keep_set = set(keep_idx)
        assoc_idx = [i for i in term_filter(icd, codes_matching(icd, assoc_p)) if i not in keep_set]
        assoc_set = set(assoc_idx)
        diff_idx = [i for i in term_filter(icd, codes_matching(icd, diff_p))
                    if i not in keep_set and i not in assoc_set]
        if not keep_idx:
            keep_idx = [0]
        rows.append((
            cond,
            icd.iloc[keep_idx]["icd_code"].tolist(),
            icd.iloc[assoc_idx]["icd_code"].tolist(),
            icd.iloc[diff_idx]["icd_code"].tolist(),
        ))
        print(f"{cond:42s} K={len(keep_idx):3d} A={len(assoc_idx):4d} D={len(diff_idx):3d}")

    write_submission(rows, "submissions/v12_refined.csv")


if __name__ == "__main__":
    main()
