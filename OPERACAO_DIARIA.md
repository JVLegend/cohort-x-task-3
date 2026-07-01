# Operacao Diaria — CohortX Task 3

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Objetivo

Enviar ate 20 submissoes por dia ate o fim da competicao, sempre com probes pequenos e informativos, evitando duplicatas e registrando o aprendizado no repo.

## Rotina de cada ciclo

1. Revalidar Kaggle:
   - `.venv/bin/python src/cohortx_ops.py status`
   - `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD`
   - `.venv/bin/kaggle competitions leaderboard -c cohort-x-task-3 -s`
2. Checar se existem notebooks/discussoes novas:
   - `.venv/bin/python src/cohortx_ops.py intel --date YYYY-MM-DD`
   - `.venv/bin/python src/sync_public_notebooks.py --dry-run`
   - `.venv/bin/python src/audit_public_notebooks.py`
   - se o intel apontar `New public notebooks > 0`, rodar `.venv/bin/python src/sync_public_notebooks.py`, diffar/auditar antes de qualquer submissao; o `daily-run` tambem bloqueia esse caso por padrao.
3. Ler `README.md`, `SUBMIT_QUEUE.md`, scripts recentes e `git status`.
4. Gerar ate 20 candidatos novos e nao duplicados.
5. Validar todos os CSVs:
   - 23 linhas.
   - colunas `Condition,KEEP,ASSOCIATION,DIFF`.
   - sem linhas vazias acidentais.
6. Gerar o relatorio de plano antes da submissao:
   - `.venv/bin/python src/cohortx_ops.py plan-report plans/YYYY-MM-DD.csv`
   - `.venv/bin/python src/audit_plan_deltas.py --plan plans/YYYY-MM-DD.csv --out reports/YYYY-MM-DD-code-deltas.md`
7. Submeter ate o limite diario.
8. Esperar todos ficarem `complete`.
9. Atualizar:
   - `reports/YYYY-MM-DD-intel.md` com `.venv/bin/python src/cohortx_ops.py intel --date YYYY-MM-DD`.
   - `reports/YYYY-MM-DD.md` com `.venv/bin/python src/cohortx_ops.py review --date YYYY-MM-DD`.
   - `reports/YYYY-MM-DD-signals.md` com `.venv/bin/python src/cohortx_ops.py signals --date YYYY-MM-DD`.
   - `reports/YYYY-MM-DD-scorecard.md` com `.venv/bin/python src/cohortx_ops.py plan-scorecard plans/YYYY-MM-DD.csv`.
   - `reports/YYYY-MM-DD-impact.md` com `.venv/bin/python src/interpret_plan_scores.py --plan plans/YYYY-MM-DD.csv --out reports/YYYY-MM-DD-impact.md`.
   - `reports/final-candidates.md` com `.venv/bin/python src/cohortx_ops.py final-candidates`.
   - `README.md` se o melhor score/insight mudou.
   - `SUBMIT_QUEUE.md` com score, leitura e plano seguinte.
   - `03_Resources/Kanban/kanban.json` no vault SuperJV quando houver mudanca de status relevante.
10. Se o lote anterior ja tiver scores completos e ainda nao houver plano para o proximo dia, gerar follow-ups adaptativos:
   - `.venv/bin/python src/v221_240_adaptive_followups.py --prior-plan plans/YYYY-MM-DD.csv --out-plan plans/YYYY-MM-DD_NEXT.csv`
   - `.venv/bin/python src/cohortx_ops.py validate-plan plans/YYYY-MM-DD_NEXT.csv`
11. Se o adaptativo ainda estiver `not_ready` perto de uma janela de quota e nao houver plano principal para o dia, preferir uma contingencia publica auditada antes da reserva:
   - `.venv/bin/python src/v261_280_public_contingency.py`
   - `.venv/bin/python src/cohortx_ops.py validate-plan plans/YYYY-MM-DD-public-contingency.csv`
   - `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD`
   - `.venv/bin/python src/cohortx_ops.py plan-report plans/YYYY-MM-DD-public-contingency.csv --out reports/YYYY-MM-DD-public-contingency-plan.md`
   - `.venv/bin/python src/audit_plan_deltas.py --plan plans/YYYY-MM-DD-public-contingency.csv --out reports/YYYY-MM-DD-public-contingency-code-deltas.md`
   - `.venv/bin/python src/cohortx_ops.py daily-run --date YYYY-MM-DD --auto-next-plan`
12. Usar o plano reserva somente apos auditoria manual se o adaptativo e a contingencia publica nao forem escolhidos e houver risco de perder quota:
   - `.venv/bin/python src/v241_260_private_reserve.py`
   - `.venv/bin/python src/cohortx_ops.py validate-plan plans/YYYY-MM-DD-reserve.csv`
   - `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD --reserve-plan plans/YYYY-MM-DD-reserve.csv`
   - `.venv/bin/python src/cohortx_ops.py plan-report plans/YYYY-MM-DD-reserve.csv --anchor submissions/v185_private_kw.csv --out reports/YYYY-MM-DD-reserve-plan.md`
   - `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD --reserve-plan plans/YYYY-MM-DD-reserve.csv --allow-reserve`
   - `.venv/bin/python src/cohortx_ops.py daily-run --date YYYY-MM-DD --reserve-plan plans/YYYY-MM-DD-reserve.csv --allow-reserve`

## Regras estrategicas

- A solucao final deve ser reproduzivel offline.
- O forum permite modelos Hugging Face e dados Creative Commons/public domain.
- Evitar dependencia de API online/proprietaria para processamento final.
- Host citou servidor com 15 GB RAM e tempo de renderizacao razoavel.
- `ASSOCIATION` e `DIFF` ficam `Not Applicable` salvo probe muito controlado.

## Estado de referencia

- Best publico: `0.42453`.
- Base confiavel: `submissions/v178_FINAL.csv`.
- Hedge privado: `submissions/v185_private_kw.csv`.
- Public movers confirmados: COPD e Enlarged Mediastinum.
- Private/invisiveis no publico: CKD, UTI, Diabetes, Pneumonia e varias medias neutras.

## Proxima frente

Para 2026-07-02, usar as 20 balas em torno de:

- COPD: remocoes/adicoes por familias ICD dentro da base.
- Enlarged Mediastinum: remocoes/adicoes por familias ICD dentro da base.
- 2-4 hedges privados apenas se forem diferentes de `v185`.

O alvo nao e fazer scores bonitos em todos os probes; e descobrir uma melhoria que supere `0.42453` ou uma combinacao privada que mantenha o publico.

## Plano pronto de 2026-07-02

Executar apos reset UTC:

```bash
.venv/bin/python src/cohortx_ops.py preflight
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

Para automacao/cron, preferir omitir `--date`: o CLI usa a data UTC atual e evita erro humano de rodar com uma data passada/futura. Se for necessario auditar uma data especifica manualmente, `--date YYYY-MM-DD` continua disponivel.

Se esse `daily-run` for executado antes de 2026-07-02 em UTC com `--date 2026-07-02`, ele valida o plano e gera `intel`/plan-report, mas imprime `target_date_relation=future`, `date_guard=skip_submit` e `post_reports_guard=no_current_plan_activity` sem chamar a submissao nem atualizar review/signals/scorecard/final-candidates.

A automacao Codex ativa roda em tres tentativas pos-reset: `00:20`, `01:20` e `02:20 UTC`. Isso e intencional: se a primeira tentativa falhar por rede/Kaggle/sessao, as proximas tentam novamente; se a primeira ja submeteu a cota, as proximas param pelo preflight/dedupe/plano ja submetido.

Se um retry encontrar apenas parte do plano no historico Kaggle e nao enviar nada novo, ele segura os relatorios pos-submissao com `post_reports_guard=no_current_plan_activity`; `review`, `signals`, `plan-scorecard`, `final-candidates` e o proximo plano so rodam depois de envio novo ou plano completo.

Equivalente expandido:

```bash
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-02
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py submit-plan plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py intel --date 2026-07-02
.venv/bin/python src/cohortx_ops.py review --date 2026-07-02
.venv/bin/python src/cohortx_ops.py signals --date 2026-07-02
.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-02.csv
.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-02.csv --out reports/2026-07-02-impact.md
.venv/bin/python src/cohortx_ops.py final-candidates
```

O script:

- conta submissoes do dia UTC;
- `status` e `preflight` mostram o proximo reset de cota em UTC/BRT, `seconds_until_reset`, deadline UTC/BRT, `seconds_until_deadline` e `competition_open`;
- `preflight` valida plano primario, contingencia publica e reserva, calcula cota restante, bloqueia data futura/passada e mostra `recommended_action` antes de qualquer envio;
- com data UTC atual e cota ja esgotada, `preflight` retorna `wait_for_quota` mesmo se ainda nao existir plano para esse mesmo dia, evitando criar um plano inutil para uma janela ja consumida;
- `preflight` retorna `competition_closed` quando o deadline passou e `target_after_deadline` para datas apos 2026-07-16;
- `intel` gera `reports/YYYY-MM-DD-intel.md` com notebooks publicos recentes via Kaggle CSV, top do leaderboard, status da pagina de discussoes e ultimas submissoes JV;
- `intel` compara as refs do Kaggle com `external_notebooks/*/kernel-metadata.json` e destaca `New public notebooks`; se aparecer ref nova, baixar/diffar antes de submeter ou gerar o proximo plano;
- `sync_public_notebooks.py` baixa refs publicas novas via `kaggle kernels pull -m` para `external_notebooks/` sem executar notebooks, e regenera `reports/public-notebook-audit.md`;
- `audit_public_notebooks.py` gera `reports/public-notebook-audit.md` a partir dos notebooks baixados, destacando modelos, top-k/thresholds, uso de TF-IDF/BM25 e risco de preencher `ASSOCIATION`/`DIFF`;
- `audit_plan_deltas.py` gera `reports/YYYY-MM-DD-code-deltas.md`, listando os codigos ICD e titulos exatos adicionados/removidos por cada item do plano para acelerar a interpretacao dos scores;
- `interpret_plan_scores.py` gera `reports/YYYY-MM-DD-impact.md`, cruzando score publico, delta vs ancora e deltas ICD para transformar cada probe em acao: promover, podar, manter como hedge ou evitar falso positivo;
- `daily-run` encadeia status, intel pre-submissao, preflight, validacao, plan-report, submissao, review, signals, plan-scorecard e final-candidates, mas tambem bloqueia submissao quando a data alvo for futura/passada, o deadline ja tiver passado ou o intel detectar notebook publico novo ainda nao baixado/auditado;
- `--allow-new-notebooks` existe apenas como override manual apos baixar/diffar/auditar a ref nova; nao usar na automacao de rotina;
- `daily-run` so roda os relatorios pos-submissao (`review`, `signals`, `plan-scorecard`, `final-candidates`) quando houve envio nesta execucao ou o plano completo ja aparece contabilizado no historico Kaggle; caso contrario imprime `post_reports_guard=no_current_plan_activity`;
- `submit-plan` tambem checa deadline antes de chamar Kaggle e imprime `competition_closed; no submissions sent` se a competicao estiver fechada;
- `--auto-next-plan` tenta gerar `plans/YYYY-MM-DD+1.csv` somente quando todos os arquivos do plano anterior ja constarem no historico Kaggle; se quota/erro deixar o plano incompleto, imprime `next_plan_guard=prior_plan_incomplete`; se `--start-version` nao for informado, infere a proxima versao pelo maior `vNNN` do plano anterior;
- respeita o limite `20/dia`;
- pula arquivos ja submetidos;
- tambem pula CSV novo cujo conteudo seja identico ao de uma submissao local ja presente no historico Kaggle;
- `validate-plan` rejeita duplicatas internas de conteudo no proprio plano, mesmo quando os arquivos tem nomes diferentes;
- so seleciona plano reserva quando `--allow-reserve` for passado; sem essa permissao explicita, imprime `reserve_guard=requires_allow_reserve`;
- seleciona `plans/YYYY-MM-DD-public-contingency.csv` automaticamente quando o primario nao existe e a contingencia existe, antes de considerar reserva;
- quando seleciona reserva, gera plan-report contra `v185_private_kw.csv` e nao cria plano adaptativo em cima da contingencia;
- valida linhas/colunas dos CSVs;
- gera `reports/YYYY-MM-DD-plan.md` para auditar mudancas planejadas antes do envio;
- espera scores completarem quando submete;
- inclui as notas de `plans/YYYY-MM-DD.csv` no relatorio diario quando o plano existir;
- compara cada submissao local contra `v178_FINAL.csv` para extrair sinais publicos por condicao, incluindo `scaled_x23` e ranking de sensibilidade publica.
- `plan-scorecard` cruza o plano com o historico Kaggle e classifica cada item como `improved`, `tied`, `worse` ou `missing_score` vs a ancora.
- `final-candidates` tambem pode ser executado isoladamente para consolidar a shortlist de selecao final: recomenda ate 20 arquivos, preserva uma ancora publica/inalterada, inclui `v185_private_kw.csv` como hedge privado e filtra mutacoes public-neutral grandes demais da selecao recomendada.

## Follow-up adaptativo

Depois que `v201-v220` forem enviados e pontuados, rodar:

```bash
.venv/bin/python src/v221_240_adaptive_followups.py --prior-plan plans/2026-07-02.csv --out-plan plans/2026-07-03.csv
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-03.csv
.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-03.csv
```

Esse gerador ranqueia as variantes de COPD e Enlarged Mediastinum por delta vs `v178_FINAL`, cria combinacoes entre os sinais que empatam/superam a ancora e duplica parte delas sobre `v185_private_kw.csv` para preservar hedge privado. Variantes com delta negativo so entram como fallback rotulado se faltarem combinacoes nao negativas suficientes.

Politica atual do adaptativo:

- ordenar combos por soma de delta publico vs `v178_FINAL`, nao por score absoluto;
- preencher primeiro 16 combos publicos, priorizando `public nonnegative combo`;
- reservar 4 slots para os melhores combos aplicados sobre `v185_private_kw.csv`;
- usar standalones e `negative fallback combo` apenas para completar 20 candidatos unicos quando ja existir ao menos um combo publico nao negativo, mas nao houver volume suficiente de combos bons.
- em reexecucoes, pular numeros de versao `vNNN` ja existentes e recusar sobrescrever CSV existente.
- por padrao, recusar criar plano primario quando nao existir ao menos um combo COPD+Mediastinum com delta publico >= 0 em ambos os lados; nesse caso preferir `plans/2026-07-03-public-contingency.csv` e deixar `plans/2026-07-03-reserve.csv` apenas para contingencia final de quota.
- `--allow-negative-fallback` existe como override manual, mas nao deve ser usado pela automacao diaria.

## Plano publico de contingencia

Ja existe uma contingencia publica para 2026-07-03:

```bash
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-03-public-contingency.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-03-public-contingency.csv --out reports/2026-07-03-public-contingency-plan.md
.venv/bin/python src/audit_plan_deltas.py --plan plans/2026-07-03-public-contingency.csv --out reports/2026-07-03-public-contingency-code-deltas.md
```

Use `plans/2026-07-03-public-contingency.csv` apenas se o adaptativo `plans/2026-07-03.csv` nao puder ser gerado com combo publico nao negativo. Ele contem `v261-v280`: ablacões finas de COPD core, pequenas adicoes de bronchiectasis, ablacões de mediastino e adicoes thymus/linfonodos intratoracicos ainda nao testadas.
No preflight atual, se o primario `plans/2026-07-03.csv` nao existir, essa contingencia aparece como `selected_plan=plans/2026-07-03-public-contingency.csv` e, quando a data alvo for atual, deve retornar `recommended_action=submit_public_contingency`.

Comando seguro:

```bash
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03
.venv/bin/python src/cohortx_ops.py daily-run --date 2026-07-03 --auto-next-plan
```

## Plano reserva

Ja existe uma reserva para 2026-07-03:

```bash
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-03-reserve.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03 --reserve-plan plans/2026-07-03-reserve.csv
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-03-reserve.csv --anchor submissions/v185_private_kw.csv --out reports/2026-07-03-reserve-plan.md
```

Use `plans/2026-07-03-reserve.csv` apenas se `plans/2026-07-03.csv` adaptativo e `plans/2026-07-03-public-contingency.csv` nao forem escolhidos a tempo. Para submeter reserva, repetir o preflight com `--allow-reserve`; sem essa flag ele deve retornar `recommended_action=hold_for_primary_or_rerun_adaptive`. Ele contem `v241-v260`: `v185_private_kw.csv` combinado com mudancas que foram public-neutral/tied em submissões anteriores.

Comando seguro de contingencia:

```bash
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-03-reserve.csv --anchor submissions/v185_private_kw.csv --out reports/2026-07-03-reserve-plan.md
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03 --reserve-plan plans/2026-07-03-reserve.csv --allow-reserve
.venv/bin/python src/cohortx_ops.py daily-run --date 2026-07-03 --reserve-plan plans/2026-07-03-reserve.csv --allow-reserve
```

## Testes locais

Antes de alterar a orquestracao ou os relatórios operacionais:

```bash
.venv/bin/python -m unittest discover -s tests -v
```

A suite cobre diffs de CSV, relatorio de plano, auditoria de deltas ICD do plano, interpretacao de impacto pos-score, relatorio de inteligencia, guarda de notebook publico novo antes de submissao, sync dry-run de notebooks publicos novos, auditoria dos notebooks publicos, sinais publicos escalados, scorecard de plano, shortlist final ate 20 selecionaveis, preflight, trava de data alvo no preflight e no `daily-run`, guarda de pos-relatorios sem atividade de plano ou retry parcial sem envio novo, deadline guard no preflight/submit-plan, reset de cota, plano reserva com permissao explicita, contingencia publica `v261-v280` e sua prioridade antes da reserva, caminho do proximo plano, inferencia automatica da proxima versao do adaptativo, guarda contra plano anterior incompleto, dedupe por conteudo ja submetido, dedupe interno de plano, reserva de slots privados, preferencia adaptativa por combos nao negativos, retry seguro no adaptativo, `daily-run` com/sem reports e falha segura de next-plan antes dos scores.
