# Fila de Submissoes — CohortX Task 3

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

> [!important] Revisao de estrategia 2026-07-01 (ver `ESTRATEGIA.md`).
> A regra "ASSOCIATION/DIFF ficam Not Applicable" esta baseada num pressuposto falso: a
> aba Train do `Task_3.xlsx` mostra gold ASSOC/DIFF populado. A proxima fila deve priorizar
> popular ASSOC/DIFF nas condicoes invisiveis no publico, nao mais ablacões de COPD/Mediastinum.

## Estado atual

- Data do diagnostico: 2026-07-04
- Melhor publico: `0.43156`
- Melhor arquivo publico: `submissions/v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv` / `submissions/v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv`
- Melhor arquivo confiavel anterior: `submissions/v178_FINAL.csv`
- Hedge privado forte: `submissions/v185_private_kw.csv`
- Limite diario: 20 submissoes/dia
- Finais selecionaveis: 20
- Deadline Kaggle: 2026-07-16 11:59

## Monitoramento 2026-07-04 00:24 UTC

- Preflight inicial estava verde: `competition_open=true`, `target_date_relation=current`,
  `quota_used_utc=0/20`, `recommended_action=submit_primary` e
  `selected_plan=plans/2026-07-04.csv`.
- `daily-run --auto-next-plan` submeteu `v301`-`v320` completos. O preflight pos-envio
  retornou `quota_used_utc=20/20`, `primary_unsubmitted_items=0` e
  `recommended_action=primary_already_submitted`; retries posteriores devem parar no
  dedupe/preflight.
- Melhor novo score: `v301` e `v302` empataram em `0.43156`, combinando o anchor COPD
  `v296`, thymus/nodes em mediastino, ASSOC-only e o hedge KEEP privado `v185`.
- Leitura do lote: 11/20 melhoraram contra `v296`; `v303`/`v304` foram o segundo bloco
  (`0.43035`), `v305`/`v306`/`v317` ficaram em `0.43015`, e reintroduzir `J81/J82` ou
  `J93/J95` no COPD derrubou para `0.42855`-`0.42894`.
- Notebooks publicos: `new_public_notebooks=0`, `updated_public_notebooks=0`; auditoria
  publica foi regenerada sem bloquear submissao.
- `reports/2026-07-04.md`, `reports/2026-07-04-signals.md`,
  `reports/2026-07-04-scorecard.md`, `reports/2026-07-04-impact.md`,
  `reports/final-candidates.md` e `reports/final-selection-audit.md` foram atualizados.
- Proxima acao segura: aguardar reset de 2026-07-05 UTC. O plano primario agora e
  `plans/2026-07-05.csv` (`v341`-`v360`), validado com 20 itens, 20 unsubmitted e
  0 duplicate_content; preflight manual para 2026-07-05 retorna
  `recommended_action=wait_for_target_date` enquanto a data UTC ainda e 2026-07-04.
- A contingencia `plans/2026-07-05-public-contingency.csv` (`v361`-`v380`) permanece como
  paraquedas apenas se o primario `plans/2026-07-05.csv` nao estiver utilizavel no reset.

## Monitoramento 2026-07-03 00:25 UTC

- Preflight inicial estava verde: `competition_open=true`, `target_date_relation=current`,
  `quota_used_utc=0/20`, `recommended_action=submit_primary` e
  `selected_plan=plans/2026-07-03.csv`.
- `daily-run --auto-next-plan` submeteu `v281`-`v300` completos. O preflight pos-envio
  retornou `recommended_action=primary_already_submitted`, entao retries posteriores devem
  parar no dedupe/preflight sem gastar cota.
- Status final Kaggle: `20/20`, `unique_submission_events_today=20`,
  `duplicate_submission_rows_today=0`, `local_ledger_submissions_today=20`, proximo reset
  `2026-07-04 00:00:00 UTC` / `2026-07-03 21:00:00 BRT`.
- Melhor novo score: `v296_copd_no_j20_j45_j81_j82_j93_j95.csv = 0.42995`, rank publico
  #8 no intel atualizado.
- Melhor leitura publica: o combo COPD removendo `J20+J45+J81/J82+J93/J95` superou `v209`
  em `+0.00308`; `v293`, `v294`, `v295` e `v300` melhoraram contra `v209`, mas ficaram
  abaixo de `v296`.
- ASSOC-only (`v283`, `v286`) ficou perto do topo (`0.42828`), enquanto DIFF ou
  ASSOC+DIFF amplos derrubaram forte; manter esses como sinais de risco publico, nao como
  promocao direta.
- Notebooks publicos: `new_public_notebooks=0`, `updated_public_notebooks=0`; forum sem
  topico novo desde 2026-06-12.
- `reports/2026-07-03.md`, `reports/2026-07-03-signals.md`,
  `reports/2026-07-03-scorecard.md`, `reports/2026-07-03-impact.md` e
  `reports/final-candidates.md` foram atualizados.
- Proxima acao segura: aguardar reset de 2026-07-04 UTC. O plano primario agora e
  `plans/2026-07-04.csv` (`v301`-`v320`), refinado para combinar em todos os candidatos
  o melhor COPD publico (`v296`) ou suas variantes proximas com o ganho de mediastino
  `v300`, ASSOC-only/neutros e hedge `v185`. A contingencia
  `plans/2026-07-04-public-contingency.csv` (`v321`-`v340`) permanece como paraquedas.
  `plans/2026-07-04.csv` foi validado com 20 itens, 20 unsubmitted e 0 duplicate_content.
- Para reduzir risco do reset seguinte, a contingencia publica de 2026-07-05 tambem esta
  pronta: `plans/2026-07-05-public-contingency.csv` (`v361`-`v380`), gerada por
  `src/v341_360_july5_contingency.py` e auditada em
  `reports/2026-07-05-public-contingency-plan.md` /
  `reports/2026-07-05-public-contingency-code-deltas.md`. Ela nao substitui o adaptativo
  primario pos-`v301-v320`; deixa `v341`-`v360` livres para esse primario e so deve ser
  usada se `plans/2026-07-05.csv` nao existir perto do reset.
- Adaptativo primario de 2026-07-05 preparado: `src/v341_360_post_july4_followups.py`
  sera escolhido automaticamente depois que `v301`-`v320` estiverem completos. Ele promove
  apenas composites public-neutral/positivos contra `v296` e cria variantes que isolam
  mediastino, `v185` e ASSOC/DIFF. Enquanto os scores faltarem ou todos os composites
  perderem publico, retorna `not_ready` e deixa a contingencia `v361`-`v380` como plano seguro.
- Shortlist final reforcada: `reports/final-candidates.md` foi regenerado com anchors
  historicos conhecidos mesmo fora da listagem recente da Kaggle (`v178`, `v185`) e hedges
  near-best ate `0.00325` abaixo de `v296`; agora tambem preenche reservas publicas
  controladas ate `0.00600` abaixo do melhor, com selecao recomendada 20/20 e CSV em
  `reports/final-selection.csv`.
- Readiness do proximo reset: `reports/2026-07-04-readiness.md` consolida preflight,
  guarda de notebooks publicos e shortlist final. Estado atual: plano primario
  `plans/2026-07-04.csv` pronto com 20 validos/20 unsubmitted/0 duplicatas, cota
  `20/20` ate o reset `2026-07-04 00:00:00 UTC`, notebooks publicos `new=0, updated=0`
  e shortlist final `20/20`.
- Auditoria de carteira final: `reports/final-selection-audit.md` mostra selecao
  `20/20`, piso publico `0.42453`, queda maxima `0.00542`, 4 slots ASSOC/DIFF,
  8 slots com mudanca non-COPD e alerta `condition_concentration=crowded` porque
  COPD aparece em 17/20 slots. Isso orienta a troca futura: substituir reservas
  COPD-only de menor valor por hedges privados/non-COPD public-neutral quando surgirem.
- Contingencia publica de 2026-07-06 pronta: `plans/2026-07-06-public-contingency.csv`
  (`v401`-`v420`), gerada por `src/v401_420_july6_contingency.py` e auditada em
  `reports/2026-07-06-public-contingency-plan.md` /
  `reports/2026-07-06-public-contingency-code-deltas.md`. Ela preserva `v381`-`v400`
  para o adaptativo primario pos-05/07 e so deve ser usada se `plans/2026-07-06.csv`
  nao existir perto do reset.
- Contingencia publica de 2026-07-07 pronta: `plans/2026-07-07-public-contingency.csv`
  (`v441`-`v460`), gerada por `src/v441_460_july7_contingency.py` e auditada em
  `reports/2026-07-07-public-contingency-plan.md` /
  `reports/2026-07-07-public-contingency-code-deltas.md`. Ela preserva `v421`-`v440`
  para o adaptativo primario pos-06/07 e recombina apenas sinais publicos/near-publicos
  (`v293`-`v295`, `v300`, `v283`, `v286`, `v287`, `v288`), sem novas fatias privadas.
- Contingencia publica de 2026-07-08 pronta: `plans/2026-07-08-public-contingency.csv`
  (`v481`-`v500`), gerada por `src/v481_500_july8_contingency.py` e auditada em
  `reports/2026-07-08-public-contingency-plan.md` /
  `reports/2026-07-08-public-contingency-code-deltas.md`. Ela preserva `v461`-`v480`
  para o adaptativo primario pos-07/07 e testa KEEP em condicoes public-neutral
  (HF, thyroid, ILD, Dermatomycosis, Bronchitis, NPC) sobre `v296`.
- Contingencia publica de 2026-07-09 pronta: `plans/2026-07-09-public-contingency.csv`
  (`v521`-`v540`), gerada por `src/v521_540_july9_assoc_isolations.py` e auditada em
  `reports/2026-07-09-public-contingency-plan.md` /
  `reports/2026-07-09-public-contingency-code-deltas.md`. Ela preserva `v501`-`v520`
  para o adaptativo primario pos-08/07 e isola ASSOC-only por condicao sobre `v296`,
  diagnosticando qual parte de `v283`/`v286` carrega o ganho publico.
- Contingencia publica de 2026-07-10 pronta: `plans/2026-07-10-public-contingency.csv`
  (`v561`-`v580`), gerada por `src/v561_580_july10_diff_isolations.py` e auditada em
  `reports/2026-07-10-public-contingency-plan.md` /
  `reports/2026-07-10-public-contingency-code-deltas.md`. Ela preserva `v541`-`v560`
  para o adaptativo primario pos-09/07 e isola DIFF-only por condicao sobre `v296`,
  diagnosticando se existe algum DIFF individual aproveitavel apesar da queda do DIFF amplo.
- Contingencia publica de 2026-07-11 pronta: `plans/2026-07-11-public-contingency.csv`
  (`v601`-`v620`), gerada por `src/v601_620_july11_keep_prunes.py` e auditada em
  `reports/2026-07-11-public-contingency-plan.md` /
  `reports/2026-07-11-public-contingency-code-deltas.md`. Ela preserva `v581`-`v600`
  para o adaptativo primario pos-10/07 e testa podas KEEP em condicoes privadas sem
  tocar nos movers publicos COPD/Mediastinum.
- Contingencia publica de 2026-07-12 pronta: `plans/2026-07-12-public-contingency.csv`
  (`v641`-`v660`), gerada por `src/v641_660_july12_prune_assoc.py` e auditada em
  `reports/2026-07-12-public-contingency-plan.md` /
  `reports/2026-07-12-public-contingency-code-deltas.md`. Ela preserva `v621`-`v640`
  para o adaptativo primario pos-11/07 e combina poda KEEP + ASSOC-only por condicao,
  mantendo DIFF vazio e COPD/Mediastinum intocados.
- Contingencia publica de 2026-07-13 pronta: `plans/2026-07-13-public-contingency.csv`
  (`v681`-`v700`), gerada por `src/v681_700_july13_prune_diff.py` e auditada em
  `reports/2026-07-13-public-contingency-plan.md` /
  `reports/2026-07-13-public-contingency-code-deltas.md`. Ela preserva `v661`-`v680`
  para o adaptativo primario pos-12/07 e combina poda KEEP + DIFF-only por condicao;
  usar apenas como fallback, ja que DIFF amplo foi negativo no publico.
- Contingencia publica de 2026-07-14 pronta: `plans/2026-07-14-public-contingency.csv`
  (`v721`-`v740`), gerada por `src/v721_740_july14_prune_assocdiff.py` e auditada em
  `reports/2026-07-14-public-contingency-plan.md` /
  `reports/2026-07-14-public-contingency-code-deltas.md`. Ela preserva `v701`-`v720`
  para o adaptativo primario pos-13/07 e combina poda KEEP + ASSOC+DIFF por condicao;
  usar apenas se o adaptativo nao existir, pois e a combinacao de maior risco publico.
- Contingencia publica de 2026-07-15 pronta: `plans/2026-07-15-public-contingency.csv`
  (`v761`-`v780`), gerada por `src/v761_780_july15_multi_keep_prunes.py` e auditada em
  `reports/2026-07-15-public-contingency-plan.md` /
  `reports/2026-07-15-public-contingency-code-deltas.md`. Ela preserva `v741`-`v760`
  para o adaptativo primario pos-14/07 e cria carteiras multi-condicao de podas KEEP
  privadas, mantendo ASSOC/DIFF vazios.
- Contingencia publica final de 2026-07-16 pronta: `plans/2026-07-16-public-contingency.csv`
  (`v801`-`v820`), gerada por `src/v801_820_july16_final_blends.py` e auditada em
  `reports/2026-07-16-public-contingency-plan.md` /
  `reports/2026-07-16-public-contingency-code-deltas.md`. Ela preserva `v781`-`v800`
  para o adaptativo primario pos-15/07 e mistura med `v300`, `v185`, zero/add hidden,
  podas KEEP e ASSOC-only seletivo, mantendo DIFF vazio para a janela final.

## Monitoramento 2026-07-02 00:24 UTC

- Preflight inicial estava verde: `competition_open=true`, `target_date_relation=current`,
  `recommended_action=submit_primary`, `primary_valid_items=20`, `primary_unsubmitted_items=20`.
- `daily-run --auto-next-plan` submeteu `v201`-`v210`; `v211` falhou com erro Kaggle de
  cota diaria esgotada.
- Status final Kaggle: `20/20`, `quota_remaining=0`, proximo reset
  `2026-07-03 00:00:00 UTC` / `2026-07-02 21:00:00 BRT`.
- O historico Kaggle mostra duplicatas para a maioria de `v202`-`v210`; tratar a cota do
  dia como consumida e nao forcar submissao manual.
- Rechecagem 2026-07-02 01:15 UTC: a listagem tinha `raw_today=20`, `unique_submission_events_today=13`
  e `duplicate_submission_rows_today=7`; tentativa controlada de enviar `v211` confirmou o limite
  real do servidor (`daily Submission allowance (20)`), entao a cota bruta da Kaggle e autoritativa.
- Preflight final: `recommended_action=wait_for_quota`, `quota_used_utc=20/20`,
  `primary_unsubmitted_items=10`.
- Melhor novo score: `v209_copd_no_acute_bronch_asthma.csv = 0.42687`, rank publico #8
  no intel atualizado.
- `reports/2026-07-02-scorecard.md` e `reports/2026-07-02-impact.md` foram atualizados
  com 10/20 itens pontuados; `v211`-`v220` seguem `missing_score`.
- Notebooks publicos: dry-run segue com `new_public_notebooks=0`,
  `updated_public_notebooks=0`.
- Protecao implementada apos a corrida: `daily-run` e `submit-plan` agora usam
  `.cohortx_locks/submission.lock`; uma segunda instancia simultanea deve imprimir
  `submission_lock_held=true` e sair sem gastar cota. `submit_plan` tambem refresca cota,
  filenames e hash de conteudo antes de cada upload.
- Protecao adicional pos-incidente: `preflight` agora exibe `unique_submission_events_today`,
  `duplicate_submission_rows_today` e `local_ledger_submissions_today`. A cota continua usando as
  linhas brutas do servidor, mas `submit-plan` grava sucessos em
  `.cohortx_locks/submission-ledger-YYYY-MM-DD.json` e pula esses arquivos em retries locais mesmo
  se a listagem Kaggle ainda nao refletir a submissao. Se o servidor responder limite diario,
  imprime `kaggle_quota_error=true` e para limpo sem traceback.
- Proxima acao segura: aguardar reset de 2026-07-03 UTC. O plano primario agora e
  `plans/2026-07-03.csv` (`v281`-`v300`), gerado por `src/v281_300_assoc_diff.py` sobre
  `v209`: 12 probes ASSOC/DIFF privados, 4 combos publicos de COPD e 4 probes de
  mediastino. `plans/2026-07-03-public-contingency.csv` e `plans/2026-07-03-reserve.csv`
  ficam como contingencias.
- Preflight de 2026-07-03: `target_date_relation=future`, `primary_valid_items=20`,
  `primary_unsubmitted_items=20`, `primary_duplicate_content_items=0`,
  `recommended_action=wait_for_target_date`, `selected_plan=plans/2026-07-03.csv`.
- Adaptativo pos-ASSOC/DIFF pronto: `src/v301_320_post_assocdiff_followups.py` sera escolhido
  automaticamente pelo `daily-run --auto-next-plan` quando o plano anterior contiver
  `assocdiff`. Depois dos scores de `v281`-`v300`, ele tenta criar `plans/2026-07-04.csv`
  (`v301`-`v320`) combinando ASSOC/DIFF public-neutral com os melhores KEEP publicos de
  COPD/mediastino e o hedge `v185`. Se os scores ainda faltarem ou nenhum ASSOC/DIFF for
  public-neutral, falha seguro com `next_plan_not_ready`.
- Contingencia de 2026-07-04 pronta: `plans/2026-07-04-public-contingency.csv`
  (`v321`-`v340`), gerada por `src/v321_340_july4_contingency.py`. Usar somente se o
  adaptativo pos-score de 03/07 nao criar `plans/2026-07-04.csv` a tempo.

## Monitoramento 2026-07-01 12:18 UTC

- Cota Kaggle atual rechecada: `20/20`; nenhuma nova submissao enviada neste ciclo.
- Proximo reset de cota: 2026-07-02 00:00:00 UTC / 2026-07-01 21:00:00 BRT.
- Rank publico JV: #9 com `0.42453`; o #8 esta em `0.42491`, e uma submissao nova em 2026-07-01 colocou `yingfali` em #4 com `0.49973`.
- Intel automatizado: `.venv/bin/python src/cohortx_ops.py intel --date 2026-07-01` gerou `reports/2026-07-01-intel.md` com notebooks, leaderboard, status da pagina de discussoes e ultimas submissões JV.
- Notebooks publicos: sem novos notebooks no filtro correto `--competition cohort-x-task-3`; `Public notebooks listed: 4`, `Downloaded notebook refs: 4`, `New public notebooks: 0`.
- Auditoria dos notebooks baixados: `reports/public-notebook-audit.md` confirma que os 4 notebooks publicos sao baselines de retrieval/embedding e todos preenchem `ASSOCIATION`/`DIFF` por top-k ou thresholds; usar apenas como ideias fracas de BM25/TF-IDF/abbreviation expansion, nao como politica de submissao.
- Forum/discussoes: `src/cohortx_ops.py intel` agora consulta `competitions.CompetitionApiService/ListCompetitionTopics` e `ListTopicMessages` diretamente. Em 2026-07-02 retornou 2 topicos (`Use of external data sources for task 3` e `New Prize for CohortX`), sem topico novo desde 2026-06-12. Sinal tecnico acionavel: processamento final precisa ser offline/reproduzivel, sem APIs online ou dados proprietarios; Hugging Face baixavel e dados Creative Commons/Public Domain sao permitidos; mirar execucao em servidor de 15 GB RAM.
- Ferramenta adaptativa pronta: `src/v221_240_adaptive_followups.py` gera `v221-v240` depois que `v201-v220` estiverem pontuados; agora calcula delta vs `v178_FINAL`, prioriza combos publicos nao negativos, rotula combos negativos apenas como fallback, reserva 4 slots para os melhores combos sobre `v185_private_kw.csv` e pula numeros `vNNN` ja existentes em reexecucoes.
- Guarda nova do adaptativo: por padrao, `v221_240_adaptive_followups.py` recusa criar plano primario se nao houver ao menos um combo COPD+Mediastinum com delta publico >= 0 em ambos os lados. Se todos os sinais publicos vierem negativos, preferir o novo lote publico `plans/2026-07-03-public-contingency.csv`; usar `plans/2026-07-03-reserve.csv` perto do reset apenas se a prioridade for nao perder quota. `--allow-negative-fallback` e override manual, nao rotina.
- Novo lote publico de contingencia: `src/v261_280_public_contingency.py` gerou `plans/2026-07-03-public-contingency.csv` (`v261-v280`) com ablacões finas de COPD core (`J40/J41/J42/J43/J44/J47`), adicoes pequenas de bronchiectasis, ablacões finas de mediastino (`C78/D38/J85`) e adicoes thymus/linfonodos intratoracicos. Preflight manual para 2026-07-03 mostra 20 validos, 20 unsubmitted, 0 duplicate_content e `wait_for_target_date`; quando a data for atual e o primario `plans/2026-07-03.csv` nao existir, o `recommended_action` sera `submit_public_contingency`.
- Novo relatorio de sinais: `reports/2026-07-01-signals.md` compara cada CSV contra `v178_FINAL.csv`, confirma os movers publicos por condicao e agora inclui `scaled_x23`/ranking de sensibilidade publica. COPD tem impacto escalado `-0.81420`; Enlarged Mediastinum, `-0.48024`.
- Novo relatorio de plano: `reports/2026-07-02-plan.md` audita `v201-v220`; todos os 20 arquivos mudam exatamente uma condicao, COPD ou Enlarged Mediastinum.
- Novo relatorio de deltas ICD: `reports/2026-07-02-code-deltas.md` lista os codigos/titulos exatos adicionados ou removidos em cada item `v201-v220`, para mapear scores futuros de volta a familias ICD.
- Novo scorecard de plano: `reports/2026-07-02-scorecard.md` cruza cada item de `plans/2026-07-02.csv` com o historico Kaggle e classifica `improved/tied/worse/missing_score`; antes do envio todos estao `missing_score`, como esperado.
- Novo relatorio de impacto: `reports/2026-07-02-impact.md` cruza score publico, delta vs `v178_FINAL` e deltas ICD para recomendar promover/podar/manter hedge/evitar falso positivo assim que `v201-v220` pontuarem.
- Novo comando unico canonico: `.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan` encadeia status, intel pre-submissao, preflight, validacao, plan-report, submissao, review, signals, plan-scorecard, final-candidates e tentativa de plano seguinte usando a data UTC atual.
- Preferencia para automacao: usar `.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan` sem `--date`, porque o CLI resolve a data UTC atual e evita rodar com data manual errada.
- Guarda de notebooks novos/atualizados: apos gerar `reports/YYYY-MM-DD-intel.md`, o `daily-run` agora para antes do `preflight`/submissao se `New public notebooks` ou `Updated public notebooks` for maior que zero, imprimindo `new_public_notebooks_guard=N` e o comando `.venv/bin/python src/sync_public_notebooks.py`; o sync mostra `pending_public_notebooks`, `new_public_notebooks` e `updated_public_notebooks`. Baixar, diffar e auditar o notebook antes de seguir. `--allow-new-notebooks` e override manual depois dessa auditoria, nao rotina da automacao.
- Retry da automacao Codex: `cohortx-task-3-daily-submission-loop` roda as `00:20`, `01:20` e `02:20 UTC` ate o deadline. As tentativas extras sao seguras: se a primeira ja consumiu a cota ou submeteu o plano, as proximas param em `wait_for_quota`, dedupe ou plano ja submetido; se encontrarem plano parcial sem envio novo, nao atualizam os relatorios pos-submissao.
- Guarda de pos-relatorios: quando o `daily-run` roda antes da data alvo, com plano incompleto sem envio novo ou sem atividade real no historico Kaggle, ele imprime `post_reports_guard=no_current_plan_activity` e nao atualiza review/signals/scorecard/final-candidates.
- Guarda extra do auto-next: `daily-run` agora so chama o gerador adaptativo se todos os itens do plano anterior constarem no historico Kaggle; se quota ou erro deixar a fila incompleta, imprime `next_plan_guard=prior_plan_incomplete`. Quando `--start-version` nao e informado, ele infere automaticamente a proxima versao a partir do maior `vNNN` do plano anterior (`v201-v220` -> `221`, `v281-v300` -> `301`, `v261-v280` -> `281`) e pula versoes ja existentes em `submissions/`; apos `v301-v320`, o proximo adaptativo deve comecar em `v341` para preservar a contingencia `v321-v340`. Planos `v301-v320` e planos modernos `v341+` usam `src/v341_360_post_july4_followups.py` com anchor `v296`; planos `v281-v300` com `assocdiff` usam `src/v301_320_post_assocdiff_followups.py` com anchor `v209`; os demais usam `src/v221_240_adaptive_followups.py`. `plan-report`, `plan-scorecard` e `audit_plan_deltas.py` agora inferem essa ancora por plano quando `--anchor` nao e informado.
- Dedupe extra: `preflight` e `submit-plan` agora detectam CSVs com conteudo identico a arquivos locais ja submetidos no Kaggle; esses itens entram como `duplicate_content_plan_items` e nao gastam cota.
- Dedupe intra-plano: `validate-plan` agora rejeita dois arquivos com conteudo identico dentro do mesmo plano antes de qualquer preflight/submissao.
- Protecao extra: `daily-run` agora aplica a mesma trava de data alvo do `preflight`; se a data for futura/passada, valida o plano, gera intel/plan-report e imprime `date_guard=skip_submit` sem chamar `submit_plan`, gerar plano adaptativo ou atualizar relatorios pos-submissao.
- Trava de deadline: `status`, `preflight`, `daily-run` e `submit-plan` agora exibem deadline/segundos restantes; `preflight` retorna `competition_closed` depois de 2026-07-16 11:59 UTC e `submit-plan` nao chama Kaggle se `competition_open=false`.
- Contingencia/reserva guardadas no comando unico: `preflight` e `daily-run` agora reconhecem `plans/YYYY-MM-DD-public-contingency.csv` entre primario e reserva; reserva continua exigindo `--allow-reserve`. Quando usa reserva, gera plan-report contra `v185_private_kw.csv` e imprime `next_plan_guard=reserve_plan` em vez de criar adaptativo em cima da contingencia.
- Novo preflight: `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD` mostra data UTC atual, relacao da data alvo, cota, proximo reset UTC/BRT, plano primario, contingencia publica, reserva, plano selecionado e `recommended_action` antes de qualquer envio; em 2026-07-01 12:51 UTC retornou `target_date_relation=future`, `contingency_exists=true` e `selected_plan=plans/2026-07-03-public-contingency.csv` para 2026-07-03.
- Guarda de cota no preflight canonico: quando chamado sem `--date` antes do reset e a cota do dia UTC ja esta `20/20`, retorna `recommended_action=wait_for_quota` em vez de sugerir criar plano para um dia ja consumido.
- Relatorio final melhorado: `reports/final-candidates.md`, `reports/final-selection.csv` e `reports/final-selection-audit.md` recomendam ate 20 finais com ancora publica, `v185_private_kw.csv`, anchors historicos suplementados quando a CLI da Kaggle trunca o historico, promocao explicita de ASSOC/DIFF near-best como hedge privado, reservas publicas controladas ate `0.00600` abaixo do melhor, filtro de volume para deixar mutacoes KEEP-only gigantes apenas em Top Public e auditoria de concentracao por condicao/coluna.
- Plano reserva pronto: `plans/2026-07-03-reserve.csv` (`v241-v260`) combina `v185_private_kw.csv` com mudancas public-neutras/tied. Usar apenas se o adaptativo `v221-v240` e a contingencia publica `v261-v280` nao forem escolhidos e houver risco real de perder quota.
- Testes locais: `.venv/bin/python -m unittest discover -s tests -v` passou com 97/97 testes, cobrindo a orquestracao, reset de cota, deadline guard, relatorio `intel`, leitura de topicos/comentarios do forum por API Kaggle direta, guarda de notebook publico novo/atualizado antes de submissao, sync dry-run de notebooks publicos novos/atualizados, auditoria de notebooks publicos, auditoria de deltas ICD do plano, interpretacao de impacto pos-score, sinais publicos escalados, scorecard de plano, readiness pre-reset, scorer offline do Train com rejeicao de no ICD desconhecido e granularidade minima, trava de data no `daily-run`, lock local contra execucoes simultaneas, ledger local anti-retry, parada limpa em erro de cota Kaggle, diagnostico de duplicatas de submissao, guarda contra plano incompleto, guarda de pos-relatorios sem atividade real ou retry parcial sem envio novo, fallback de reserva com permissao explicita, contingencias publicas `v261-v280`, `v321-v340`, `v361-v380` e `v401-v420`, prioridade de contingencia antes da reserva, gerador ASSOC/DIFF `v281-v300`, adaptativo pos-ASSOC/DIFF `v301-v320`, adaptativo pos-04/07 `v341-v360`, inferencia automatica da proxima versao do adaptativo, salto de faixas ja reservadas em `submissions/`, dedupe por conteudo ja submetido e intra-plano, preflight canonico com cota esgotada, adaptativo com preferencia por combos nao negativos, guarda contra plano primario sem combo publico nao negativo, slots privados/retry seguro, shortlist final 20/20 com CSV operacional, auditoria de concentracao final e promocao de hedges ASSOC/DIFF mesmo quando o volume de codigos e alto.

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
.venv/bin/python src/cohortx_ops.py preflight
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

Em automacao/cron, omitir `--date` e deixar o CLI usar a data UTC atual. Para auditoria manual de uma data especifica, manter `--date YYYY-MM-DD`. Antes da virada UTC, um comando datado para a data futura tambem fica seguro: ele retorna `date_guard=skip_submit` e `post_reports_guard=no_current_plan_activity` em vez de enviar a fila cedo ou atualizar relatorios pos-submissao.
O cron Codex executa esse caminho em uma janela de retry pos-reset (`00:20`, `01:20`, `02:20 UTC`) para reduzir risco de perder o dia por falha pontual de rede/Kaggle. Retry parcial sem envio novo tambem fica contido em `post_reports_guard=no_current_plan_activity`.

Expandido:

```bash
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-02
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-02.csv
.venv/bin/python src/audit_plan_deltas.py --plan plans/2026-07-02.csv --out reports/2026-07-02-code-deltas.md
.venv/bin/python src/cohortx_ops.py submit-plan plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py intel --date 2026-07-02
.venv/bin/python src/cohortx_ops.py review --date 2026-07-02
.venv/bin/python src/cohortx_ops.py signals --date 2026-07-02
.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-02.csv
.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-02.csv --out reports/2026-07-02-impact.md
.venv/bin/python src/cohortx_ops.py final-candidates
.venv/bin/python src/v221_240_adaptive_followups.py --prior-plan plans/2026-07-02.csv --out-plan plans/2026-07-03.csv
```

O adaptativo de 03/07 so deve rodar depois dos scores completos. Antes disso ele retorna `not_ready` e nao cria arquivo prematuro; quando rodar, `public nonnegative combo` tem prioridade sobre `negative fallback combo`.
Se nao houver nenhum combo publico nao negativo, ele tambem retorna `not_ready` por padrao para evitar transformar combos publicamente ruins em plano primario. Nesse cenario, preferir a contingencia publica ja pronta antes da reserva privada/neutra.

Plano publico de contingencia se `v221-v240` nao puder virar primario:

```bash
.venv/bin/python src/v261_280_public_contingency.py
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-03-public-contingency.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-03-public-contingency.csv --out reports/2026-07-03-public-contingency-plan.md
.venv/bin/python src/audit_plan_deltas.py --plan plans/2026-07-03-public-contingency.csv --out reports/2026-07-03-public-contingency-code-deltas.md
.venv/bin/python src/cohortx_ops.py daily-run --date 2026-07-03 --auto-next-plan
```

Plano reserva se `v221-v240` e `v261-v280` nao forem usados perto do reset seguinte:

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

Relatorios vivos: `reports/final-candidates.md` e `reports/final-selection.csv`. Regerar depois de cada dia com scores completos para atualizar a selecao recomendada de ate 20 finais, a watchlist e evitar promover probes que cairam no publico.

## Plano reserva 2026-07-03

- Arquivo: `plans/2026-07-03-reserve.csv`.
- Auditoria: `reports/2026-07-03-reserve-plan.md`.
- Gerador: `src/v241_260_private_reserve.py`.
- Uso: contingencia de quota. Priorizar `plans/2026-07-03.csv` adaptativo quando os scores de `v201-v220` existirem. Sem `--allow-reserve`, o preflight deve segurar a reserva com `recommended_action=hold_for_primary_or_rerun_adaptive`.
