# CohortX Task 3 — ICD-10-CM Code Resolution

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Status vivo — 2026-07-02

**Melhor público atual: 0.42687** (`v209_copd_no_acute_bronch_asthma`)
**Leaderboard público: #8/112** em 2026-07-02
**Deadline:** 2026-07-16 11:59
**Limite:** 20 submissões/dia, até 20 finais selecionáveis

> [!important] Revisão de estratégia 2026-07-01 (rev 2): ver `ESTRATEGIA.md`.
> A aba **Train** do `data/Task_3.xlsx` mostra que o gold **popula** `ASSOCIATION` e
> `DIFF` (6 de 10 pares dos exemplos), então deixar `Not Applicable` em tudo concede ~2/3
> das 69 células. O plateau de `0.42453` vem de disputar só a coluna KEEP.
> **Rev 2 (verificado nos dados):** o gold é determinístico (escolher o nó ICD certo e
> expandir todos os descendentes do dicionário); a granularidade do nó importa muito
> (expandir a família 3-char cheia derruba Aortic ASSOC 1.000→0.748, Stroke ASSOC
> 1.000→0.274); e preencher ASSOC/DIFF **não** é de graça, é aposta por célula (~40% do
> gold ASSOC/DIFF é vazio no Train). Frente: preencher ASSOC/DIFF **seletivo** nas
> condições invisíveis, calibrado offline no `src/train_scorer.py` antes de gastar bala.

Repo local sincronizado com `origin/master`: `https://github.com/JVLegend/cohort-x-task-3`.
Foram enviados 20/20 CSVs em 2026-07-01 (`v181`-`v200`). Em 2026-07-02, a automação
submeteu `v201`-`v210`; o Kaggle registrou entradas duplicadas no histórico e esgotou a
cota (`20/20`) antes de `v211`-`v220`. Não reenviar até o reset de 2026-07-03 00:00 UTC.

## Achados novos — 2026-07-02

- `v209_copd_no_acute_bronch_asthma.csv` elevou o melhor público para `0.42687`.
- Remover COPD `J20+J45` junto foi o melhor sinal público (`+0.00234` vs `v178_FINAL`).
- Também melhoraram as remoções isoladas `J45`, `J81/J82`, `J93/J95`, `J20`, `J98` e
  `J31`; remover `J96` ou reduzir COPD ao core `J41/J42/J43/J44` derruba forte.
- `v211`-`v220` continuam não submetidos; o preflight atual retorna `wait_for_quota`.

## Achados novos — 2026-07-01

- Fórum: o host permite Hugging Face e dados Creative Commons/domínio público, mas a solução deve ser offline, reproduzível, sem APIs online/proprietárias, carregável em servidor de 15 GB RAM e sem demora excessiva.
- Notebooks públicos: `reports/2026-07-01-intel.md` confirma 4 notebooks listados e 4 já baixados em `external_notebooks/`; `New public notebooks: 0`. `reports/public-notebook-audit.md` mostra que todos são baselines BioBERT/SentenceTransformer + TF-IDF/BM25 com top-k pequeno e ASSOC/DIFF preenchidos. Não superam a estratégia atual.
- Public split: as mudanças de `CKD`, `UTI`, `Diabetes` e `Pneumonia` continuam invisíveis no público (`v185 = 0.42453`), então são apostas privadas.
- Entre as 9 condições "médias", só duas mexem no público:
  - `COPD`: zerar cai para `0.38913`; impacto `scaled_x23 = -0.81420`.
  - `Enlarged Mediastinum`: zerar cai para `0.40365`; impacto `scaled_x23 = -0.48024`.
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
5. Regerar `reports/final-candidates.md` depois de cada lote pontuado para manter a seleção final objetiva de até 20 arquivos, com âncora pública, hedge privado e filtro contra mutações grandes demais.
6. Usar `plans/2026-07-03-public-contingency.csv` como novo lote público se o adaptativo `v221-v240` não puder virar plano primário. Usar `plans/2026-07-03-reserve.csv` apenas como última contingência de quota. O adaptativo normal prioriza combos com delta público não negativo vs `v178_FINAL`, reserva 16 combos públicos + 4 combos sobre `v185_private_kw`, bloqueia plano primário se não houver combo COPD+Mediastinum não negativo, e pula versões `vNNN` já existentes em reexecuções.
7. Usar `reports/2026-07-02-code-deltas.md` para interpretar os scores de `v201-v220`: ele lista os códigos/títulos ICD exatos adicionados/removidos por probe.
8. Depois dos scores, usar `reports/2026-07-02-impact.md` para transformar cada delta público em ação: promover, podar, manter hedge ou evitar falso positivo.
9. Rodar `preflight` antes de qualquer janela de envio para confirmar cota, próximo reset, deadline, plano selecionado e ação recomendada. Se a data UTC atual já consumiu `20/20`, o preflight canônico retorna `wait_for_quota` em vez de sugerir plano novo para o dia esgotado. Em automação, usar `.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan` sem `--date`, deixando o CLI resolver a data UTC atual. O `daily-run` também recusa data futura/passada ou competição fechada antes de chamar `submit_plan`, deduplica por conteúdo já submetido, rejeita duplicatas internas no plano, só atualiza relatórios pós-submissão quando enviou algo nesta execução ou quando o plano completo já está contabilizado, gera `intel`/`plan-scorecard`, bloqueia submissão se o intel detectar notebook público novo/atualizado ainda não baixado/auditado, aponta `.venv/bin/python src/sync_public_notebooks.py` para baixar/auditar a ref, só cria o próximo plano quando a fila anterior estiver completa no Kaggle, infere a próxima versão pelo maior `vNNN` do plano anterior, reconhece contingência pública antes de reserva e só usa plano reserva com `--allow-reserve`.
10. A automação Codex roda uma janela de retry pós-reset (`00:20`, `01:20`, `02:20 UTC`). Como o pipeline é idempotente, a primeira execução que conseguir envia a cota; as seguintes devem parar em `wait_for_quota`, dedupe ou plano já submetido. Um retry que encontre plano parcial sem envio novo não atualiza os relatórios pós-submissão.

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
2. ~~**ASSOC/DIFF gold são VAZIOS na maioria**~~ **CORRIGIDO 2026-07-01:** a aba Train
   prova que o gold **popula** ASSOC/DIFF (6 de 10 pares). O que derruba é preencher com
   os códigos ERRADOS (probes antigos usaram KEEP como ASSOC/DIFF em todas as condições,
   inclusive as públicas cujo gold é vazio). Ver `ESTRATEGIA.md`.
3. **Cobertura ampla > shrink** para KEEP (o gold Train agrupa a família inteira)
4. **BioBERT médico + sweep threshold** é a alavanca semântica
5. **LLM local 7B aluciнa ICDs** (Thyroiditis→H05 orbit, Epistaxis→D56 thalassemia)
6. **Plateau em 0.42453** disputando só KEEP; ASSOC/DIFF é a frente não explorada
7. **Gold é determinístico** (verificado): escolher o nó ICD certo → expandir todos os
   descendentes no dicionário. O jogo é escolher os nós, não códigos avulsos.
8. **Granularidade do nó decide a precisão**: gold mistura níveis (A50 cheio, mas só
   M352/A539; só H340/H341 de H34). Super-expandir a família cheia mata o F1.
9. **Preencher ASSOC/DIFF é aposta por célula**: ~40% do gold ASSOC/DIFF é vazio (Train),
   e vazio já vale F1=1.0. Encher em bloco é EV negativo; curar seletivo por condição.
10. **Loop de feedback offline** (`src/train_scorer.py`): reproduz a métrica oficial nos
    5 golds do Train (self-check 1.0000). Calibrar aqui antes de gastar bala do Kaggle.

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
submissions/          CSVs gerados e enviados
SUBMIT_QUEUE.md       roteiro de submissões
PLAN_TOMORROW.md      plano operacional da próxima janela
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
