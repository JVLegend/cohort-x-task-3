# Operacao Diaria — CohortX Task 3

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Objetivo

Enviar ate 20 submissoes por dia ate o fim da competicao, sempre com probes pequenos e informativos, evitando duplicatas e registrando o aprendizado no repo.

## Rotina de cada ciclo

1. Revalidar Kaggle:
   - `.venv/bin/python src/cohortx_ops.py status`
   - `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD`
   - `.venv/bin/python src/cohortx_ops.py readiness --date YYYY-MM-DD`
   - `.venv/bin/kaggle competitions leaderboard -c cohort-x-task-3 -s`
2. Checar se existem notebooks/discussoes novas:
   - `.venv/bin/python src/cohortx_ops.py intel --date YYYY-MM-DD`
   - `.venv/bin/python src/sync_public_notebooks.py --dry-run`
   - `.venv/bin/python src/audit_public_notebooks.py`
   - se o intel apontar `New public notebooks > 0` ou `Updated public notebooks > 0`, rodar `.venv/bin/python src/sync_public_notebooks.py`, diffar/auditar antes de qualquer submissao; o `daily-run` tambem bloqueia esse caso por padrao.
3. Ler `README.md`, `SUBMIT_QUEUE.md`, scripts recentes e `git status`.
4. Gerar ate 20 candidatos novos e nao duplicados.
5. Validar todos os CSVs:
   - 23 linhas.
   - colunas `Condition,KEEP,ASSOCIATION,DIFF`.
   - sem linhas vazias acidentais.
6. Gerar o relatorio de plano antes da submissao:
   - `.venv/bin/python src/cohortx_ops.py plan-report plans/YYYY-MM-DD.csv`
   - `.venv/bin/python src/cohortx_ops.py plan-strategy plans/YYYY-MM-DD.csv`
   - `.venv/bin/python src/cohortx_ops.py plan-decision plans/YYYY-MM-DD.csv`
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
   - `reports/final-selection-audit.md` e atualizado junto com `final-candidates`; use `.venv/bin/python src/cohortx_ops.py final-audit` se precisar regenerar apenas a auditoria.
   - `reports/final-diversity.md` tambem e atualizado junto com `final-candidates`; use `.venv/bin/python src/cohortx_ops.py final-diversity` se precisar regenerar apenas a watchlist de diversidade.
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
   - `.venv/bin/python src/cohortx_ops.py plan-strategy plans/YYYY-MM-DD-public-contingency.csv --out reports/YYYY-MM-DD-public-contingency-strategy.md`
   - `.venv/bin/python src/audit_plan_deltas.py --plan plans/YYYY-MM-DD-public-contingency.csv --out reports/YYYY-MM-DD-public-contingency-code-deltas.md`
   - `.venv/bin/python src/cohortx_ops.py daily-run --date YYYY-MM-DD --auto-next-plan`
12. Usar o plano reserva somente apos auditoria manual se o adaptativo e a contingencia publica nao forem escolhidos e houver risco de perder quota:
   - `.venv/bin/python src/v241_260_private_reserve.py`
   - `.venv/bin/python src/cohortx_ops.py validate-plan plans/YYYY-MM-DD-reserve.csv`
   - `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD --reserve-plan plans/YYYY-MM-DD-reserve.csv`
   - `.venv/bin/python src/cohortx_ops.py plan-report plans/YYYY-MM-DD-reserve.csv --anchor submissions/v185_private_kw.csv --out reports/YYYY-MM-DD-reserve-plan.md`
   - `.venv/bin/python src/cohortx_ops.py plan-strategy plans/YYYY-MM-DD-reserve.csv --anchor submissions/v185_private_kw.csv --out reports/YYYY-MM-DD-reserve-strategy.md`
   - `.venv/bin/python src/cohortx_ops.py preflight --date YYYY-MM-DD --reserve-plan plans/YYYY-MM-DD-reserve.csv --allow-reserve`
   - `.venv/bin/python src/cohortx_ops.py daily-run --date YYYY-MM-DD --reserve-plan plans/YYYY-MM-DD-reserve.csv --allow-reserve`

## Regras estrategicas

- A solucao final deve ser reproduzivel offline.
- O forum permite modelos Hugging Face e dados Creative Commons/public domain.
- Evitar dependencia de API online/proprietaria para processamento final.
- Host citou servidor com 15 GB RAM e tempo de renderizacao razoavel.
- ~~`ASSOCIATION` e `DIFF` ficam `Not Applicable` salvo probe muito controlado.~~
  **REVISTO 2026-07-01 (ver `ESTRATEGIA.md`):** o gold POPULA ASSOC/DIFF (aba Train).
  Popular ASSOC/DIFF com curadoria clinica nas condicoes invisiveis no publico e agora a
  frente prioritaria. Manter `Not Applicable` apenas em COPD e Enlarged Mediastinum
  (public movers com gold provavelmente vazio) ate evidencia em contrario.

## Estado de referencia

- Best publico: `0.43156` (`submissions/v301_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_broad_assoc_v185keep.csv` e `submissions/v302_copd_no_j20_j45_j81_j82_j93_j95_med_add_thymus_nodes_assocdiff_highconf_assoc_v185keep.csv`).
- Bases confiaveis anteriores: `submissions/v209_copd_no_acute_bronch_asthma.csv` e
  `submissions/v178_FINAL.csv`.
- Hedge privado: `submissions/v185_private_kw.csv`.
- Public movers confirmados: COPD e Enlarged Mediastinum.
- Private/invisiveis no publico: CKD, UTI, Diabetes, Pneumonia e varias medias neutras.

## Proxima frente

Depois do envio completo de 2026-07-04, `v301`-`v320` pontuaram e a cota UTC esta
consumida (`20/20`). Antes do proximo reset, nao forcar submissao manual; o preflight
atual deve retornar `primary_already_submitted`/sem cota restante.
`src/cohortx_ops.py` agora usa `.cohortx_locks/submission.lock` em `daily-run` e
`submit-plan`, e refresca cota/filenames/conteudo antes de cada upload em `submit_plan`,
para interromper o loop se o historico remoto atingir `20/20` durante a execucao.

Para a proxima janela, usar como primario `plans/2026-07-05.csv`:

- `v341`-`v360`: follow-ups pos-04/07 sobre os melhores composites (`v301`/`v302` e
  `v303`/`v304`), isolando manter/remover thymus/nodes em mediastino, fatias privadas de
  `v185` e buckets ASSOC/DIFF seletivos.
- `reports/2026-07-05-strategy.md` audita a cobertura antes do envio: 20/20 itens,
  source publico maximo `0.43156`, `med=keep` 13 slots, `med=drop` 7, quatro buckets de
  private KEEP e cinco buckets ASSOC/DIFF. Se houver falha parcial de rede/Kaggle,
  preservar a ordem do plano.

Se `plans/2026-07-05.csv` nao estiver utilizavel no reset, usar como paraquedas
`plans/2026-07-05-public-contingency.csv` (`v361`-`v380`) antes de considerar reserva.

Para o reset de 2026-07-06, preservar `v381`-`v400` para o adaptativo primario pos-score
de 05/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-06-public-contingency.csv` (`v401`-`v420`), que combina `v296`, mediastino
`v300`, ASSOC/DIFF near-best e fatias parciais de `v185`.

Para o reset de 2026-07-07, preservar `v421`-`v440` para o adaptativo primario pos-score
de 06/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-07-public-contingency.csv` (`v441`-`v460`), que recombina `v293`-`v295`
com mediastino `v300` e ASSOC/DIFF public-neutral/positivo sem novas fatias privadas.

Para o reset de 2026-07-08, preservar `v461`-`v480` para o adaptativo primario pos-score
de 07/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-08-public-contingency.csv` (`v481`-`v500`), que testa KEEP em condicoes
public-neutral sobre `v296`, com e sem mediastino `v300`.

Para o reset de 2026-07-09, preservar `v501`-`v520` para o adaptativo primario pos-score
de 08/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-09-public-contingency.csv` (`v521`-`v540`), que isola ASSOC-only por
condicao sobre `v296` para decompor o ganho de `v283`/`v286` sem misturar DIFF.

Para o reset de 2026-07-10, preservar `v541`-`v560` para o adaptativo primario pos-score
de 09/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-10-public-contingency.csv` (`v561`-`v580`), que isola DIFF-only por
condicao sobre `v296` para confirmar se algum DIFF individual presta apesar da queda do
DIFF amplo.

Para o reset de 2026-07-11, preservar `v581`-`v600` para o adaptativo primario pos-score
de 10/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-11-public-contingency.csv` (`v601`-`v620`), que testa podas KEEP em
condicoes privadas sobre `v296`, sem tocar nos movers publicos COPD/Mediastinum.

Para o reset de 2026-07-12, preservar `v621`-`v640` para o adaptativo primario pos-score
de 11/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-12-public-contingency.csv` (`v641`-`v660`), que combina poda KEEP +
ASSOC-only na mesma condicao sobre `v296`, mantendo DIFF vazio e sem tocar nos movers
publicos COPD/Mediastinum.

Para o reset de 2026-07-13, preservar `v661`-`v680` para o adaptativo primario pos-score
de 12/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-13-public-contingency.csv` (`v681`-`v700`), que combina poda KEEP +
DIFF-only na mesma condicao sobre `v296`. Este e fallback de maior risco porque DIFF
amplo derrubou publico.

Para o reset de 2026-07-14, preservar `v701`-`v720` para o adaptativo primario pos-score
de 13/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-14-public-contingency.csv` (`v721`-`v740`), que combina poda KEEP +
ASSOC+DIFF na mesma condicao sobre `v296`. Este e o fallback mais agressivo da familia
prune+bucket e deve ficar atras do adaptativo.

Para o reset de 2026-07-15, preservar `v741`-`v760` para o adaptativo primario pos-score
de 14/07. Se esse primario nao existir perto da janela, usar
`plans/2026-07-15-public-contingency.csv` (`v761`-`v780`), que cria carteiras
multi-condicao de podas KEEP privadas sobre `v296`, mantendo ASSOC/DIFF vazios. E um
hedge finalista privado, nao uma tentativa de otimizar o public LB.

Para o reset final de 2026-07-16, preservar `v781`-`v800` para o adaptativo primario
pos-score de 15/07. Se esse primario nao existir perto da janela antes do deadline
11:59 UTC, usar `plans/2026-07-16-public-contingency.csv` (`v801`-`v820`), que combina
`v296`, mediastino `v300`, fatias `v185`, overlays zero/add public-neutral, podas KEEP
e ASSOC-only seletivo, mantendo DIFF vazio.

O melhor composite publico atual e `v301`/`v302` (`0.43156`), mas a base KEEP dele segue
sendo remover `J20+J45+J81/J82+J93/J95` de COPD (`v296`). Remover `J96`, reduzir COPD ao
core `J41/J42/J43/J44`, remover mediastino `J98` ou reintroduzir `J81/J82`/`J93/J95`
derruba forte; evitar essas direcoes em candidatos publicos.

## Plano pronto de 2026-07-05

Executar apos reset UTC:

```bash
.venv/bin/python src/cohortx_ops.py preflight
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

Para automacao/cron, preferir omitir `--date`: o CLI usa a data UTC atual e evita erro humano de rodar com uma data passada/futura. Se for necessario auditar uma data especifica manualmente, `--date YYYY-MM-DD` continua disponivel.

Se esse `daily-run` for executado antes de 2026-07-05 em UTC com `--date 2026-07-05`, ele valida o plano e gera `intel`/plan-report, mas imprime `target_date_relation=future`, `date_guard=skip_submit` e `post_reports_guard=no_current_plan_activity` sem chamar a submissao nem atualizar review/signals/scorecard/final-candidates.

A automacao Codex ativa roda em tres tentativas pos-reset: `00:20`, `01:20` e `02:20 UTC`. Isso e intencional: se a primeira tentativa falhar por rede/Kaggle/sessao, as proximas tentam novamente; se a primeira ja submeteu a cota, as proximas param pelo preflight/dedupe/plano ja submetido.

Se um retry encontrar apenas parte do plano no historico Kaggle e nao enviar nada novo, ele segura os relatorios pos-submissao com `post_reports_guard=no_current_plan_activity`; `review`, `signals`, `plan-scorecard`, `final-candidates` e o proximo plano so rodam depois de envio novo ou plano completo.

Equivalente historico do plano primario de 2026-07-04:

```bash
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-04.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-04
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-04.csv --anchor submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv
.venv/bin/python src/cohortx_ops.py submit-plan plans/2026-07-04.csv
.venv/bin/python src/cohortx_ops.py intel --date 2026-07-04
.venv/bin/python src/cohortx_ops.py review --date 2026-07-04
.venv/bin/python src/cohortx_ops.py signals --date 2026-07-04 --anchor submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv
.venv/bin/python src/cohortx_ops.py plan-scorecard plans/2026-07-04.csv --anchor submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv
.venv/bin/python src/interpret_plan_scores.py --plan plans/2026-07-04.csv --anchor submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv --out reports/2026-07-04-impact.md
.venv/bin/python src/cohortx_ops.py final-candidates
```

Equivalente expandido para o proximo plano primario:

```bash
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-05.csv
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-05
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-05.csv
.venv/bin/python src/cohortx_ops.py plan-strategy plans/2026-07-05.csv
.venv/bin/python src/cohortx_ops.py plan-decision plans/2026-07-05.csv
.venv/bin/python src/audit_plan_deltas.py --plan plans/2026-07-05.csv --out reports/2026-07-05-code-deltas.md
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

O script:

- conta submissoes do dia UTC;
- `status` e `preflight` mostram o proximo reset de cota em UTC/BRT, `seconds_until_reset`, deadline UTC/BRT, `seconds_until_deadline` e `competition_open`;
- `preflight` valida plano primario, contingencia publica e reserva, calcula cota restante, bloqueia data futura/passada e mostra `recommended_action` antes de qualquer envio;
- quando a data UTC atual ja esta com cota `20/20`, `preflight` tambem mostra `next_reset_*` se existir plano pronto para o proximo reset, incluindo `next_reset_selected_plan` e `next_reset_recommended_action`;
- `readiness` gera `reports/YYYY-MM-DD-readiness.md`, consolidando `preflight`, guarda de notebooks publicos novos/atualizados, validade do plano selecionado, matriz de decisao, auto-next do dia seguinte, shortlist final 20/20, comando canonico de reset e regras de parada pre-submit em gates de pronto/bloqueado antes do reset; o bloco Raw Preflight omite `seconds_until_*` para evitar diff volatil em checagens repetidas;
- `plan-decision` gera `reports/YYYY-MM-DD-decision.md`, com comparacoes pareadas para interpretar scores por eixo (`med`, `private_keep`, `assoc`, `source`) antes de gerar o proximo plano; o `daily-run` tambem gera esse relatorio automaticamente para o plano selecionado e para planos adaptativos novos;
- a cota operacional usa as linhas brutas do historico Kaggle, porque o servidor pode contar
  arquivos repetidos contra o limite diario; para diagnostico, `preflight` tambem mostra
  `unique_submission_events_today`, `duplicate_submission_rows_today` e
  `local_ledger_submissions_today`;
- com data UTC atual e cota ja esgotada, `preflight` retorna `wait_for_quota` mesmo se ainda nao existir plano para esse mesmo dia, evitando criar um plano inutil para uma janela ja consumida;
- `preflight` retorna `competition_closed` quando o deadline passou e `target_after_deadline` para datas apos 2026-07-16;
- `intel` gera `reports/YYYY-MM-DD-intel.md` com notebooks publicos recentes via Kaggle CSV, top do leaderboard, topicos/comentarios do forum via API Kaggle direta, notas de regras externas e ultimas submissoes JV;
- `intel` compara as refs do Kaggle com `external_notebooks/*/kernel-metadata.json` e destaca `New public notebooks`; se aparecer ref nova, baixar/diffar antes de submeter ou gerar o proximo plano;
- `sync_public_notebooks.py` mostra `pending_public_notebooks`, `new_public_notebooks` e `updated_public_notebooks`; quando nao esta em dry-run, baixa refs publicas novas ou atualizadas via `kaggle kernels pull -m` para `external_notebooks/` sem executar notebooks, atualiza `external_notebooks/public_notebook_manifest.json` e regenera `reports/public-notebook-audit.md`;
- `audit_public_notebooks.py` gera `reports/public-notebook-audit.md` a partir dos notebooks baixados, destacando modelos, top-k/thresholds, uso de TF-IDF/BM25 e risco de preencher `ASSOCIATION`/`DIFF`;
- `audit_plan_deltas.py` gera `reports/YYYY-MM-DD-code-deltas.md`, listando os codigos ICD e titulos exatos adicionados/removidos por cada item do plano para acelerar a interpretacao dos scores; quando `--anchor` nao e informado, usa a mesma ancora inferida por plano do `plan-report`;
- `plan-strategy` gera `reports/YYYY-MM-DD-strategy.md`, auditando a cobertura de eixos do plano antes do envio: source score, ordem, med=keep/drop, buckets private_keep e buckets ASSOC/DIFF; o `daily-run` tambem gera esse relatorio automaticamente para o plano selecionado e para planos adaptativos novos;
- `interpret_plan_scores.py` gera `reports/YYYY-MM-DD-impact.md`, cruzando score publico, delta vs ancora e deltas ICD para transformar cada probe em acao: promover, podar, manter como hedge ou evitar falso positivo;
- `daily-run` encadeia status, intel pre-submissao, preflight, validacao, plan-report, plan-strategy, plan-decision, deltas de plano, submissao, review, signals, plan-scorecard e final-candidates, mas tambem bloqueia submissao quando a data alvo for futura/passada, o deadline ja tiver passado ou o intel detectar notebook publico novo/atualizado ainda nao baixado/auditado;
- `--allow-new-notebooks` existe apenas como override manual apos baixar/diffar/auditar a ref nova; nao usar na automacao de rotina;
- `daily-run` so roda os relatorios pos-submissao (`review`, `signals`, `plan-scorecard`, `impact`, `final-candidates`) e o auto-next quando o plano completo aparece contabilizado no historico Kaggle e todos os itens do plano ja tem `publicScore` por filename ou por conteudo equivalente ja pontuado; se os arquivos foram aceitos mas os scores ainda faltam, imprime `score_guard=waiting_for_scores` e segura os relatorios com `post_reports_guard=no_current_plan_activity`;
- `submit-plan` tambem checa deadline antes de chamar Kaggle e imprime `competition_closed; no submissions sent` se a competicao estiver fechada;
- `--auto-next-plan` tenta gerar `plans/YYYY-MM-DD+1.csv` somente quando todos os arquivos do plano anterior ja constarem no historico Kaggle; se quota/erro deixar o plano incompleto, imprime `next_plan_guard=prior_plan_incomplete`; se `--start-version` nao for informado, infere a proxima versao pelo maior `vNNN` do plano anterior e pula faixas ja existentes em `submissions/` (ex.: depois de `v301-v320`, usar `v341+` para preservar a contingencia `v321-v340`); planos `v301-v320` e planos modernos `v341+` usam `src/v341_360_post_july4_followups.py` com anchor `v296`, planos `v281-v300` com `assocdiff` usam `src/v301_320_post_assocdiff_followups.py` com anchor `v209`, e os demais usam `src/v221_240_adaptive_followups.py`;
- se o adaptativo de 2026-07-05 nao existir, a contingencia publica `plans/2026-07-05-public-contingency.csv` usa `v361-v380` para nao ocupar `v341-v360`, que ficam reservadas para o primario pos-score de 04/07; para 2026-07-06, a contingencia `plans/2026-07-06-public-contingency.csv` usa `v401-v420` para preservar `v381-v400`; para 2026-07-07, a contingencia `plans/2026-07-07-public-contingency.csv` usa `v441-v460` para preservar `v421-v440`; para 2026-07-08, a contingencia `plans/2026-07-08-public-contingency.csv` usa `v481-v500` para preservar `v461-v480`; para 2026-07-09, a contingencia `plans/2026-07-09-public-contingency.csv` usa `v521-v540` para preservar `v501-v520`; para 2026-07-10, a contingencia `plans/2026-07-10-public-contingency.csv` usa `v561-v580` para preservar `v541-v560`; para 2026-07-11, a contingencia `plans/2026-07-11-public-contingency.csv` usa `v601-v620` para preservar `v581-v600`; para 2026-07-12, a contingencia `plans/2026-07-12-public-contingency.csv` usa `v641-v660` para preservar `v621-v640`; para 2026-07-13, a contingencia `plans/2026-07-13-public-contingency.csv` usa `v681-v700` para preservar `v661-v680`; para 2026-07-14, a contingencia `plans/2026-07-14-public-contingency.csv` usa `v721-v740` para preservar `v701-v720`; para 2026-07-15, a contingencia `plans/2026-07-15-public-contingency.csv` usa `v761-v780` para preservar `v741-v760`; para 2026-07-16, a contingencia `plans/2026-07-16-public-contingency.csv` usa `v801-v820` para preservar `v781-v800`;
- respeita o limite `20/dia`;
- pula arquivos ja submetidos;
- pula arquivos registrados em `.cohortx_locks/submission-ledger-YYYY-MM-DD.json`, criado
  apos um upload local retornar sucesso, para evitar reenvio em retries quando a listagem da
  Kaggle ainda nao refletiu a submissao;
- se a Kaggle rejeitar upload com `daily Submission allowance (20)`, imprime
  `kaggle_quota_error=true`, trata a cota como acabada e para sem traceback;
- tambem pula CSV novo cujo conteudo seja identico ao de uma submissao local ja presente no historico Kaggle;
- `validate-plan` rejeita duplicatas internas de conteudo no proprio plano, mesmo quando os arquivos tem nomes diferentes;
- so seleciona plano reserva quando `--allow-reserve` for passado; sem essa permissao explicita, imprime `reserve_guard=requires_allow_reserve`;
- seleciona `plans/YYYY-MM-DD-public-contingency.csv` automaticamente quando o primario nao existe e a contingencia existe, antes de considerar reserva;
- quando seleciona reserva, gera plan-report contra `v185_private_kw.csv` e nao cria plano adaptativo em cima da contingencia;
- valida linhas/colunas dos CSVs;
- gera `reports/YYYY-MM-DD-plan.md` para auditar mudancas planejadas antes do envio;
- gera `reports/YYYY-MM-DD-strategy.md` para auditar se as 20 submissões cobrem os eixos estrategicos esperados antes do envio;
- espera scores completarem quando submete;
- inclui as notas de `plans/YYYY-MM-DD.csv` no relatorio diario quando o plano existir;
- compara cada submissao local contra `v178_FINAL.csv` para extrair sinais publicos por condicao, incluindo `scaled_x23` e ranking de sensibilidade publica.
- `plan-scorecard` cruza o plano com o historico Kaggle e classifica cada item como `improved`, `tied`, `worse` ou `missing_score` vs a ancora.
- `final-candidates` tambem pode ser executado isoladamente para consolidar a shortlist de selecao final: recomenda ate 20 arquivos em `reports/final-candidates.md`, escreve o espelho operacional `reports/final-selection.csv`, escreve `reports/final-selection-audit.md`, escreve `reports/final-diversity.md`, preserva uma ancora publica/inalterada, suplementa anchors historicos conhecidos (`v178`, `v185`) quando a listagem recente da Kaggle os omite, promove ASSOC/DIFF near-best como hedge estrategico, aceita hedges ate `0.00325` abaixo do melhor publico, preenche slots restantes com reservas publicas controladas ate `0.00600` abaixo do melhor e filtra mutacoes KEEP-only grandes demais da selecao recomendada.
- `final-selection-audit` mede a carteira final: slots, queda publica maxima, queda publica dos slots substituiveis, mix de roles, slots ASSOC/DIFF, concentracao por condicao e prioridade de troca. O gate `public_floor` ignora os slots protegidos `Public anchor` e `Private hedge`; se `condition_concentration=crowded`, nao e bloqueio imediato, e sim sinal para diversificar a proxima selecao quando surgirem candidatos public-neutral melhores.
- `final-diversity` mede candidatos alternativos dentro do piso publico controlado que podem reduzir concentracao da carteira final; use como guia de swap, nao como substituto automatico da selecao.

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

A suite cobre diffs de CSV, relatorio de plano, auditoria de deltas ICD do plano, interpretacao de impacto pos-score, relatorio de inteligencia, guarda de notebook publico novo/atualizado antes de submissao, sync dry-run de notebooks publicos novos/atualizados, auditoria dos notebooks publicos, sinais publicos escalados, scorecard de plano, scorer offline do Train com rejeicao de no ICD desconhecido e granularidade minima, shortlist final ate 20 selecionaveis com CSV operacional e auditoria de concentracao, preflight, trava de data alvo no preflight e no `daily-run`, guarda de pos-relatorios sem atividade de plano ou retry parcial sem envio novo, deadline guard no preflight/submit-plan, reset de cota, plano reserva com permissao explicita, contingencias publicas `v261-v280`, `v321-v340`, `v361-v380` e `v401-v420`, prioridade de contingencia antes da reserva, caminho do proximo plano, inferencia automatica da proxima versao do adaptativo, salto de faixas ja reservadas em `submissions/`, guarda contra plano anterior incompleto, dedupe por conteudo ja submetido, dedupe interno de plano, reserva de slots privados, preferencia adaptativa por combos nao negativos, retry seguro no adaptativo, `daily-run` com/sem reports e falha segura de next-plan antes dos scores.
