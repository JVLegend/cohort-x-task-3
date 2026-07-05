# Plano da proxima janela - CohortX Task 3

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Estado atual para a proxima janela

- Diagnostico: 2026-07-05, depois do lote `v341`-`v360`.
- Cota Kaggle atual: `20/20`; nao tentar submissao adicional antes do reset UTC.
- Proximo reset: 2026-07-06 00:00 UTC / 2026-07-05 21:00 BRT.
- Melhor publico JV: `0.43156`, rank publico #8; gap para #7: `0.00585`.
- Plano primario selecionado: `plans/2026-07-06.csv` (`v381`-`v400`).
- Estado do plano: 20 validos, 20 ainda nao submetidos, 0 duplicatas de conteudo.
- Prontidao: `reports/2026-07-06-readiness.md` marca manifesto pronto, matriz de decisao
  pronta, auto-next pronto para `plans/2026-07-07.csv` com `start_version=421`, notebooks
  publicos `new=0, updated=0` e shortlist final 20/20.
- Integridade: `reports/2026-07-06-manifest.md` tem 20 hashes SHA-256 unicos e
  `drift=0` no preflight/readiness; qualquer drift antes do envio exige inspecao.

## Plano primario para 2026-07-06

Usar `plans/2026-07-06.csv`, com anchor operacional
`submissions/v296_copd_no_j20_j45_j81_j82_j93_j95.csv`.

- `v381`-`v400`: follow-ups pos-05/07 sobre os empates de topo (`v341`, `v342`, `v357`),
  com foco em source `v357`, manutencao/remocao de mediastino, fatiamento do hedge
  `v185` e controles ASSOC/DIFF.
- `reports/2026-07-06-strategy.md`: 20/20 itens, source publico maximo `0.43156`,
  source `v357` em 17 slots, source `v359` em 3, `med=keep` 8, `med=drop` 12,
  8 buckets private KEEP e 3 buckets ASSOC/DIFF.
- `reports/2026-07-06-decision.md`: 15 comparacoes pareadas para interpretar depois dos
  scores, especialmente `med`, fatiamento de `v185`, source family e ASSOC/DIFF.
- Watchlist: manifesto 06/07 esta limpo (`change_volume_watch=clear`, max volume 973);
  ainda assim, preservar a ordem do plano se houver falha parcial.

Comando canonico depois do reset:

```bash
.venv/bin/python src/cohortx_ops.py preflight
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

Nao passar `--date` na automacao normal. Submeter somente se o preflight do dia UTC atual
retornar `recommended_action=submit_primary`. Se retornar `wait_for_quota`,
`wait_for_target_date`, `competition_closed` ou bloqueio equivalente, o `daily-run` deve
parar com guarda antes de chamar `submit_plan`.

Se aparecer notebook publico novo/atualizado, rodar:

```bash
.venv/bin/python src/sync_public_notebooks.py
.venv/bin/python src/audit_public_notebooks.py
```

Depois dos scores de `v381`-`v400`, consultar:

- `reports/2026-07-06-scorecard.md`
- `reports/2026-07-06-decision-outcome.md`
- `reports/2026-07-06-impact.md`
- `reports/final-candidates.md`
- `reports/final-diversity.md`

Se o primario `plans/2026-07-06.csv` ficar inutilizavel no reset, usar como paraquedas
`plans/2026-07-06-public-contingency.csv` (`v401`-`v420`) antes de qualquer reserva.

## Estado historico 2026-07-05 pre-reset

- O plano `plans/2026-07-05.csv` (`v341`-`v360`) foi submetido completo e pontuado em
  2026-07-05 00:01-00:03 UTC.
- `v341`, `v342` e `v357` empataram o melhor publico `0.43156`; `v360` foi a unica
  piora contra `v296`.
- `reports/2026-07-05-decision-outcome.md` favorece `med=keep`, source `v302`,
  `ent_gi_derm_assocdiff` e menor volume nos empates de `private_keep`.

## Estado historico 2026-07-02

- Diagnostico: 2026-07-02 00:24 UTC / 2026-07-01 21:24 BRT.
- Cota Kaggle: `20/20`; nenhuma submissao adicional deve ser tentada antes do reset.
- Proximo reset: 2026-07-03 00:00 UTC / 2026-07-02 21:00 BRT.
- Automacao Codex: ativa em `00:20`, `01:20` e `02:20 UTC`, ate 2026-07-16 11:59 UTC.
- Melhor publico JV: `0.42687`, rank #8.
- Lote 2026-07-02 ficou parcial em arquivos unicos: `v201`-`v210` pontuaram, `v211`-`v220`
  nao foram enviados porque o Kaggle contou duplicatas no historico e esgotou a cota.
- Plano primario 2026-07-03 pronto: `plans/2026-07-03.csv` (`v281`-`v300`), gerado por
  `src/v281_300_assoc_diff.py` sobre `v209`.
- Alvo imediato: nao reenviar nada antes do reset; no proximo ciclo, submeter o plano
  primario ASSOC/DIFF se o preflight continuar com `primary_unsubmitted_items=20` e sem
  notebooks publicos novos/atualizados.

## MUDANCA DE PRIORIDADE 2026-07-01 rev 2 (ver ESTRATEGIA.md)

O plano antigo abaixo (`plans/2026-07-02.csv`) gasta as 20 balas lapidando COPD +
Enlarged Mediastinum, que sao 2 de 23 condicoes e so rendem milesimos. A frente de maior
retorno agora e **popular ASSOCIATION e DIFF SELETIVO nas condicoes invisiveis no
publico**. Verificado nos dados (rev 2): o gold e determinístico (escolher o no ICD certo
-> expandir descendentes), a granularidade do no decide a precisao, e ~40% das celulas
ASSOC/DIFF do Train tem gold vazio (vazio ja vale F1=1.0), entao encher em bloco e EV
negativo. Curar por (condicao, bucket).

Passo bloqueante 1 (offline, ZERO balas): calibrar os nos no `src/train_scorer.py` antes
de qualquer submissao. Rodar `--self-check` (teto = 1.0000) e `--spec` para validar que a
selecao de nos reproduz o gold do Train na granularidade certa.

Passo bloqueante 2: construir `src/vXXX_assoc_diff.py` a partir do dict de nos ja
calibrado. A infra de quota/dedupe/guard continua a mesma; muda o conteudo, nao o
encanamento.

Alocacao recomendada das 20 balas por janela:
- 12-14 balas: experimento ASSOC/DIFF (Fase A) SELETIVO e ja calibrado offline, em lotes
  DIFF-only / ASSOC-only / ambos, sempre sobre `v178_FINAL`, deixando COPD, Enlarged
  Mediastinum e toda condicao sem ligacao clinica inequivoca vazias.
- 3-4 balas: correcao de familias KEEP nas condicoes grandes invisiveis (Fase B); checar
  granularidade das raizes no scorer.
- 2-4 balas: os melhores probes publicos de COPD/Mediastinum do plano antigo (opcional).

## Plano primario para 2026-07-03

Usar `plans/2026-07-03.csv`, com anchor `submissions/v209_copd_no_acute_bronch_asthma.csv`.

- `v281`-`v292`: ASSOC/DIFF seletivo nas condicoes invisiveis no publico, incluindo lotes
  DIFF-only, ASSOC-only, grupos clinicos e combinacao com o hedge `v185` sem restaurar
  COPD/Mediastinum.
- `v293`-`v296`: combos publicos de COPD que preservam o ganho de `J20+J45` e testam
  remocoes adicionais que melhoraram em 2026-07-02.
- `v297`-`v300`: probes de Enlarged Mediastinum que nao foram consumidos em 2026-07-02.

Preflight verificado antes do reset:

```bash
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03
```

Resultado esperado antes da virada: `target_date_relation=future`, `primary_valid_items=20`,
`primary_unsubmitted_items=20`, `primary_duplicate_content_items=0`,
`selected_plan=plans/2026-07-03.csv`.

Comando canonico depois do reset:

```bash
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

`daily-run` e `submit-plan` usam `.cohortx_locks/submission.lock`; se uma segunda instancia
rodar ao mesmo tempo, ela deve sair com `submission_lock_held=true`.

## Paraquedas 2026-07-04

O caminho preferido apos `v281`-`v300` e o adaptativo gerar `plans/2026-07-04.csv` usando
os scores publicos dos probes `v293`-`v300`. Se isso nao acontecer a tempo, ja existe:

```bash
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-04
```

Com o primario ausente, o preflight deve selecionar
`plans/2026-07-04-public-contingency.csv` (`v321`-`v340`): `v209` + variantes de KEEP
privado `v185`, ASSOC/DIFF seletivo e alguns probes publicos isolados. Nao usar essa
contingencia se o adaptativo criar um primario melhor.

## Plano antigo (rebaixado a probes publicos opcionais)

`plans/2026-07-02.csv` foi parcialmente consumido: `v201`-`v210` foram submetidos e
pontuados; `v211`-`v220` seguem ausentes. O lote testa apenas as duas condicoes que
realmente mexeram no public split:

- `Chronic Obstructive Pulmonary Disease`: ablations finas e pequenas adicoes controladas.
- `Enlarged Mediastinum`: ablations finas e pequenas adicoes controladas.

Comando canonico da janela pos-reset:

```bash
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

Nao passar `--date` na automacao normal. O CLI usa a data UTC atual, valida plano/cota/deadline, envia o lote certo, atualiza relatorios e so cria `plans/2026-07-03.csv` se todos os 20 itens de `2026-07-02` aparecerem completos no historico Kaggle. Se o intel detectar notebook publico novo ou atualizado, o comando para antes do preflight/submissao com `new_public_notebooks_guard` e aponta `.venv/bin/python src/sync_public_notebooks.py`; baixar/diffar/auditar antes de usar qualquer override.

## Checklist antes de submissao manual

```bash
.venv/bin/python src/cohortx_ops.py status
.venv/bin/python src/cohortx_ops.py intel
.venv/bin/python src/sync_public_notebooks.py --dry-run
.venv/bin/python src/audit_public_notebooks.py
.venv/bin/python src/cohortx_ops.py preflight
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-03.csv
```

Submeter somente se o intel nao mostrar notebook publico novo/atualizado e o `preflight` indicar:

- `competition_open=true`
- `target_date_relation=current`
- `recommended_action=submit_primary`
- `primary_valid_items=20`
- `primary_unsubmitted_items` coerente com o plano escolhido e quota disponivel
- `primary_duplicate_content_items=0`

`--allow-new-notebooks` e apenas para uso manual depois que a ref nova ja foi baixada, comparada e auditada.

## Interpretacao depois dos scores

Relatorios a consultar depois da submissao:

- `reports/2026-07-02-scorecard.md`
- `reports/2026-07-02-impact.md`
- `reports/2026-07-02-code-deltas.md`
- `reports/final-candidates.md`

Decisao:

- Remocao que melhora public score: familia candidata a poda.
- Adicao que melhora public score: familia candidata a promocao.
- Empate: guardar como hedge privado se a mudanca for pequena.
- Piora: evitar a direcao daquela edicao em combos publicos.

## Plano seguinte

Se `v201-v220` pontuarem completo, o `daily-run --auto-next-plan` deve tentar gerar `plans/2026-07-03.csv` via `src/v221_240_adaptive_followups.py`.

Politica do adaptativo:

- Priorizar combos COPD + Mediastinum com delta publico nao negativo contra `v178_FINAL`.
- Reservar alguns slots para hedges privados sobre `v185_private_kw.csv`.
- Recusar plano primario se nao houver combo publico nao negativo.
- Inferir automaticamente o proximo `vNNN` pelo maior numero do plano anterior.

## Contingencias

Se o adaptativo nao puder gerar um plano primario para 2026-07-03, usar antes a contingencia publica:

```bash
.venv/bin/python src/cohortx_ops.py preflight --date 2026-07-03
.venv/bin/python src/cohortx_ops.py daily-run --date 2026-07-03 --auto-next-plan
```

Esse caminho seleciona `plans/2026-07-03-public-contingency.csv` quando a data for atual, o plano primario nao existir e a contingencia tiver 20 itens validos, nao submetidos e sem duplicatas.

Usar `plans/2026-07-03-reserve.csv` apenas se o adaptativo e a contingencia publica nao forem utilizaveis e a alternativa for perder quota diaria. Reserva exige `--allow-reserve`.

## Nao fazer

- Nao usar o plano antigo de Gemini/API para submissao de rotina.
- Nao chamar `kaggle competitions submit` cru, exceto em emergencia manual deliberada.
- Nao preencher `ASSOCIATION`/`DIFF` fora de probe controlado.
- Nao forcar `--allow-negative-fallback` na automacao.
- Nao submeter antes do reset UTC ou quando `recommended_action` for `wait_for_quota`, `wait_for_target_date` ou `competition_closed`.
