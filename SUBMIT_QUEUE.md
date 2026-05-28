# Fila de Submissions (15/dia)

Best atual: **v23 = 0.36177**

## Prioridade (ordem de submit)

| # | Arquivo | Estrategia | Custo (sub) | Esperado |
|---|---------|-----------|-------------|----------|
| 1 | v24_pair_diff.csv | v23 + DIFF pares hipo/hiper | 1 | ±0.01 |
| 2 | v25_sweep_th92.csv | BioBERT threshold 0.92 (entre v22 e v23) | 1 | refina pico |
| 3 | v25_sweep_th94.csv | BioBERT threshold 0.94 (mais estrito) | 1 | testa estritar |
| 4 | v25_sweep_th91.csv | BioBERT threshold 0.91 | 1 | testa relaxar |
| 5 | v25_sweep_th90.csv | BioBERT threshold 0.90 | 1 | confirma 0.85 era ruim |
| 6 | v27a_assoc_all.csv | PROBE: ASSOC=todos | 1 | mede contribuicao ASSOC |
| 7 | v27b_diff_all.csv  | PROBE: DIFF=todos | 1 | mede contribuicao DIFF |
| 8 | v28_llm.csv | LLM-as-classifier (precisa API key) | 1 | ESPERADO 0.50+ |
| 9 | v26_probe_cond00..22 | Per-condition probes (1 por dia se necessario) | varios | mapeia gold |

## Setup LLM (Plano D)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
cd ~/Documents/GitHub/cohort-x-task-3
.venv/bin/pip install -q anthropic
.venv/bin/python src/v28_llm_classifier.py
```

Custo estimado: $1-2 (Claude Sonnet 4.5) ou $0.20 (Haiku/4o-mini).
