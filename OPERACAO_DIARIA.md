# Operacao Diaria — CohortX Task 3

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Objetivo

Enviar ate 20 submissoes por dia ate o fim da competicao, sempre com probes pequenos e informativos, evitando duplicatas e registrando o aprendizado no repo.

## Rotina de cada ciclo

1. Revalidar Kaggle:
   - `.venv/bin/python src/cohortx_ops.py status`
   - `.venv/bin/kaggle competitions leaderboard -c cohort-x-task-3 -s`
2. Checar se existem notebooks/discussoes novas.
3. Ler `README.md`, `SUBMIT_QUEUE.md`, scripts recentes e `git status`.
4. Gerar ate 20 candidatos novos e nao duplicados.
5. Validar todos os CSVs:
   - 23 linhas.
   - colunas `Condition,KEEP,ASSOCIATION,DIFF`.
   - sem linhas vazias acidentais.
6. Gerar o relatorio de plano antes da submissao:
   - `.venv/bin/python src/cohortx_ops.py plan-report plans/YYYY-MM-DD.csv`
7. Submeter ate o limite diario.
8. Esperar todos ficarem `complete`.
9. Atualizar:
   - `reports/YYYY-MM-DD.md` com `.venv/bin/python src/cohortx_ops.py review --date YYYY-MM-DD`.
   - `reports/YYYY-MM-DD-signals.md` com `.venv/bin/python src/cohortx_ops.py signals --date YYYY-MM-DD`.
   - `README.md` se o melhor score/insight mudou.
   - `SUBMIT_QUEUE.md` com score, leitura e plano seguinte.
   - `03_Resources/Kanban/kanban.json` no vault SuperJV quando houver mudanca de status relevante.
10. Se o lote anterior ja tiver scores completos e ainda nao houver plano para o proximo dia, gerar follow-ups adaptativos:
   - `.venv/bin/python src/v221_240_adaptive_followups.py --prior-plan plans/YYYY-MM-DD.csv --out-plan plans/YYYY-MM-DD_NEXT.csv`
   - `.venv/bin/python src/cohortx_ops.py validate-plan plans/YYYY-MM-DD_NEXT.csv`

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
.venv/bin/python src/cohortx_ops.py daily-run --date 2026-07-02 --auto-next-plan
```

Equivalente expandido:

```bash
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py plan-report plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py submit-plan plans/2026-07-02.csv
.venv/bin/python src/cohortx_ops.py review --date 2026-07-02
.venv/bin/python src/cohortx_ops.py signals --date 2026-07-02
```

O script:

- conta submissoes do dia UTC;
- `daily-run` encadeia status, validacao, plan-report, submissao, review e signals;
- `--auto-next-plan` tenta gerar `plans/YYYY-MM-DD+1.csv` depois que os scores do lote estiverem completos;
- respeita o limite `20/dia`;
- pula arquivos ja submetidos;
- valida linhas/colunas dos CSVs;
- gera `reports/YYYY-MM-DD-plan.md` para auditar mudancas planejadas antes do envio;
- espera scores completarem quando submete;
- inclui as notas de `plans/YYYY-MM-DD.csv` no relatorio diario quando o plano existir;
- compara cada submissao local contra `v178_FINAL.csv` para extrair sinais publicos por condicao.

## Follow-up adaptativo

Depois que `v201-v220` forem enviados e pontuados, rodar:

```bash
.venv/bin/python src/v221_240_adaptive_followups.py --prior-plan plans/2026-07-02.csv --out-plan plans/2026-07-03.csv
.venv/bin/python src/cohortx_ops.py validate-plan plans/2026-07-03.csv
```

Esse gerador ranqueia as variantes de COPD e Enlarged Mediastinum por score publico, cria combinacoes entre os melhores sinais e duplica parte delas sobre `v185_private_kw.csv` para preservar hedge privado.

## Testes locais

Antes de alterar a orquestracao ou os relatórios operacionais:

```bash
.venv/bin/python -m unittest discover -s tests -v
```

A suite cobre diffs de CSV, relatorio de plano, caminho do proximo plano, `daily-run` com/sem reports e falha segura de next-plan antes dos scores.
