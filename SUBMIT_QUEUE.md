# Fila de Submissoes — CohortX Task 3

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Estado atual

- Data do diagnostico: 2026-07-01
- Melhor publico: `0.42453`
- Melhor arquivo confiavel: `submissions/v178_FINAL.csv`
- Hedge privado forte: `submissions/v185_private_kw.csv`
- Limite diario: 20 submissoes/dia
- Finais selecionaveis: 20
- Deadline Kaggle: 2026-07-16 11:59

## Monitoramento 2026-07-01 05:08 UTC

- Cota Kaggle atual: `20/20`; nenhuma nova submissao enviada neste ciclo.
- Proximo reset de cota: 2026-07-02 00:00:00 UTC / 2026-07-01 21:00:00 BRT.
- Rank publico JV: #9 com `0.42453`; o #8 esta em `0.42491`, e uma submissao nova em 2026-07-01 colocou `yingfali` em #4 com `0.49973`.
- Notebooks publicos: sem novos notebooks no filtro correto `--competition cohort-x-task-3`; seguem os mesmos 4 ja baixados em `external_notebooks/`, com ultimos runs em abril/maio.
- Forum/discussoes: busca publica ainda destaca `New Prize for CohortX`; sem novo notebook/forum tecnico acionavel encontrado neste ciclo.
- Ferramenta adaptativa pronta: `src/v221_240_adaptive_followups.py` gera `v221-v240` depois que `v201-v220` estiverem pontuados; agora calcula delta vs `v178_FINAL`, prioriza combos publicos nao negativos, rotula combos negativos apenas como fallback, reserva 4 slots para os melhores combos sobre `v185_private_kw.csv` e pula numeros `vNNN` ja existentes em reexecucoes.
- Novo relatorio de sinais: `reports/2026-07-01-signals.md` compara cada CSV contra `v178_FINAL.csv` e confirma os movers publicos por condicao.
- Novo relatorio de plano: `reports/2026-07-02-plan.md` audita `v201-v220`; todos os 20 arquivos mudam exatamente uma condicao, COPD ou Enlarged Mediastinum.
- Novo scorecard de plano: `reports/2026-07-02-scorecard.md` cruza cada item de `plans/2026-07-02.csv` com o historico Kaggle e classifica `improved/tied/worse/missing_score`; antes do envio todos estao `missing_score`, como esperado.
- Novo comando unico: `.venv/bin/python src/cohortx_ops.py daily-run --date 2026-07-02 --auto-next-plan` encadeia status, validacao, plan-report, submissao, review, signals, plan-scorecard, final-candidates e tentativa de plano seguinte.
- Guarda extra do auto-next: `daily-run` agora so chama o gerador adaptativo se todos os itens do plano anterior constarem no historico Kaggle; se quota ou erro deixar a fila incompleta, imprime `next_plan_guard=prior_plan_incomplete`.
- Dedupe extra: `preflight` e `submit-plan` agora detectam CSVs com conteudo identico a arquivos locais ja submetidos no Kaggle; esses itens entram como `duplicate_content_plan_items` e nao gastam cota.
- Protecao extra: `daily-run` agora aplica a mesma trava de data alvo do `preflight`; se a data for futura/passada, valida o plano, gera plan-report e imprime `date_guard=skip_submit` sem chamar `submit_plan` nem gerar plano adaptativo.
- Trava de deadline: `status`, `preflight`, `daily-run` e `submit-plan` agora exibem deadline/segundos restantes; `preflight` retorna `competition_closed` depois de 2026-07-16 11:59 UTC e `submit-plan` nao chama Kaggle se `competition_open=false`.
- Reserva guardada no comando unico: `daily-run` agora aceita `--reserve-plan` e so seleciona essa fila com `--allow-reserve`; quando usa reserva, gera plan-report contra `v185_private_kw.csv` e imprime `next_plan_guard=reserve_plan` em vez de criar adaptativo em cima da contingencia.
- Novo preflight: `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD` mostra data UTC atual, relacao da data alvo, cota, proximo reset UTC/BRT, plano selecionado e `recommended_action` antes de qualquer envio; em 2026-07-01 04:01 UTC retornou `target_date_relation=future` e `recommended_action=wait_for_target_date` para `plans/2026-07-02.csv`.
- Relatorio final melhorado: `reports/final-candidates.md` agora recomenda uma selecao de 20/20 finais com ancora publica, `v185_private_kw.csv`, empates public-neutral e filtro de volume para deixar mutacoes gigantes apenas em Top Public.
- Plano reserva pronto: `plans/2026-07-03-reserve.csv` (`v241-v260`) combina `v185_private_kw.csv` com mudancas public-neutras/tied. Usar apenas se o adaptativo `v221-v240` nao estiver pronto e houver risco real de perder quota.
- Testes locais: `.venv/bin/python -m unittest discover -s tests -v` passou com 24 testes, cobrindo a orquestracao, reset de cota, deadline guard, scorecard de plano, trava de data no `daily-run`, guarda contra plano incompleto, fallback de reserva com permissao explicita, dedupe por conteudo ja submetido, adaptativo com preferencia por combos nao negativos, slots privados/retry seguro e shortlist final de ate 20 selecionaveis antes do reset.

## Lote enviado em 2026-07-01

| Arquivo | Public | Leitura |
|---|---:|---|
| `v181_kw_mid.csv` | 0.38479 | keyword puro nas medias piora muito |
| `v182_kw_wide.csv` | 0.39712 | keyword wide nas medias piora |
| `v183_kw_chapter.csv` | 0.40019 | keyword+chapter nas medias piora |
| `v184_union_kw.csv` | 0.41953 | adicionar keyword extras nas medias piora pouco |
| `v185_private_kw.csv` | 0.42453 | private hedge neutro no publico |
| `v186_zero_copd.csv` | 0.38913 | COPD e publico/importante |
| `v187_zero_hf.csv` | 0.42453 | Heart Failure invisivel/neutro no publico |
| `v188_zero_hyperthyroid.csv` | 0.42453 | Hyperthyroidism invisivel/neutro no publico |
| `v189_zero_ild.csv` | 0.42453 | ILD invisivel/neutro no publico |
| `v190_zero_derm.csv` | 0.42453 | Dermatomycosis invisivel/neutro no publico |
| `v191_zero_bronchitis.csv` | 0.42453 | Bronchitis invisivel/neutro no publico |
| `v192_zero_npc.csv` | 0.42453 | NPC invisivel/neutro no publico |
| `v193_zero_hypothyroid.csv` | 0.42453 | Hypothyroidism invisivel/neutro no publico |
| `v194_zero_mediastinum.csv` | 0.40365 | Enlarged Mediastinum e publico/importante |
| `v195_add_copd_kw.csv` | 0.42139 | COPD keyword extras adicionam falso positivo |
| `v196_add_hf_kw.csv` | 0.42453 | HF extras neutros no publico |
| `v197_add_ild_kw.csv` | 0.42453 | ILD extras neutros no publico |
| `v198_add_derm_kw.csv` | 0.42453 | Derm extras neutros no publico |
| `v199_add_mediastinum_kw.csv` | 0.42267 | Mediastinum extras adicionam falso positivo |
| `v200_add_npc_kw.csv` | 0.42453 | NPC extras neutros no publico |

## Conclusao do lote

O public LB das "medias" e explicado por COPD + Enlarged Mediastinum:

- `v177_zero_mid = 0.36825`.
- `v186_zero_copd = 0.38913`.
- `v194_zero_mediastinum = 0.40365`.
- Quedas de COPD e mediastino somam exatamente a queda de zerar todas as medias, entao as outras sete medias sao invisiveis no public split.

## Plano para 2026-07-02

Prioridade: 20 probes pequenos, todos offline/reprodutiveis.

1. COPD: testar remocoes por familia de codigos dentro do `v178_FINAL`.
2. COPD: testar variantes terminologia/titulos sem os 11 extras de `v195`.
3. Enlarged Mediastinum: testar remocoes por chapter/familia dentro do `v178_FINAL`.
4. Enlarged Mediastinum: testar adicoes menores que `v199`, uma familia por vez.
5. Privado: reservar 2-4 balas para CKD/UTI/Diabetes/Pneumonia se houver candidata nova realmente diferente.

## Fila pronta para 2026-07-02

Gerada por `src/v201_220_public_targets.py`, registrada em `plans/2026-07-02.csv` e validada por `src/cohortx_ops.py`.

Comandos depois do reset UTC:

```bash
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-02
.venv/bin/python src/cohortx_ops.py daily-run --date 2026-07-02 --auto-next-plan
```

Antes da virada UTC, o segundo comando tambem fica seguro: ele retorna `date_guard=skip_submit` em vez de enviar a fila cedo.

Expandido:

```bash
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-02
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py submit-plan plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py review --date 2026-07-02
.venv/bin/python src/cohortx_ops.py signals --date 2026-07-02
.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py final-candidates
.venv/bin/python src/v221_240_adaptive_followups.py --prior-plan plans/2026-07-02.csv --out-plan plans/2026-07-03.csv
```

O adaptativo de 03/07 so deve rodar depois dos scores completos. Antes disso ele retorna `not_ready` e nao cria arquivo prematuro; quando rodar, `public nonnegative combo` tem prioridade sobre `negative fallback combo`.

Plano reserva se `v221-v240` ainda estiver `not_ready` perto do reset seguinte:

```bash
.venv/bin/python src/v241_260_private_reserve.py
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-03-reserve.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03 --reserve-plan plans/2026-07-03-reserve.csv
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-03-reserve.csv --anchor submissions/v185_private_kw.csv --out reports/2026-07-03-reserve-plan.md
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03 --reserve-plan plans/2026-07-03-reserve.csv --allow-reserve
.venv/bin/python src/cohortx_ops.py daily-run --date 2026-07-03 --reserve-plan plans/2026-07-03-reserve.csv --allow-reserve
```

| Ordem | Arquivo | Hipotese |
|---:|---|---|
| 1 | `v201_copd_no_j20.csv` | remover acute bronchitis de COPD |
| 2 | `v202_copd_no_j31.csv` | remover chronic rhinitis/nasopharyngitis de COPD |
| 3 | `v203_copd_no_j45.csv` | remover asthma de COPD |
| 4 | `v204_copd_no_j81_j82.csv` | remover pulmonary edema/eosinophilia de COPD |
| 5 | `v205_copd_no_j93_j95.csv` | remover pneumothorax/postprocedural de COPD |
| 6 | `v206_copd_no_j96.csv` | remover respiratory failure de COPD |
| 7 | `v207_copd_no_j98.csv` | remover other respiratory disorders de COPD |
| 8 | `v208_copd_core_j41_j42_j43_j44.csv` | COPD so core bronchitis/emphysema/COPD |
| 9 | `v209_copd_no_acute_bronch_asthma.csv` | remover J20+J45 juntos |
| 10 | `v210_copd_add_p25_only.csv` | isolar P25 perinatal emphysema |
| 11 | `v211_copd_add_t79_t81_only.csv` | isolar traumatic/procedural emphysema |
| 12 | `v212_med_no_j98.csv` | remover J98 de mediastino |
| 13 | `v213_med_no_q34.csv` | remover Q34 de mediastino |
| 14 | `v214_med_no_d15.csv` | remover D15 de mediastino |
| 15 | `v215_med_no_c38.csv` | remover C38 de mediastino |
| 16 | `v216_med_only_mediastin_title.csv` | manter so titulos com mediastin |
| 17 | `v217_med_keep_neoplasm_only.csv` | manter so neoplasias/intrathoracic uncertain |
| 18 | `v218_med_add_c852_only.csv` | isolar mediastinal B-cell lymphoma |
| 19 | `v219_med_add_n80b5_only.csv` | isolar endometriosis mediastinal |
| 20 | `v220_med_add_p252_only.csv` | isolar pneumomediastinum perinatal |

Nao repetir:

- `v181`, `v182`, `v183`, `v184` como grupos.
- Adicionar todos os extras de COPD (`v195`) ou de mediastino (`v199`).
- Mexer em Heart Failure, Hyperthyroidism, ILD, Dermatomycosis, Bronchitis, NPC, Hypothyroidism buscando public LB; esses so devem ser usados como hedge privado.

## Finais provisoriamente selecionaveis

1. `v178_FINAL.csv` — melhor publico confiavel.
2. `v185_private_kw.csv` — hedge privado, neutro no publico.

Relatorio vivo: `reports/final-candidates.md`. Regerar depois de cada dia com scores completos para atualizar a selecao recomendada de ate 20 finais, a watchlist e evitar promover probes que cairam no publico.

## Plano reserva 2026-07-03

- Arquivo: `plans/2026-07-03-reserve.csv`.
- Auditoria: `reports/2026-07-03-reserve-plan.md`.
- Gerador: `src/v241_260_private_reserve.py`.
- Uso: contingencia de quota. Priorizar `plans/2026-07-03.csv` adaptativo quando os scores de `v201-v220` existirem. Sem `--allow-reserve`, o preflight deve segurar a reserva com `recommended_action=hold_for_primary_or_rerun_adaptive`.
