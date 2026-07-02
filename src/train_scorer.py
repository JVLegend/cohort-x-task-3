#!/usr/bin/env python3
"""Scorer local offline contra o gold da aba Train (5 condicoes).

Objetivo: parar de gastar balas do Kaggle para descobrir se um recipe funciona.
A aba Train de data/Task_3.xlsx tem gold completo para KEEP/ASSOCIATION/DIFF em
5 condicoes. A metrica da competicao e macro-F1 set-overlap por celula. Este
script reproduz essa metrica localmente, entao qualquer selecao de nos ICD pode
ser calibrada de graca antes de virar submissao.

Uso 1 - checar o "teto" do recipe de expansao (nos do proprio gold -> F1=1.0):
    .venv/bin/python src/train_scorer.py --self-check

Uso 2 - pontuar um spec de nos (JSON) contra o gold do Train:
    .venv/bin/python src/train_scorer.py --spec meu_spec.json

Formato do spec JSON:
    {"URTI": {"KEEP": ["J00","J01"], "ASSOCIATION": ["H65","H66"], "DIFF": ["J12"]}}
Cada no e expandido para TODOS os descendentes em data/icd_dict.csv (prefix match),
espelhando como o gold e construido. Celula vazia (sem nos) = "Not Applicable".

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia
"""
import argparse
import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DICT_CSV = ROOT / "data" / "icd_dict.csv"
TASK_XLSX = ROOT / "data" / "Task_3.xlsx"
BUCKETS = ["KEEP", "ASSOCIATION", "DIFF"]


def load_codes():
    d = pd.read_csv(DICT_CSV)
    return set(d["icd_code"].astype(str).str.strip())


def parse_cell(x):
    if pd.isna(x):
        return set()
    return set(t.strip() for t in str(x).split(";") if t.strip() and t.strip().lower() != "nan")


def load_train_gold():
    tr = pd.read_excel(TASK_XLSX, sheet_name="Train")
    gold = {}
    for _, row in tr.iterrows():
        gold[str(row["Condition"])] = {b: parse_cell(row[b]) for b in BUCKETS}
    return gold


def expand_nodes(nodes, codes):
    """Expande uma lista de nos ICD para todos os descendentes no dicionario."""
    out = set()
    for n in nodes:
        n = str(n).strip()
        if not n:
            continue
        out |= set(c for c in codes if c.startswith(n))
    return out


def f1(pred, gold):
    """Set-overlap F1. Convencao: ambos vazios -> 1.0 (celula 'Not Applicable' certa)."""
    if not pred and not gold:
        return 1.0
    if not pred or not gold:
        return 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0
    prec = tp / len(pred)
    rec = tp / len(gold)
    return 2 * prec * rec / (prec + rec)


def score_spec(spec, gold, codes, verbose=True):
    """spec: {cond: {bucket: [nodes]}}. Pontua so as condicoes presentes no gold."""
    cells = []
    for cond, g in gold.items():
        cspec = spec.get(cond, {})
        for b in BUCKETS:
            pred = expand_nodes(cspec.get(b, []), codes)
            val = f1(pred, g[b])
            cells.append(val)
            if verbose:
                tag = "empty" if not g[b] else f"gold={len(g[b])}"
                print(f"  {cond:22s} {b:12s} F1={val:.3f}  pred={len(pred):4d}  {tag}")
    macro = sum(cells) / len(cells) if cells else 0.0
    return macro


def self_check(gold, codes):
    """Sanidade: usar os nos do proprio gold como spec deve dar F1=1.0 em toda celula.

    Isso confirma que a regra 'expandir descendentes' reproduz o gold exatamente
    quando os nos certos, na granularidade certa, sao escolhidos.
    """
    spec = {}
    for cond, g in gold.items():
        spec[cond] = {}
        for b in BUCKETS:
            # deriva os nos minimos: raizes cujo descendente-set == gold-subset.
            # aqui usamos os proprios codigos do gold como "nos" (cada um e seu proprio prefixo).
            spec[cond][b] = sorted(g[b])
    print("== SELF-CHECK (nos = codigos do gold; espera F1=1.000 em tudo) ==")
    macro = score_spec(spec, gold, codes)
    print(f"\nMACRO-F1 self-check = {macro:.4f}  (esperado 1.0000)")
    return macro


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--spec", type=str, help="caminho para spec JSON")
    ap.add_argument("--self-check", action="store_true")
    args = ap.parse_args()

    codes = load_codes()
    gold = load_train_gold()
    print(f"Dicionario: {len(codes)} codigos | Train gold: {len(gold)} condicoes\n")

    if args.self_check or not args.spec:
        self_check(gold, codes)
        if not args.spec:
            return

    if args.spec:
        spec = json.loads(Path(args.spec).read_text())
        print(f"\n== SPEC: {args.spec} ==")
        macro = score_spec(spec, gold, codes)
        print(f"\nMACRO-F1 (Train, {len(gold)} conds x 3 buckets) = {macro:.4f}")


if __name__ == "__main__":
    main()
