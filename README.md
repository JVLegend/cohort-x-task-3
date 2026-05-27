# CohortX Task 3 — ICD-10-CM Code Resolution

Mapeia 23 condições médicas para códigos ICD-10-CM (dicionário MIMIC-IV ~97k códigos), classificando em três buckets: **KEEP** (diagnóstico correto), **ASSOCIATION** (relacionados), **DIFF** (diferenciais).

Métrica: **macro F1** entre as três categorias. Restrição: CPU-only, offline.

## Estrutura
```
data/                 Task_3.xlsx + dicionário ICD-10
src/
  common.py           helpers (normalização, abreviações, escrita do CSV)
  v1_tfidf.py         TF-IDF puro
  v2_chapter.py       TF-IDF word+char + corte por capítulo ICD
  v3_hybrid.py        regras por condição + hierarquia ICD
submissions/          CSVs submetidos
```

## 3 propostas
| Versão | Estratégia |
|--------|-----------|
| v1 | TF-IDF word n-gramas → KEEP = top com keyword no título; DIFF = mesma família ICD |
| v2 | TF-IDF word+char concat → vota capítulos top; KEEP/ASSOC dentro do capítulo, DIFF fora |
| v3 | Dicionário de sinônimos por condição + estrutura ICD; DIFF restrito a capítulos distintos |

## Rodar
```bash
pip install pandas scikit-learn openpyxl scipy kaggle
python src/v1_tfidf.py
python src/v2_chapter.py
python src/v3_hybrid.py
kaggle competitions submit -c cohort-x-task-3 -f submissions/v3_hybrid.csv -m "v3"
```
