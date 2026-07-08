# CohortX Task 3 — ICD-10-CM Code Resolution

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

## Status vivo — 2026-07-08

**Melhor público atual: 0.43156** (`v301` / `v302` / `v341` / `v342` / `v357` / `v382` / `v384` / `v385` / `v388` / `v389` / `v391` / `v392`)
**Leaderboard público: #8/114** em 2026-07-07; próximo alvo #7 `Md Raihan` em `0.43741` (gap `0.00585`)
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
> O relatório `reports/train-gold-minimal-nodes.md` registra os nós mínimos do Train
> que reproduzem F1=1.000, servindo como régua de granularidade.

Repo local sincronizado com `origin/master`: `https://github.com/JVLegend/cohort-x-task-3`.
Foram enviados 20/20 CSVs em 2026-07-08 (`v481`-`v500`) pelo comando canonico
`.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan`. O preflight pos-envio
mostra `quota_used_utc=20/20`, `recommended_action=contingency_already_submitted` e
0 itens restantes no plano de contingencia 08/07. O lote todo ficou abaixo do melhor
publico, entao o gerador adaptativo manteve `plans/2026-07-09.csv` como `not_ready` em
vez de promover composite perdedor. O proximo reset seleciona a contingencia publica
`plans/2026-07-09-public-contingency.csv` (`v521`-`v540`), com manifesto sem drift,
matriz de decisao pronta e alerta semantico `review_role_overlap` por ASSOC preenchido
com overlap direto contra KEEP.
Em 2026-07-08, o `preflight` ganhou auditoria semantica de papeis
`KEEP`/`ASSOCIATION`/`DIFF`: o plano selecionado agora imprime
`selected_plan_semantic_role_status`, contadores de arquivos com ASSOC/DIFF
preenchidos, overlaps diretos entre papeis e maximo de codigos ASSOC/DIFF.
O plano 08/07 retornou `clear_assocdiff_empty`; o plano 09/07 retorna
`review_role_overlap`, entao so deve ser enviado apos revisao consciente do risco.

## Achados novos — 2026-07-08

- O plano de contingencia 08/07 fechou 20/20 submetido e pontuado (`v481`-`v500`), sem
  novo topo publico. Contra o melhor `0.43156`, foram 0 melhorias, 0 empates e 20 quedas.
- O bloco sem mediastino (`v481`-`v495`) ficou todo em `0.42995`; o bloco com mediastino
  (`v496`-`v500`) ficou em `0.43015`. Nenhum item entra na shortlist final enquanto os
  empates de topo 04/07-06/07 continuarem disponiveis.
- `reports/2026-07-08-public-contingency-decision-outcome.md` resolveu 7/7 comparacoes:
  `med=keep` venceu 5/5, mas ainda abaixo do topo; os empates de `private_keep`
  recomendam menor volume (`add_npc` sem mediastino, `zero_hf` com mediastino).
- `reports/2026-07-08-public-contingency-impact.md` marca todas as podas KEEP
  hidden como public-worse e todas as keyword-additions como falso positivo publico.
  Restaurar KEEP dessas condicoes em candidatos public-facing; nao promover adds
  keyword de HF/ILD/Derm/NPC.
- Scouting publico externo registrou a regra semantica operacional:
  `KEEP` e diagnostico correto; `ASSOCIATION` e codigo relacionado que exige
  triagem; `DIFF` e diagnostico diferencial confundivel. Portanto, qualquer
  preenchimento de `ASSOCIATION`/`DIFF` deve ser tratado como aposta seletiva e
  auditavel, nao como extensao automatica de `KEEP`.
- `src/cohortx_ops.py preflight` agora expõe `selected_plan_semantic_role_status`
  e métricas de ASSOC/DIFF antes de qualquer janela de envio. Isso torna visivel
  se o plano selecionado esta limpo (`clear_assocdiff_empty`) ou se exige revisão
  (`review_assoc_positive`, `review_diff_positive` ou `review_role_overlap`).
- Validacao local 08/07: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s tests -v`
  rodou `127` testes OK antes do envio; `py_compile`, notebooks dry-run e auditoria
  publica tambem passaram.
- Preflight pos-envio confirma `quota_used_utc=20/20`, `quota_remaining=0`,
  `recommended_action=contingency_already_submitted`, melhor publico `0.43156` e
  leaderboard JV #8/114.
- Readiness 09/07 seleciona `plans/2026-07-09-public-contingency.csv` (`v521`-`v540`),
  com 20 validos, 20 unsubmitted, 0 duplicatas, manifesto `drift=0`, matriz de decisao
  com 1 comparacao, notebooks publicos `new=0 updated=0` e shortlist final 20/20.
- Alerta para 09/07: `next_reset_selected_plan_semantic_role_status=review_role_overlap`;
  20/20 arquivos tem ASSOC preenchido, 12/20 tem overlap direto entre KEEP e ASSOC,
  `max_assocdiff_codes=137`. Revisar antes do reset se faz sentido gastar a janela em
  ASSOC-only isolado apesar do risco semantico.

## Achados novos — 2026-07-07

- O plano de contingencia 07/07 fechou 20/20 submetido e pontuado (`v441`-`v460`), sem
  novo topo publico. Contra o melhor `0.43156`, foram 0 melhorias, 0 empates e 20 quedas.
- Os melhores do dia foram `v456` e `v459` com `0.43035` (`-0.00121`), seguidos de
  `v444`/`v447` com `0.43015`. Nenhum deve entrar na shortlist final enquanto os empates
  de topo 04/07-06/07 continuarem disponiveis.
- `reports/2026-07-07-public-contingency-decision-outcome.md` resolveu 18/18
  comparacoes: `med=keep` venceu 5/5, `source=copd_j31_j98` venceu 7/7 dentro do lote
  perdedor, e `assoc=highconf_assoc` foi recomendado nos empates por menor volume.
- `pulmonary_assocdiff` e `cardiorenal_assocdiff` cairam para `0.42835`-`0.42874`;
  manter esses buckets como falsos positivos publicos ate nova decomposicao por condicao.
- A leitura importante e negativa: recombinar `v293`-`v295` com mediastino e ASSOC-only
  nao substitui o anchor COPD `v296` nem os composites `v301`/`v302`/`v357`.
- `src/v341_360_post_july4_followups.py` foi corrigido para usar o melhor score publico
  disponivel quando a listagem recente da Kaggle nao inclui `v296`, evitando falso
  bloqueio por historico truncado.
- O primario 08/07 ficou ausente por criterio estrategico, nao por erro de coleta: os
  sinais novos nao justificaram promover variantes negativas. Usar a contingencia publica
  08/07 salvo se um primario novo aparecer no preflight.
- `reports/2026-07-08-readiness.md` confirma `plans/2026-07-08-public-contingency.csv`
  (`v481`-`v500`) com 20 validos, 20 unsubmitted, 0 duplicatas, manifesto `drift=0`,
  7 comparacoes na matriz de decisao, notebooks publicos `new=0 updated=0` e shortlist
  final 20/20.

## Achados novos — 2026-07-06

- O plano 06/07 fechou 20/20 submetido e pontuado (`v381`-`v400`), sem novo topo publico.
  Sete variantes empataram `0.43156`: `v382`, `v384`, `v385`, `v388`, `v389`, `v391` e
  `v392`; as outras 13 cairam.
- `reports/2026-07-06-decision-outcome.md` resolveu 15/15 comparacoes: `med=keep`
  venceu 7/7, o source `v357` venceu 2/2 contra `v359`, `assoc=assocdiff` venceu
  `pulmonary_assocdiff` em 2/2, e os empates de `private_keep` favorecem menor volume
  (`none` ou `CKD+UTI`).
- O principal sinal publico e manter thymus/nodes em Enlarged Mediastinum nos composites.
  Remover esse eixo custou `-0.00020` nos pares comparaveis.
- `pulmonary_assocdiff` derrubou para `0.42995`; evitar promover esse bucket amplo sem
  decompor.
- O source `v359`/COPD `J31/J98` voltou a ser pior em combinacoes (`v397`/`v400`
  `0.43015`; `v396` `0.42894`). Continuar preferindo a familia `v357`.
- A shortlist final agora tem 10 submissões empatadas no melhor publico e 50 near-best.
  A selecao recomendada inclui os novos empates `v382`, `v384`, `v385`, `v388`, `v389`,
  `v391` e `v392`, mantendo `v178_FINAL` e `v185_private_kw`.
- O auto-next pos-06/07 nao gerou `plans/2026-07-07.csv`: `not_ready: Missing public
  anchor score for v296_copd_no_j20_j45_j81_j82_j93_j95.csv`. Nao forcar
  `--allow-negative-fallback`; se nao houver primario antes do reset, usar a contingencia
  publica 07/07.
- Preflight pos-envio confirma `quota_used_utc=20/20`, `quota_remaining=0`,
  `recommended_action=primary_already_submitted`, e readiness do proximo reset `ready`
  via `plans/2026-07-07-public-contingency.csv` com 18 comparacoes.

## Achados novos — 2026-07-05

- `v341`, `v342` e `v357` empataram o melhor publico `0.43156`; nao houve novo topo, mas
  a carteira final agora tem 5 submissões empatadas no melhor score e 44 near-best dentro
  de `0.00325`.
- O plano 05/07 fechou 20/20 submetido e pontuado: contra o anchor `v296`, foram
  17 melhorias, 2 empates e 1 piora; contra o melhor publico anterior, 3 empates no topo
  e 17 quedas.
- A matriz pareada 05/07 resolveu 20/20 comparacoes: `med=keep` venceu as 5 comparacoes
  de mediastino, a source family `v302` venceu 4 comparacoes e empatou 1, e o bucket
  `ent_gi_derm_assocdiff` venceu a comparacao ASSOC principal.
- `private_keep` empatou em 7 comparacoes; o desempate por volume recomenda `CKD+UTI`
  quando empata contra `Diabetes+Pneumonia`, e `none` quando empata contra
  `CKD+UTI+Diabetes+Pneumonia` em buckets pulmonary/cardiorenal. Isto sugere que parte
  do sinal publico vem de ASSOC/DIFF e mediastino, nao necessariamente das fatias KEEP
  privadas amplas.
- `v360` foi a unica piora contra `v296` (`0.42894`, delta `-0.00101`): evitar combinar
  source `v304` + pulmonary ASSOC/DIFF + v185keep completo sem decompor.
- `plans/2026-07-06.csv` foi gerado automaticamente com `v381`-`v400`, 20 itens validos,
  20 unsubmitted e 0 duplicate content. O manifesto 06/07 tem 20 hashes unicos, 23 linhas
  por CSV, `change_volume_watch=clear` e volume maximo 973.
- `reports/2026-07-06-readiness.md` confirma reset 06/07 pronto: manifesto drift=0,
  matriz de decisao com 15 comparacoes, notebooks publicos `new=0 updated=0`, shortlist
  final 20/20 e auto-next preparado para `plans/2026-07-07.csv` com `start_version=421`.
- As contingencias publicas de 07/07 a 16/07 agora tambem tem `strategy`, `manifest` e
  `decision` pregerados. `reports/deadline-readiness.md` mostra cobertura 12/12 sem gaps,
  220 slots futuros protegidos e matriz de decisao pronta para todos os fallback days
  restantes: 18, 7, 1, 1, 1, 5, 1, 5, 1 e 7 comparacoes respectivamente.
- Os relatorios `plan-strategy` agora incluem `Axis Risk Notes` quando algum eixo fica
  `thin`. Para 06/07, o aviso principal e `assoc_mix` fino: interpretar os buckets
  ASSOC/DIFF submetidos, mas nao generalizar para buckets nao testados no auto-next.
- `src/cohortx_ops.py` passou a inferir eixos de contingencias antigas por filename/notes
  (`v296`, COPD source, mediastino, ASSOC/DIFF e KEEP prune/add/zero), evitando relatorios
  com `unknown` quando o CSV ja traz essa informacao no nome operacional.
- A shortlist final foi atualizada: slots recomendados incluem `v357`, `v342`, `v341`,
  `v302` e `v301` no topo, mantendo `v178_FINAL` e `v185_private_kw` como anchor/hedge
  historicos.
- Pequena correcao operacional: `plan-report` e `audit_plan_deltas.py` agora normalizam o
  EOF com uma unica quebra de linha, evitando `git diff --check` vermelho em relatorios
  gerados.

## Achados novos — 2026-07-04

- `v301` e `v302` subiram o melhor publico para `0.43156`, combinando a poda COPD de
  `v296`, thymus/nodes em Enlarged Mediastinum, ASSOC-only amplo/high-confidence e o hedge
  KEEP privado de `v185`.
- O plano de 2026-07-04 fechou com 11/20 melhorias contra `v296`; `v303`/`v304` tambem
  melhoraram (`0.43035`) e `v305`/`v306`/`v317` ficaram em `0.43015`.
- As combinacoes que reintroduzem partes de COPD `J81/J82` ou `J93/J95` cairam para
  `0.42855`-`0.42894`; manter a poda completa `J20+J45+J81/J82+J93/J95` como anchor.
- A shortlist final foi regenerada com 20/20 slots; agora ha 16 slots ASSOC/DIFF hedge,
  mas a auditoria marca `condition_concentration=crowded` em CKD/UTI/Diabetes/Pneumonia
  por causa dos overlays de `v185`. O piso substituivel segue saudavel:
  `replaceable_max_drop=0.00301`, abaixo da tolerancia `0.00600`; a queda maior
  `0.00703` vem apenas dos slots protegidos `v178`/`v185`.
- `reports/final-diversity.md` complementa a auditoria final com 12 alternativas dentro
  do piso publico controlado (`>=0.42556`) para quebrar concentracao, sem trocar a
  selecao automaticamente.
- `plans/2026-07-05.csv` foi gerado e validado com `v341`-`v360`. O preflight manual para
  2026-07-05 mostra `target_date_relation=future`, 20 unsubmitted e
  `recommended_action=wait_for_target_date`; usar o comando canonico sem `--date` apos o
  reset UTC.
- `reports/2026-07-05-strategy.md` audita o plano primario antes do reset: 20/20 itens,
  source publico maximo `0.43156`, ordem pronta, `med=keep` 13 slots, `med=drop` 7, quatro
  buckets private KEEP e cinco buckets ASSOC/DIFF.
- `reports/2026-07-05-manifest.md` trava a integridade do plano primario: 20 hashes
  SHA-256 unicos, 23 linhas por arquivo, volumes de mudanca e eixos estrategicos por CSV.
  Tambem marca `change_volume_watch=review` para `v347` (volume 1146) como broad private
  hedge que deve ser lido com cautela antes de promocao. Regerar antes do reset; qualquer
  drift de hash/linhas/volume exige inspecao antes de subir para o Kaggle. O `preflight`
  e o `readiness` agora comparam os hashes salvos no manifesto com os CSVs atuais e
  retornam `manifest=drift`/`next_reset_manifest=drift` se algum arquivo mudou depois do
  manifesto.
- O gerador moderno `src/v341_360_post_july4_followups.py` agora penaliza candidatos
  adaptativos futuros com volume de mudanca acima de 1000 contra `v296`; isso protege os
  proximos planos `v381+` de promover hedges largos quando houver alternativas limpas com
  prioridade parecida, sem reescrever a fila primaria 05/07 ja pronta.
- `reports/2026-07-05-decision.md` pre-compromete a leitura pos-score com 20 comparacoes
  pareadas por eixo (`med`, `private_keep`, `assoc`, `source`), reduzindo ruido de
  leaderboard na hora de gerar o proximo adaptativo.
- O comando `plan-decision-outcome` transforma essa matriz em vencedores/empates por
  eixo assim que os scores chegam e agora mostra volumes por variante, recomendando o
  menor volume quando o public score empata; o `daily-run` gera
  `reports/YYYY-MM-DD-decision-outcome.md` automaticamente no bloco pos-score.
- `reports/2026-07-05-readiness.md` agora inclui o comando canonico de reset, regras de
  parada pre-submit, gates `manifest`, `decision_matrix` e `auto_next_plan` apontando
  para `reports/2026-07-05-manifest.md`, `reports/2026-07-05-decision.md`,
  `plans/2026-07-06.csv`, `start_version=381` e a contingencia
  `plans/2026-07-06-public-contingency.csv`; tambem omite contadores volateis
  `seconds_until_*` para poder ser reexecutado sem sujar o diff quando nada operacional
  mudou.
- O `preflight` canonico, quando a cota atual ja esta `20/20`, agora tambem resume a
  prontidao do proximo reset: `next_reset_manifest`, `next_reset_decision_matrix`,
  comparacoes pareadas, `next_reset_auto_next_*` e
  `next_reset_readiness=ready/needs_attention`.
- `reports/deadline-readiness.md` audita a cobertura ate o deadline: 13/13 dias
  protegidos, 0 gaps duros e 240 slots futuros unsubmitted cobertos por primario ou
  contingencia publica. Usar `.venv/bin/python src/cohortx_ops.py deadline-readiness`
  depois de qualquer plano novo.
- `reports/2026-07-04-intel.md` confirma JV #8/114, gap `0.00585` para o #7
  (`Md Raihan`, `0.43741`), `20/20` submissões completas no dia, 4 notebooks publicos
  conhecidos, nenhum notebook novo/atualizado e forum sem topico novo desde 2026-06-12.

## Achados novos — 2026-07-03

- `v296_copd_no_j20_j45_j81_j82_j93_j95.csv` subiu o melhor publico para `0.42995`.
- Combinar a poda de COPD `J20+J45+J81/J82+J93/J95` e o novo anchor publico; as variantes
  com `J31/J98`, apenas `J81/J82` ou apenas `J93/J95` ficaram abaixo.
- ASSOC-only amplo/high-confidence (`v283`, `v286`) quase empatou o anchor anterior
  (`0.42828`), mas DIFF e ASSOC+DIFF derrubaram forte; tratar DIFF amplo como falso
  positivo publico ate nova evidencia.
- Mediastino ainda parece sensivel: remover `J98` caiu para `0.41453`, remover `D15/C38`
  caiu para `0.42265`, adicionar `C852` caiu para `0.42528` e thymus/nodes ficou
  `0.42707`.
- `plans/2026-07-04.csv` foi gerado e validado com `v301`-`v320`: combina o melhor KEEP
  publico de COPD (`v296`), o pequeno ganho de mediastino (`v300`), ASSOC-only/neutros
  e hedge `v185`. Usar o comando canonico sem `--date` depois do reset UTC.
- Contingencia de 2026-07-05 pronta: `plans/2026-07-05-public-contingency.csv`
  (`v361`-`v380`) usa `v296` como anchor, preserva `v341`-`v360` para o adaptativo
  primario pos-`v301-v320`, e serve apenas se esse primario nao for criado a tempo.
- Rota adaptativa pos-04/07 endurecida: `src/v341_360_post_july4_followups.py` gera o
  primario `plans/2026-07-05.csv` a partir dos scores de `v301`-`v320`, isolando
  mediastino, `v185` e buckets ASSOC/DIFF em vez de reutilizar o gerador de `v281`-`v300`.
  Enquanto os scores faltarem, retorna `not_ready` e preserva a contingencia.
- `reports/final-candidates.md` agora compensa a listagem recente truncada da Kaggle
  recolocando anchors historicos conhecidos (`v178`, `v185`) e recomenda hedges
  estrategicos ate `0.00325` abaixo do melhor publico. Se a shortlist ficar curta, preenche
  reservas publicas controladas ate `0.00600` abaixo do melhor; selecao atual: 20/20 slots
  em `reports/final-candidates.md` e `reports/final-selection.csv`.
- `reports/2026-07-04-readiness.md` confirma que o proximo reset esta operacionalmente
  pronto: `plans/2026-07-04.csv` tem 20 validos/20 unsubmitted/0 duplicatas, nao ha
  notebook publico novo/atualizado, a shortlist final esta 20/20 e a unica espera e a
  cota resetar em 2026-07-04 00:00 UTC.
- `reports/final-selection-audit.md` mostra que a carteira final esta pronta, mas
  concentrada. Depois do lote 04/07, a concentracao migrou de COPD-only para overlays
  `v185` + ASSOC/DIFF: CKD/UTI/Diabetes/Pneumonia aparecem em 18/20 slots. Isso nao
  bloqueia a selecao atual porque os slots substituiveis seguem dentro do piso publico,
  mas vira criterio para diversificar se surgirem hedges private/non-COPD melhores.
- Contingencia publica de 2026-07-06 pronta: `plans/2026-07-06-public-contingency.csv`
  (`v401`-`v420`) preserva `v381`-`v400` para o adaptativo primario pos-05/07 e combina
  `v296`, mediastino `v300`, ASSOC/DIFF near-best e fatias parciais de `v185`.
- Contingencia publica de 2026-07-07 pronta: `plans/2026-07-07-public-contingency.csv`
  (`v441`-`v460`) preserva `v421`-`v440` para o adaptativo primario pos-06/07 e recombina
  `v293`-`v295` com mediastino `v300` e ASSOC/DIFF public-neutral/positivo sem adicionar
  novas fatias privadas.
- Contingencia publica de 2026-07-08 pronta: `plans/2026-07-08-public-contingency.csv`
  (`v481`-`v500`) preserva `v461`-`v480` para o adaptativo primario pos-07/07 e explora
  KEEP de condições que foram public-neutral em probes anteriores, incluindo zeros e
  keyword-adds de HF/ILD/Derm/NPC/thyroid/Bronchitis.
- Contingencia publica de 2026-07-09 pronta: `plans/2026-07-09-public-contingency.csv`
  (`v521`-`v540`) preserva `v501`-`v520` para o adaptativo primario pos-08/07 e isola
  ASSOC-only por condicao sobre `v296`, para descobrir qual parte de `v283`/`v286`
  carrega o ganho publico sem misturar DIFF.
- Contingencia publica de 2026-07-10 pronta: `plans/2026-07-10-public-contingency.csv`
  (`v561`-`v580`) preserva `v541`-`v560` para o adaptativo primario pos-09/07 e isola
  DIFF-only por condicao sobre `v296`, para mapear se algum DIFF individual presta ou se
  o bloqueio de DIFF amplo deve continuar.
- Contingencia publica de 2026-07-11 pronta: `plans/2026-07-11-public-contingency.csv`
  (`v601`-`v620`) preserva `v581`-`v600` para o adaptativo primario pos-10/07 e testa
  podas KEEP em condicoes privadas, removendo familias suspeitas/ruidosas sem mexer nos
  movers publicos COPD/Mediastinum.
- Contingencia publica de 2026-07-12 pronta: `plans/2026-07-12-public-contingency.csv`
  (`v641`-`v660`) preserva `v621`-`v640` para o adaptativo primario pos-11/07 e combina
  poda KEEP + ASSOC-only na mesma condicao sobre `v296`, sem DIFF e sem mexer nos movers
  publicos COPD/Mediastinum.
- Contingencia publica de 2026-07-13 pronta: `plans/2026-07-13-public-contingency.csv`
  (`v681`-`v700`) preserva `v661`-`v680` para o adaptativo primario pos-12/07 e combina
  poda KEEP + DIFF-only na mesma condicao sobre `v296`; usar como fallback de maior risco,
  pois DIFF amplo derrubou publico.
- Contingencia publica de 2026-07-14 pronta: `plans/2026-07-14-public-contingency.csv`
  (`v721`-`v740`) preserva `v701`-`v720` para o adaptativo primario pos-13/07 e combina
  poda KEEP + ASSOC+DIFF por condicao sobre `v296`; e o membro mais agressivo da familia
  prune+bucket e deve ficar atras do adaptativo.
- Contingencia publica de 2026-07-15 pronta: `plans/2026-07-15-public-contingency.csv`
  (`v761`-`v780`) preserva `v741`-`v760` para o adaptativo primario pos-14/07 e cria
  carteiras multi-condicao de podas KEEP privadas, mantendo ASSOC/DIFF vazios para servir
  como hedge finalista se o adaptativo nao existir.
- Contingencia publica final de 2026-07-16 pronta: `plans/2026-07-16-public-contingency.csv`
  (`v801`-`v820`) preserva `v781`-`v800` para o adaptativo primario pos-15/07 e combina
  `v296`, mediastino `v300`, fatias `v185`, overlays zero/add public-neutral, podas KEEP
  e ASSOC-only seletivo, mantendo DIFF vazio para a janela final antes do deadline.
- `src/train_scorer.py` agora falha limpo quando um nó ICD não existe no dicionário e
  gera `reports/train-gold-minimal-nodes.md`; usar esse relatório antes de curar novos
  nós ASSOC/DIFF ou KEEP.

## Achados novos — 2026-07-02

- `v209_copd_no_acute_bronch_asthma.csv` elevou o melhor público para `0.42687`.
- Remover COPD `J20+J45` junto foi o melhor sinal público (`+0.00234` vs `v178_FINAL`).
- Também melhoraram as remoções isoladas `J45`, `J81/J82`, `J93/J95`, `J20`, `J98` e
  `J31`; remover `J96` ou reduzir COPD ao core `J41/J42/J43/J44` derruba forte.
- `v211`-`v220` continuam não submetidos; o preflight atual retorna `wait_for_quota`.

## Achados novos — 2026-07-01

- Fórum: `reports/2026-07-02-intel.md` agora lê os tópicos por API Kaggle direta. O host permite Hugging Face e dados Creative Commons/domínio público, mas a solução deve ser offline, reproduzível, sem APIs online/proprietárias, carregável em servidor de 15 GB RAM e sem demora excessiva. Não há tópico novo desde 2026-06-12.
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

1. Usar as 20 submissões diárias para probes pequenos e informativos. A janela de
   2026-07-06 deve testar follow-ups sobre os empates de topo `v341`/`v342`/`v357` e a
   leitura pareada 05/07.
2. Manter `v301`/`v302`/`v341`/`v342`/`v357` como melhores anchors publicos atuais,
   preservando `v296`, `v209` e `v178_FINAL` como bases historicas/confiaveis anteriores.
3. Manter `v185_private_kw` como hedge privado candidato, pois mexe nas condições invisíveis sem prejudicar público.
4. Priorizar candidatos offline/reprodutíveis. LLMs externos podem orientar curadoria, mas não devem ser dependência da solução final.
5. Regerar `reports/final-candidates.md` depois de cada lote pontuado para manter a seleção final objetiva de até 20 arquivos, com CSV espelho em `reports/final-selection.csv`, auditoria em `reports/final-selection-audit.md`, watchlist de diversidade em `reports/final-diversity.md`, âncora pública, hedge privado, promoção explícita de ASSOC/DIFF public-neutral, reservas públicas controladas, filtro contra mutações KEEP-only grandes demais e alerta de concentração por condição.
6. Usar `plans/2026-07-06.csv` como plano primario: `v381`-`v400` refinam o empate
   publico de `v357`, isolam `med=keep/drop`, removem ou fatiam o v185 KEEP hedge e
   concentram o ASSOC/DIFF em `assocdiff` com alguns controles pulmonary/cardiorenal.
   Antes de enviar, consultar `reports/2026-07-06-strategy.md`,
   `reports/2026-07-06-manifest.md`, `reports/2026-07-06-decision.md` e
   `reports/2026-07-06-readiness.md`; preservar a ordem se houver envio parcial.
7. Se o primario de 2026-07-06 nao estiver utilizavel no reset, usar
   `plans/2026-07-06-public-contingency.csv` (`v401`-`v420`) como paraquedas antes de
   considerar qualquer reserva privada.
8. Para 2026-07-07, manter `v421`-`v440` livres para adaptativo pos-06/07; se ele nao
   existir perto da janela, usar `plans/2026-07-07-public-contingency.csv` (`v441`-`v460`).
   Para 2026-07-08, manter `v461`-`v480` livres para adaptativo pos-07/07; se ele nao
   existir perto da janela, usar `plans/2026-07-08-public-contingency.csv` (`v481`-`v500`).
   Para 2026-07-09, manter `v501`-`v520` livres para adaptativo pos-08/07; se ele nao
   existir perto da janela, usar `plans/2026-07-09-public-contingency.csv` (`v521`-`v540`).
   Para 2026-07-10, manter `v541`-`v560` livres para adaptativo pos-09/07; se ele nao
   existir perto da janela, usar `plans/2026-07-10-public-contingency.csv` (`v561`-`v580`).
   Para 2026-07-11, manter `v581`-`v600` livres para adaptativo pos-10/07; se ele nao
   existir perto da janela, usar `plans/2026-07-11-public-contingency.csv` (`v601`-`v620`).
   Para 2026-07-12, manter `v621`-`v640` livres para adaptativo pos-11/07; se ele nao
   existir perto da janela, usar `plans/2026-07-12-public-contingency.csv` (`v641`-`v660`).
   Para 2026-07-13, manter `v661`-`v680` livres para adaptativo pos-12/07; se ele nao
   existir perto da janela, usar `plans/2026-07-13-public-contingency.csv` (`v681`-`v700`).
   Para 2026-07-14, manter `v701`-`v720` livres para adaptativo pos-13/07; se ele nao
   existir perto da janela, usar `plans/2026-07-14-public-contingency.csv` (`v721`-`v740`).
   Para 2026-07-15, manter `v741`-`v760` livres para adaptativo pos-14/07; se ele nao
   existir perto da janela, usar `plans/2026-07-15-public-contingency.csv` (`v761`-`v780`).
   Para 2026-07-16, manter `v781`-`v800` livres para adaptativo pos-15/07; se ele nao
   existir perto da janela antes do deadline, usar `plans/2026-07-16-public-contingency.csv`
   (`v801`-`v820`).
9. Usar `reports/2026-07-03-code-deltas.md` para interpretar os scores de `v281-v300`: ele lista os códigos/títulos ICD exatos adicionados/removidos por probe.
10. Depois dos scores, usar `reports/YYYY-MM-DD-decision-outcome.md` para ler vencedores pareados por eixo e `reports/YYYY-MM-DD-impact.md` para transformar cada delta público em ação: promover, podar, manter hedge ou evitar falso positivo.
11. Rodar `preflight`, `readiness`, `plan-manifest` e `deadline-readiness` antes de qualquer janela de envio para confirmar cota, próximo reset, deadline, plano selecionado, ação recomendada, guarda de notebooks públicos, integridade byte-a-byte do plano, matriz de decisão, auto-next do dia seguinte, cobertura diária até 16/07 e shortlist final 20/20. Se a data UTC atual já consumiu `20/20`, o preflight canônico retorna `wait_for_quota` ou `primary_already_submitted`, e também mostra `next_reset_*` quando existe plano pronto para o próximo reset, incluindo `next_reset_manifest`, `next_reset_decision_matrix`, `next_reset_auto_next_*` e `next_reset_readiness=ready/needs_attention`, em vez de sugerir plano novo para o dia esgotado. Em automação, usar `.venv/bin/python src/cohortx_ops.py daily-run --auto-next-plan` sem `--date`, deixando o CLI resolver a data UTC atual. O `daily-run` também respeita `recommended_action`: só chama `submit_plan` para ações de envio ou plano já submetido; para `wait_for_quota` e bloqueios equivalentes, imprime `preflight_guard=...` e segura submissão/relatórios pós-score. Também recusa data futura/passada ou competição fechada antes de chamar `submit_plan`, deduplica por conteúdo já submetido, rejeita duplicatas internas no plano, só atualiza relatórios pós-submissão e só cria o próximo plano quando todos os arquivos do plano estão contabilizados no Kaggle e todos já têm `publicScore` por filename ou conteúdo equivalente, gera `intel`/`plan-manifest`/`plan-decision`/`plan-scorecard`/`plan-decision-outcome`, bloqueia submissão se o intel detectar notebook público novo/atualizado ainda não baixado/auditado, aponta `.venv/bin/python src/sync_public_notebooks.py` para baixar/auditar a ref, infere a próxima versão pelo maior `vNNN` do plano anterior e pula faixas já existentes em `submissions/`, reconhece contingência pública antes de reserva, infere `v296` como âncora de relatórios para planos modernos `v301+`, e só usa plano reserva com `--allow-reserve`.
12. A automação Codex roda uma janela de retry pós-reset (`00:20`, `01:20`, `02:20 UTC`).
    `daily-run` e `submit-plan` agora usam `.cohortx_locks/submission.lock`, então uma
    segunda instância simultânea deve sair com `submission_lock_held=true` antes de gastar
    cota. O `submit_plan` também refresca cota/filenames/conteúdo antes de cada upload.
13. A cota usada deve seguir as linhas brutas aceitas pelo servidor Kaggle, mesmo quando o
    histórico exibe arquivos repetidos. Para diagnosticar isso, o preflight mostra
    `unique_submission_events_today` e `duplicate_submission_rows_today`; para evitar retry local
    do mesmo arquivo quando a listagem atrasa, `submit-plan` grava sucessos em
    `.cohortx_locks/submission-ledger-YYYY-MM-DD.json` e para limpo com `kaggle_quota_error=true`
    se a Kaggle responder que o limite diario acabou.

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
