# Operacao Diaria — CohortX Task 3

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Objetivo

Enviar ate 20 submissoes por dia ate o fim da competicao, sempre com probes pequenos e informativos, evitando duplicatas e registrando o aprendizado no repo.

## Rotina de cada ciclo

1. Revalidar Kaggle:
   - `kaggle competitions list -s cohort-x-task-3`
   - `kaggle competitions submissions -c cohort-x-task-3 -v`
   - `kaggle competitions leaderboard -c cohort-x-task-3 -s`
2. Checar se existem notebooks/discussoes novas.
3. Ler `README.md`, `SUBMIT_QUEUE.md`, scripts recentes e `git status`.
4. Gerar ate 20 candidatos novos e nao duplicados.
5. Validar todos os CSVs:
   - 23 linhas.
   - colunas `Condition,KEEP,ASSOCIATION,DIFF`.
   - sem linhas vazias acidentais.
6. Submeter ate o limite diario.
7. Esperar todos ficarem `complete`.
8. Atualizar:
   - `README.md` se o melhor score/insight mudou.
   - `SUBMIT_QUEUE.md` com score, leitura e plano seguinte.
   - `03_Resources/Kanban/kanban.json` no vault SuperJV quando houver mudanca de status relevante.

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
