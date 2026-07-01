# Plano da proxima janela - CohortX Task 3

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Estado confirmado

- Diagnostico: 2026-07-01 13:06 UTC / 10:06 BRT.
- Cota Kaggle: `20/20`; nenhuma submissao adicional deve ser tentada antes do reset.
- Proximo reset: 2026-07-02 00:00 UTC / 2026-07-01 21:00 BRT.
- Automacao Codex: ativa em `00:20`, `01:20` e `02:20 UTC`, ate 2026-07-16 11:59 UTC.
- Melhor publico JV: `0.42453`, rank #9.
- Alvo imediato: superar `0.42491` do #8 publico.

## Plano primario para 2026-07-02

Usar `plans/2026-07-02.csv`, que ja esta validado com 20 itens, 20 ainda nao submetidos e 0 duplicatas de conteudo. O lote testa apenas as duas condicoes que realmente mexeram no public split:

- `Chronic Obstructive Pulmonary Disease`: ablations finas e pequenas adicoes controladas.
- `Enlarged Mediastinum`: ablations finas e pequenas adicoes controladas.

Comando canonico da janela pos-reset:

```bash
.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan
```

Nao passar `--date` na automacao normal. O CLI usa a data UTC atual, valida plano/cota/deadline, envia o lote certo, atualiza relatorios e so cria `plans/2026-07-03.csv` se todos os 20 itens de `2026-07-02` aparecerem completos no historico Kaggle. Se o intel detectar notebook publico novo, o comando para antes do preflight/submissao com `new_public_notebooks_guard`; baixar/diffar/auditar antes de usar qualquer override.

## Checklist antes de submissao manual

```bash
.venv/bin/python src/cohortx_ops.py status
.venv/bin/python src/cohortx_ops.py intel
.venv/bin/python src/audit_public_notebooks.py
.venv/bin/python src/cohortx_ops.py preflight
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-02.csv
```

Submeter somente se o intel nao mostrar notebook publico novo e o `preflight` indicar:

- `competition_open=true`
- `target_date_relation=current`
- `recommended_action=submit_primary`
- `primary_valid_items=20`
- `primary_unsubmitted_items=20`
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
