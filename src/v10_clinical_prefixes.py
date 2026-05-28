"""V10 — Classificacao via prefixos ICD-10 curados clinicamente.

Para cada condicao, prefixos KEEP/ASSOC/DIFF baseados em conhecimento medico.
Inclui TODOS os codigos do dicionario cujo code comeca com algum prefixo.
"""
from common import load_data, write_submission

# (KEEP_prefixes, ASSOC_prefixes, DIFF_prefixes)
# Prefixos ICD-10-CM curados — KEEP = a condicao em si, ASSOC = relacionados, DIFF = diferenciais clinicos.
RULES = {
    "Epistaxis": (
        ["R04"],  # R040=Epistaxis, R041-9=hemorragias respiratorias
        ["J343"],  # hipertrofia conchas — causa frequente; +Z87.2 nao tem
        ["R042", "R049", "K920", "K661"],  # hemoptise, hematemese — confundiveis
    ),
    "Intracranial Pressure": (
        ["G932", "G935", "G936"],  # benign IH, compression, edema
        ["G931", "G938", "G939", "G937", "G910", "G911", "G912", "G913", "G919", "G94"],  # hidrocefalia, encefalopatia
        ["G440", "G441", "G442", "G43", "R51", "H470"],  # cefaleia, enxaqueca, papiledema
    ),
    "Chronic Obstructive Pulmonary Disease": (
        ["J44"],
        ["J41", "J42", "J43", "J47", "J982", "J983", "J984"],  # bronquite cronica, enfisema, bronquiectasia
        ["J45", "J46", "J84"],  # asma, status asthmaticus, ILD
    ),
    "Enlarged Mediastinum": (
        ["J985", "J986", "Q341"],  # mediastinite, doencas mediastino, cisto congenito
        ["C38", "D151", "D152", "D383"],  # neoplasias mediastinais
        ["R911", "R590", "R598", "R599"],  # achados imagem, linfonodos
    ),
    "Gout": (
        ["M10", "M1A"],  # gout idiopatica + cronica
        ["E790", "E791"],  # hiperuricemia, sind. lise
        ["M11", "M12"],  # pseudogota, outras artropatias por cristais
    ),
    "Latent Adrenal Insufficiency": (
        ["E271", "E272", "E274"],  # primary, drug-induced, unspec adrenocortical insuf
        ["E270", "E273", "E275", "E278", "E279", "E255", "E258", "E259"],  # outros disturbios adrenais
        ["E230", "E231", "E232", "E233", "E236", "E237"],  # hipopituitarismo
    ),
    "Dermatomycosis": (
        ["B35", "B36"],  # tinea, outras micoses superficiais
        ["B37"],  # candidiase
        ["L20", "L21", "L23", "L24", "L25", "L26", "L27", "L28", "L29", "L40"],  # eczema, dermatite, psoriase
    ),
    "Pleurisy": (
        ["R091", "J90", "J91"],  # pleurisy, pleural effusion
        ["J86", "J94"],  # empiema, outras cond pleurais
        ["J93", "J81", "I26"],  # pneumotorax, edema pulmonar, embolia
    ),
    "Bronchitis": (
        ["J20", "J21", "J40", "J41", "J42"],  # aguda, bronquiolite, cronica
        ["J22"],  # infeccao trato resp inferior nao especificada
        ["J45", "J18", "J44"],  # asma, pneumonia, COPD
    ),
    "Thyroiditis": (
        ["E06"],  # thyroiditis (todas)
        ["E031", "E032"],  # mixedema, hipotireoidismo por outros medicamentos
        ["E05", "E04", "E03"],  # hipertireoidismo, bocio, hipotireoidismo
    ),
    "Nasopharyngeal Carcinoma": (
        ["C11"],  # malig nasofaringe (todas)
        ["D000", "D101", "C10", "C09", "C12", "C13", "C14"],  # in situ, benignas, outras malig faringe
        ["C30", "C31", "C32"],  # malig nasal, sinusal, laringe
    ),
    "CKD": (
        ["N18", "N19"],  # CKD + insuficiencia renal nao especificada
        ["N083", "I12", "I13", "Z992", "Z9115"],  # CKD em outras doencas, neph HTN, dialise
        ["N17", "N00", "N01", "N03", "N05"],  # AKI, nefritis aguda/cronica
    ),
    "Hypothyroidism": (
        ["E03", "E890"],  # hipotireoidismo + pos-cirurgico
        ["E02", "E000", "E001", "E002", "E009"],  # bocio com hipo, sind iodo defic
        ["E05", "E06", "E07", "E04"],  # hiper, tireoidite, outros disturbios
    ),
    "Hematemesis": (
        ["K920"],  # hematemese
        ["K921", "K922", "K661"],  # melena, GI bleed, hemoperitonio
        ["R042", "K226", "K2211"],  # hemoptise, sind mallory-weiss, esofagite ulcerativa
    ),
    "Heart Failure": (
        ["I50", "I110", "I130", "I132"],  # HF + HTN with HF + HTN-CKD with HF
        ["I420", "I421", "I422", "I425", "I428", "I429", "I43", "I255"],  # cardiomiopatias
        ["I21", "I22", "I252", "I48", "I49"],  # IAM, fibrilacao, arritmias
    ),
    "Hypergonadism": (
        ["E270", "E281", "E282"],  # outros hipergonadismo
        ["E283", "E288", "E289", "E290", "E291", "E298", "E299"],  # disturbios ovariano/testicular
        ["E230", "E232", "E893", "E894"],  # hipopituitarismo, hipogonadismo
    ),
    "UTI": (
        ["N390", "N300", "N308", "N309", "N341", "N342", "N390"],  # UTI, cistite aguda, uretrite
        ["N10", "N11", "N12", "N136"],  # pielonefritis
        ["N343", "N76", "N41", "N493"],  # uretrite, vaginite, prostatite
    ),
    "Diabetes": (
        ["E10", "E11", "E13"],  # DM tipo 1, 2, outros especificados
        ["E08", "E09", "Z794", "R73"],  # DM por doenca, induzido, dependencia insulina, hiperglicemia
        ["E16", "E230", "E231", "E232"],  # hipoglicemia, diabetes insipidus
    ),
    "Interstitial Lung Disease": (
        ["J84"],  # ILD (todas)
        ["J60", "J61", "J62", "J63", "J64", "J65", "J66", "J67", "J68", "J70"],  # pneumoconiose, hipersens
        ["J18", "J81", "J44", "J47"],  # pneumonia, edema, COPD, bronquiectasia
    ),
    "Hypoparathyroidism": (
        ["E200", "E201", "E208", "E209", "E893"],  # hipopara + pos-cirurgico
        ["E834", "E835"],  # hipocalcemia/magnesemia
        ["E21"],  # hiperparatireoidismo (oposto)
    ),
    "Hyperparathyroidism": (
        ["E210", "E211", "E212", "E213"],  # hiperpara primario, secundario, terciario, NOS
        ["E215", "E835"],  # outros disturbios paratireoide, hipercalcemia
        ["E20", "E893"],  # hipopara (oposto)
    ),
    "Hyperthyroidism": (
        ["E05"],  # tireotoxicose / hipertireoidismo (todas)
        ["E041", "E042", "E040"],  # bocio nodular toxico, multinodular toxico, simples
        ["E03", "E06", "E89"],  # hipo, tireoidite, pos-cirurgico
    ),
    "Pneumonia": (
        ["J12", "J13", "J14", "J15", "J16", "J17", "J18", "J851", "J690"],  # pneumonias bacterianas/virais/aspirativa
        ["J20", "J21", "J22", "J86", "J85", "B012"],  # bronquite, bronquiolite, abscesso, varicela pneum
        ["J45", "J44", "J90", "A15", "J47", "J84"],  # asma, COPD, derrame, TB, bronquiectasia, ILD
    ),
}


def codes_matching(icd, prefixes):
    if not prefixes:
        return []
    out = []
    for p in prefixes:
        mask = icd["icd_code"].astype(str).str.startswith(p)
        out.extend(icd[mask].index.tolist())
    # dedup mantendo ordem
    seen = set()
    res = []
    for i in out:
        if i not in seen:
            seen.add(i)
            res.append(i)
    return res


def main():
    cond_df, icd = load_data()
    rows = []
    for cond in cond_df["Condition"]:
        keep_p, assoc_p, diff_p = RULES.get(cond, ([cond.lower()], [], []))
        keep_idx = codes_matching(icd, keep_p)
        keep_set = set(keep_idx)
        assoc_idx = [i for i in codes_matching(icd, assoc_p) if i not in keep_set]
        assoc_set = set(assoc_idx)
        diff_idx = [i for i in codes_matching(icd, diff_p)
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

    write_submission(rows, "submissions/v10_clinical.csv")


if __name__ == "__main__":
    main()
