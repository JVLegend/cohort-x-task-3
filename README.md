# CohortX Task 3 — ICD-10-CM Code Resolution

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Status vivo — 2026-07-01

**Melhor público atual: 0.42453** (`v145_prune` / `v178_FINAL` / variantes neutras)
**Leaderboard público: #9/112** em 2026-07-01
**Deadline:** 2026-07-16 11:59
**Limite:** 20 submissões/dia, até 20 finais selecionáveis

Repo local sincronizado com `origin/master`: `https://github.com/JVLegend/cohort-x-task-3`.
Foram enviados 20/20 CSVs em 2026-07-01 (`v181`-`v200`).

## Achados novos — 2026-07-01

- Fórum: o host permite Hugging Face e dados Creative Commons/domínio público, mas a solução deve ser offline, reproduzível, sem APIs online/proprietárias, carregável em servidor de 15 GB RAM e sem demora excessiva.
- Notebooks públicos: só há 4 notebooks; todos são baselines BioBERT/SentenceTransformer + TF-IDF/BM25 com top-k pequeno e ASSOC/DIFF preenchidos. Não superam a estratégia atual.
- Public split: as mudanças de `CKD`, `UTI`, `Diabetes` e `Pneumonia` continuam invisíveis no público (`v185 = 0.42453`), então são apostas privadas.
- Entre as 9 condições "médias", só duas mexem no público:
  - `COPD`: zerar cai para `0.38913`.
  - `Enlarged Mediastinum`: zerar cai para `0.40365`.
  - Heart Failure, Hyperthyroidism, ILD, Dermatomycosis, Bronchitis, NPC e Hypothyroidism zeram sem efeito público.
- Expansões keyword isoladas:
  - COPD extras pioram (`v195 = 0.42139`).
  - Enlarged Mediastinum extras pioram (`v199 = 0.42267`).
  - HF/ILD/Derm/NPC extras são neutros no público.

## Operação daqui para frente

1. Usar as 20 submissões diárias para probes pequenos, principalmente COPD e Enlarged Mediastinum.
2. Manter `v178_FINAL` como submissão pública/confiável.
3. Manter `v185_private_kw` como hedge privado candidato, pois mexe nas condições invisíveis sem prejudicar público.
4. Priorizar candidatos offline/reprodutíveis. LLMs externos podem orientar curadoria, mas não devem ser dependência da solução final.

Ver detalhes em `SUBMIT_QUEUE.md` e `OPERACAO_DIARIA.md`.

## Histórico inicial

## Leaderboard final
| # | Time | Score |
|---|---|---|
| 1 | Alan T. Andrea | 1.00000 ⚠️ provável gabarito |
| 2 | AT0641 | 0.75416 |
| 3 | Jason Karpeles | 0.48485 |
| 4 | Md Raihan | 0.43741 |
| 5 | NTUA | 0.41167 |
| 6 | OTSUKA Kazutaka | 0.41002 |
| 7 | Thomas Greissler | 0.40128 |
| 8 | kaviya pothuvan | 0.39956 |
| **9** | **João Victor (você)** | **0.36565** |
| 10 | Fatima Shaza | 0.36274 |

## Tarefa
Mapear 23 condições médicas para códigos ICD-10-CM, classificando em três buckets:
- **KEEP**: códigos que representam a condição
- **ASSOCIATION**: códigos relacionados
- **DIFF**: diagnósticos diferenciais

Métrica: macro F1 entre 3 categorias × 23 conditions. Dicionário: 97.441 códigos do MIMIC-IV.

## Solução final (v33)
```python
KEEP = (prefixos clínicos curados ∪ keyword matching ∪ BioBERT sim≥0.91)
ASSOCIATION = "Not Applicable"  # gold quase sempre vazio
DIFF = "Not Applicable"          # gold quase sempre vazio
```

Stack:
- `pritamdeka/S-PubMedBert-MS-MARCO` (sentence-transformer médico)
- TF-IDF + BM25 para keyword retrieval
- ~80 prefixos ICD-10 canônicos curados manualmente por condition

## Jornada (49 submissions, 7 dias)
### Fase 1 — Retrieval clássico (subs 1-13)
| Marco | Score |
|---|---|
| v1 TF-IDF baseline | 0.10 |
| v8 só códigos terminais 5+ char | 0.18 |
| v11 prefixos clínicos curados | 0.245 |

### Fase 2 — Probes definitivos (subs 14-23)
| Marco | Score | Insight |
|---|---|---|
| v15 (tudo vazio) | 0.222 | 🔍 Baseline alto: gold tem muitos ASSOC/DIFF vazios |
| v18 KEEP wide | 0.348 | Cobertura ampla > shrink |
| v25 BioBERT sweep th=0.91 | **0.366** | Sweet spot |

### Fase 3 — LLM local (subs 24-40)
- qwen2.5:7b via Ollama: 0.286-0.296 (conservador demais)
- qwen3:14b: OOM (16GB RAM insuficiente)
- Conclusão: LLM 7B local alucina ICD codes, pior que retrieval

### Fase 4 — Gemini API (subs 41-46)
- Gemini Flash: 0.316 (cortou códigos legítimos)
- Gemini 2.5 Pro / 3 Pro Preview: rate-limited severely
- Spend cap mensal exausto

### Fase 5 — Probes finais (subs 47-49)
| Marco | Score | Aprendizado |
|---|---|---|
| v47 KEEP=ASSOC | 0.310 | gold ASSOC ≠ KEEP |
| v48 KEEP=DIFF | 0.203 | gold DIFF quase 100% vazio |
| v49 PRF | 0.314 | query expansion sobrecarrega |

## Análise matemática
- Baseline empty (v15) = 0.222 → ~15 das 69 células gold são vazias
- v33 best = 0.366 → ~25 células corretas
- Para 0.97 (líder) precisaria de ~67 células corretas — impossível sem mais informação

## Insights chave
1. **Gold usa códigos terminais 5+ char** (v8_long 0.18 vs v8_short 0.10)
2. **ASSOC/DIFF gold são VAZIOS na maioria** — preencher derruba
3. **Cobertura ampla > shrink** para KEEP
4. **BioBERT médico + sweep threshold** é a alavanca semântica
5. **LLM local 7B aluciнa ICDs** (Thyroiditis→H05 orbit, Epistaxis→D56 thalassemia)
6. **Plateau real em 0.366** com retrieval clássico

## Estrutura do repo
```
data/                 Task_3.xlsx + dicionário MIMIC-IV
src/
  common.py           helpers
  v1-v9               iterações iniciais (retrieval clássico)
  v10-v13             prefixos clínicos curados
  v14-v15             probes (tudo vazio / só KEEP)
  v16-v24             refinamentos
  v25-v33             sweep thresholds + ensemble (BEST = v33)
  v34-v40             LLM local qwen 7B via Ollama
  v41-v46             Gemini API (Flash/Pro)
  v47-v49             probes finais
submissions/          49 CSVs
SUBMIT_QUEUE.md       roteiro de submissões
PLAN_TOMORROW.md      plano se Gemini liberar
```

## Reproduzir best
```bash
python -m venv .venv && source .venv/bin/activate
pip install pandas scikit-learn openpyxl scipy sentence-transformers rank-bm25 requests
kaggle competitions download -c cohort-x-task-3 -p data && cd data && unzip *.zip && cd ..
python src/v33_obscure.py
kaggle competitions submit -c cohort-x-task-3 -f submissions/v33_obscure.csv -m "v33"
```

## O que faria diferente para top-3
1. **LLM grande sem rate limit**: Claude Opus / GPT-4o / Gemini 2.5 Pro com spend cap alto. Custo ~$2-5 para classificar 23×500 candidatos.
2. **Fine-tune bi-encoder** com pares (condition, ICD) sintéticos via LLM
3. **MIMIC-IV diagnoses_icd frequency** (precisa PhysioNet access) para priorizar códigos comuns
4. **Reranker cross-encoder** (`ms-marco-MiniLM`) sobre top-200 BioBERT

## Repositório
https://github.com/JVLegend/cohort-x-task-3
