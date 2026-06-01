# CohortX Task 3 — ICD-10-CM Code Resolution

**🥉 Posição final: #9 mundial** (de >50 participantes)
**Best score: 0.36565** (v33, retrieval híbrido com BioBERT)

## Leaderboard
| Posição | Time | Score |
|---|---|---|
| 1 | Alan T. Andrea | 1.00000 |
| 2 | AT0641 | 0.74242 |
| 3 | Jason Karpeles | 0.48485 |
| 4 | Md Raihan | 0.43741 |
| 5 | Kyriaki Kolpetinou | 0.41167 |
| 6 | OTSUKA Kazutaka | 0.40911 |
| 7 | Thomas Greissler | 0.40128 |
| 8 | kaviya pothuvan | 0.39956 |
| **9** | **João Victor (eu)** | **0.36565** |
| 10 | Fatima Shaza | 0.36274 |

## Tarefa
Mapear 23 condições médicas para códigos ICD-10-CM, classificando em três buckets:
- **KEEP**: códigos que representam a condição
- **ASSOCIATION**: códigos relacionados
- **DIFF**: diagnósticos diferenciais

Métrica: macro F1 entre as 3 categorias × 23 conditions. Dicionário: 97.441 códigos do MIMIC-IV.

## Solução vencedora (v33)
```bash
KEEP = (prefixos clínicos curados ∪ keyword matching ∪ BioBERT sim≥0.91)
ASSOCIATION = "Not Applicable"
DIFF = "Not Applicable"
```

Stack:
- `pritamdeka/S-PubMedBert-MS-MARCO` (sentence-transformer médico, 420 MB)
- TF-IDF + BM25 para keyword retrieval
- Prefixos ICD-10 canônicos curados manualmente por condition

## Jornada (41 submissions em 3 dias)
| Marco | Score | Insight |
|---|---|---|
| v1 TF-IDF | 0.10 | Baseline |
| v8 só terminais | 0.18 | Gold usa códigos 5+ char |
| v11 prefixos clínicos | 0.245 | Conhecimento médico bate retrieval cego |
| v15 (probe: tudo vazio) | 0.222 | 🔍 Gold tem ASSOC/DIFF vazios em maioria |
| v18 KEEP wide | 0.348 | Cobertura ampla > shrink |
| v25 BioBERT th=0.91 | 0.366 | Sweet spot threshold |
| **v33** | **0.36565** | **Best, plateau de retrieval** |
| v34-v40 LLM 7B | <0.36 | LLM local insuficiente |

## Insights chave
1. **Gold usa códigos terminais 5+ char** (v8_long 0.18 vs v8_short 0.10)
2. **ASSOC/DIFF gold são VAZIOS na maioria** — preencher derruba o score
3. **Cobertura ampla > shrink** — não restringir KEEP por top-K
4. **BioBERT médico + sweep de threshold** é a alavanca semântica
5. **LLM local 7B** (qwen2.5) alucina ICDs — modelo grande seria necessário

## Estrutura
```
data/                 Task_3.xlsx + dicionário MIMIC-IV
src/
  common.py           helpers
  v1-v9               iterações iniciais (retrieval clássico)
  v10-v13             prefixos clínicos
  v14-v15             probes (tudo vazio / só KEEP)
  v16-v24             refinamentos
  v25-v33             sweep thresholds + ensemble (BEST)
  v34-v40             LLM local (qwen2.5:7b via Ollama)
submissions/          41 CSVs
SUBMIT_QUEUE.md       roteiro de submissões
```

## Reproduzir best
```bash
python -m venv .venv && source .venv/bin/activate
pip install pandas scikit-learn openpyxl scipy sentence-transformers rank-bm25 requests
kaggle competitions download -c cohort-x-task-3 -p data && cd data && unzip *.zip && cd ..
python src/v33_obscure.py
kaggle competitions submit -c cohort-x-task-3 -f submissions/v33_obscure.csv -m "v33"
```

## O que faria diferente
1. Usar Claude/GPT-4o API ($1-2) para classificação fina dos top-200 candidatos BioBERT
2. Probe de ASSOC/DIFF por condition individualmente (gasta subs mas mapeia gold)
3. Fine-tune bi-encoder com pares (condition, ICD) sintéticos
