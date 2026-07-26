# Plano de avanco CohortX Task 3 - 10 a 16 de julho de 2026

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

> [!important] Status deste documento
> Este documento nasceu como plano, mas o JV autorizou a execucao em seguida. Em
> 2026-07-09 foi implementado o primeiro lote primario adaptativo:
> `plans/2026-07-10.csv`, gerado por `src/v541_560_july10_primary.py`. Nenhuma submissao
> adicional foi feita nesta etapa porque a cota Kaggle ja estava em `20/20`; o envio fica
> para depois do reset de 2026-07-10 00:00 UTC / 2026-07-09 21:00 BRT.

## Resultado pretendido

Sair do plateau publico de `0.43156`, disputar ao menos a faixa do atual #7
(`0.43741`) e, principalmente, chegar ao fechamento com 20 finalistas que cubram
hipoteses privadas realmente diferentes. O plano nao promete um salto especifico:
ele troca volume de submissao por experimentos identificaveis, curadoria clinica
calibrada e diversidade mensuravel.

O maior ganho possivel agora nao esta na automacao. A operacao, os guards e as
contingencias ja estao maduros. O gargalo e escolher melhor os nos ICD, separar os
papeis KEEP/ASSOCIATION/DIFF e aprender o maximo com cada uma das 140 balas teoricas
restantes entre 10 e 16 de julho.

## Ponto de partida

- Melhor publico: `0.43156`, rank #8/114 em 09/07.
- Alvo publico imediato: `0.43741`, diferenca de `0.00585`.
- Deadline: 16/07/2026 11:59 UTC, ou 08:59 BRT.
- Cota: 20 submissões por reset UTC e ate 20 submissões finais selecionaveis.
- O lote 09/07 nao melhorou: `v521` ficou em `0.43136`; `v522`-`v540`, em
  `0.42995`.
- A selecao final atual esta concentrada: Epistaxis em 18/20 slots, COPD em 18/20,
  Enlarged Mediastinum e Hematemesis em 17/20, e nenhum slot com mudanca em DIFF.
- As contingencias de 10 a 16/07 estao prontas, mas sao fallbacks. Elas nao devem ser
  tratadas como plano primario automatico.

## Correcao estrategica

A frase antiga "so COPD e Enlarged Mediastinum movem o publico" deve ser aposentada.
Os isolamentos de 08 e 09/07 mostram que mudancas de uma unica celula em varias
condicoes alteram o score publico, muitas vezes pelo mesmo degrau de `-0.00161`.
Portanto:

1. Toda condicao deve ser tratada como potencialmente avaliada no publico ate que um
   isolamento controlado prove o contrario.
2. Empate publico significa apenas que a alteracao foi neutra para o split publico;
   nao prova ganho privado.
3. Queda uniforme pode significar celula vazia no gold, predicao sem intersecao ou um
   degrau da metrica. Nao se deve escolher entre essas explicacoes sem novo contraste.
4. O score publico continua util para eliminar familias claramente ruins, mas nao e
   suficiente para escolher sozinho os 20 finalistas.

## Tese de avanco

O trabalho segue tres trilhos que se encontram nos dias finais:

### Trilho 1 - Aprender o split publico

Usar isolamentos e ablacões hierarquicas para descobrir quais celulas e quais nos ICD
tem sinal. Cada lote deve mudar uma unica dimensao ou formar uma matriz fatorial com
comparacoes pareadas. Variantes amplas, sem um contraste que permita explicar o
resultado, ficam proibidas.

### Trilho 2 - Reconstruir o private por regra clinica

Usar o Train para aprender a funcao de rotulagem, nao para copiar familias. O gold
ensina que o alvo e um conjunto de nos ICD em granularidade especifica, expandido para
todos os descendentes. Para cada condicao de teste, a outra sessao deve produzir uma
especificacao clinica versionada com tres larguras: `narrow`, `balanced` e `broad`.

### Trilho 3 - Otimizar o portfolio final

Selecionar os 20 finalistas como um conjunto, nao como os 20 maiores scores. O conjunto
precisa combinar ancora publica, exploracao KEEP, ASSOCIATION seletiva, DIFF seletivo e
alguns candidatos de maior variancia privada. Diversidade deve ser medida por celula,
condicao, papel e nos ICD.

## Fase 0 - Controles antes de gastar quota

Objetivo: impedir que um score seja atribuido ao eixo errado.

1. Congelar duas bases canonicas:
   - `public_anchor`: melhor conteudo publico conhecido, semanticamente equivalente ao
     anchor `v296`/melhores empatados.
   - `private_anchor`: a versao conservadora com hedge KEEP atualmente representada por
     `v185` ou seu melhor sucessor validado.
2. Comparar cada candidato com o anchor por hash semantico e diff por
   `(condicao, papel, codigo)`. O relatorio deve listar exatamente as celulas mudadas.
3. Criar um ledger de hipoteses com: id, anchor, eixo, condicao, nos adicionados ou
   removidos, motivo clinico, score esperado, score observado e decisao.
4. Recalcular o custo aparente de uma celula a partir dos deltas repetidos de 08/09.
   Registrar como hipotese, nao como propriedade confirmada da metrica.
5. Bloquear candidato com drift, duplicata semantica, no inexistente, pai e filho
   redundantes ou overlap KEEP/ASSOCIATION/DIFF sem justificativa explicita.

Gate de saida: nenhum plano e promovido se houver mudanca nao explicada ou se dois
candidatos diferirem em mais eixos do que a matriz de decisao declara.

## Fase 1 - Screening DIFF e reducao de nos

O lote `v561`-`v580` e util como screening porque isola DIFF por condicao. Na sessao de
execucao, ele deve ser revisado antes do envio, especialmente os oito arquivos com
overlap direto entre papeis e as celulas muito largas, como Gout com 260 codigos.

Ordem recomendada:

1. Separar os 20 isolamentos em tres classes por volume e risco.
2. Para cada celula com mais de 50 descendentes, criar uma versao reduzida baseada em
   nos mais especificos antes de aceitar a versao ampla.
3. Priorizar primeiro DIFF curto e clinicamente inequivoco, por exemplo celulas com
   2-15 codigos; usar as muito largas apenas como contraste de largura.
4. Interpretar o resultado contra o mesmo anchor:
   - melhora: promover o no e testar granularidade adjacente;
   - empate: guardar como hedge privado, sem declarar ganho;
   - queda de ate `0.00025`: near-neutral, manter apenas se a tese clinica for forte;
   - queda maior: retirar da linha principal e usar somente em candidato de alta
     variancia privada, se houver justificativa.
5. Depois do score, gerar follow-ups apenas para vencedores ou para divisao de um no
   amplo. Nao recombinar automaticamente todos os isolamentos.

## Fase 2 - Busca hierarquica no KEEP publico

O melhor publico veio de podas em COPD e combinacoes com Enlarged Mediastinum, mas as
rodadas recentes fizeram recombinacoes largas demais. A proxima busca deve operar na
arvore ICD:

1. Decompor o delta atual de COPD em subarvores removidas e mantidas.
2. Fazer group testing em 6-8 grupos clinicamente coerentes, seguido de split binario
   apenas nos grupos que melhorarem ou ficarem muito proximos do anchor.
3. Testar Enlarged Mediastinum e Epistaxis em matriz `2 x 2`, mantendo COPD constante,
   para medir interacao sem misturar hedges privados.
4. Reservar no maximo oito submissões por janela para este trilho. Se duas rodadas
   seguidas nao produzirem melhora, congelar o melhor eixo publico e deslocar quota
   para private/finais.
5. Exigir ganho de pelo menos `+0.00010` para promocao publica; empate so entra por
   diversidade ou por sustentar uma tese privada distinta.

Meta: produzir 3-5 candidatos publicos realmente distintos acima de `0.43156`, ou
demonstrar cedo que o teto publico local foi atingido e parar de gastar quota nele.

## Fase 3 - Curadoria privada por condicao

Criar uma `ConditionSpec` por cada uma das 23 condicoes, contendo:

- sinonimos e definicao clinica;
- nos KEEP essenciais, opcionais e excluidos;
- nos ASSOCIATION de complicacao, etiologia ou comorbidade forte;
- nos DIFF de apresentacao semelhante e causa diferente;
- nivel de confianca por no;
- quantidade de descendentes no dicionario;
- fonte ou justificativa clinica;
- overlap entre papeis e motivo para mante-lo, quando inevitavel.

Metodo de curadoria:

1. Calibrar o rubric no Train e confirmar que ele recupera os nos minimos registrados
   em `reports/train-gold-minimal-nodes.md`.
2. Fazer tres passes independentes de curadoria e promover um no para `narrow` apenas
   quando houver consenso forte e granularidade defensavel.
3. `balanced` pode adicionar nos de confianca media; `broad` fica reservado a hedges de
   alta variancia e nunca vira default.
4. ASSOCIATION e DIFF devem ter, por padrao, no maximo tres intencoes clinicas por
   celula. Excecoes exigem explicacao e contraste de largura.
5. Evitar codigos repetidos entre KEEP, ASSOCIATION e DIFF. Overlap deve ser um sinal
   de revisao, nao apenas um warning operacional.
6. Priorizar primeiro as condicoes que hoje concentram risco ou volume: CKD, Diabetes,
   Pneumonia, UTI, Heart Failure, Gout, Hematemesis e os grupos de tireoide/paratireoide.

Entregaveis desta fase para a outra sessao:

- especificacao clinica versionada;
- relatorio de expansao por no;
- score offline no Train para validar o metodo;
- 6 candidatos `narrow`, 6 `balanced` e no maximo 4 `broad` para composicao.

## Fase 4 - Desenho das submissões diarias

Distribuicao recomendada de uma janela completa de 20, adaptavel pelos resultados:

| Bloco | Slots | Funcao |
|---|---:|---|
| Publico controlado | 6 | Podas hierarquicas KEEP e interacoes curtas |
| Private narrow | 6 | Uma ou duas celulas de alta confianca por candidato |
| Private balanced | 4 | Combinar vencedores sem aumentar demais o volume |
| Follow-ups | 2 | Refinar apenas sinais da janela anterior |
| Finais/controles | 2 | Materializar candidatos elegiveis e preservar anchors |

Regras:

- Os dois primeiros slots de cada janela devem ser os candidatos com maior valor de
  informacao, caso a Kaggle permita apenas envio parcial.
- Nenhuma janela deve ter 20 variantes do mesmo eixo.
- Nao gastar os 20 slots so porque a cota existe. Um candidato sem hipotese nova e
  pior que uma bala preservada.
- A contingencia diaria so entra quando o primario nao estiver pronto e depois de
  revisar overlap, volume e matriz de decisao.
- Cada score deve atualizar o ledger antes de gerar a proxima rodada.

## Calendario proposto

### 10/07 - Diagnostico DIFF

- Revisar e, se aprovado, executar o screening DIFF em versoes curtas e amplas.
- Medir o degrau de score por celula.
- Comecar a `ConditionSpec` das oito condicoes prioritarias.

### 11/07 - KEEP hierarquico

- Substituir o fallback de podas soltas por group testing em COPD, Mediastinum e
  Epistaxis.
- Levar apenas os melhores DIFF da vespera para follow-up.
- Materializar os primeiros candidatos private `narrow`.

### 12/07 - ASSOCIATION calibrada

- Testar ASSOCIATION com nos menores que os usados em 09/07.
- Comparar `narrow` contra `balanced` por condicao, sem DIFF no mesmo arquivo.
- Atualizar os candidatos finais, removendo concentracao desnecessaria em Epistaxis.

### 13/07 - Private KEEP

- Auditar e testar KEEP nas condicoes de maior volume.
- Separar poda de familia errada de adicao de familia ausente.
- Combinar apenas mudancas que venceram isoladamente ou que tenham tese privada forte.

### 14/07 - Hibridos identificaveis

- Cruzar o melhor eixo publico com os melhores `narrow` e `balanced`.
- Criar pares que diferem em um unico bucket para estimar interacoes.
- Congelar qualquer eixo com duas rodadas sem sinal.

### 15/07 - Ensaio do portfolio final

- Gerar e auditar a selecao 20/20.
- Medir distancia por celula, condicao, papel e conjunto de codigos.
- Submeter qualquer finalista ainda nao materializado.
- Deixar pronta a selecao na Kaggle, sem depender de geracao no ultimo dia.

### 16/07 - Fechamento

- Usar a janela apenas para correcoes finais de alto sinal e para garantir que todos os
  candidatos escolhidos estejam elegiveis.
- Encerrar exploracao ate 06:00 BRT.
- Rodar auditoria final, selecionar os 20 e confirmar antes de 08:30 BRT, mantendo
  margem para o deadline de 08:59 BRT.

## Portfolio final alvo

O desenho inicial dos 20 slots deve ser:

| Papel | Slots | Criterio |
|---|---:|---|
| Anchors | 2 | Melhor publico puro e hedge privado conservador |
| Publicos otimizados | 5 | Melhores scores com mutacoes diferentes |
| Private narrow | 5 | Alta confianca, baixo volume e papeis limpos |
| Private balanced | 4 | Cobertura clinica moderada em dominios distintos |
| Hibridos | 2 | Melhor publico + melhor tese privada |
| Alta variancia | 2 | Broad controlado, para upside privado |

Gates da selecao:

- nenhum bucket especulativo presente em mais de 6/20 slots;
- pelo menos 10 condicoes nao public-anchor representadas no conjunto;
- pelo menos 4 estrategias com DIFF, se o screening nao mostrar dano sistematico;
- pelo menos 4 estrategias sem ASSOCIATION;
- no maximo 8 slots com a mesma assinatura de condicoes alteradas;
- todos os candidatos dentro de `0.00325` do melhor publico, exceto ate quatro hedges
  privados protegidos e justificados;
- auditoria sem drift, duplicata, no invalido ou overlap nao revisado.

## Criterios de parada e mudanca de rota

- Se uma familia causar queda acima de `0.00100` em dois contrastes controlados,
  bloquea-la no trilho publico.
- Se um eixo nao melhorar em duas janelas, congelar o melhor representante.
- Se ASSOCIATION ou DIFF amplo continuar caindo, reduzir granularidade; nao concluir
  automaticamente que o bucket inteiro e vazio.
- Se o private `broad` dominar o portfolio por volume, substituir por versoes narrow
  antes de criar novos combos.
- Se a selecao continuar com mais de 10 slots concentrados na mesma mutacao, priorizar
  diversidade mesmo com pequeno custo publico controlado.

## Execucao em outra sessao

O JV deve abrir uma nova sessao e pedir a execucao deste documento. A ordem inicial e:

1. Ler `PLANO_AVANCO.md`, `README.md`, `ESTRATEGIA.md`, `SUBMIT_QUEUE.md`,
   `PLAN_TOMORROW.md` e o ultimo scorecard.
2. Consultar status, cota, leaderboard, notebooks publicos e deadline sem submeter.
3. Auditar semanticamente `v561`-`v580` e propor quais variantes devem ser reduzidas,
   mantidas ou substituidas.
4. Criar o ledger de hipoteses e as primeiras `ConditionSpec`.
5. Montar um plano primario para a data corrente e apresentar o resumo pre-submit.
6. Somente depois do aceite explicito do JV, executar submissões e atualizar a
   documentacao.

Prompt curto sugerido para a nova sessao:

> Execute o `PLANO_AVANCO.md` da CohortX Task 3. Comece pelos controles e pela auditoria
> do plano da janela atual. Antes de qualquer submissao, mostre o lote primario, os
> contrastes, os riscos e o que ele substitui da contingencia.

## O que nao fazer

- Nao enviar automaticamente `v561`-`v820` apenas porque os fallbacks estao prontos.
- Nao tratar empate publico como validacao privada.
- Nao promover ASSOCIATION/DIFF amplo sem reducao de nos e contraste de granularidade.
- Nao usar score de candidatos com varios eixos mudados para atribuir causalidade.
- Nao chegar ao dia 16 com finalistas ainda nao submetidos.
- Nao trocar a selecao final por score apenas; a competicao permite 20 escolhas para
  cobrir incerteza privada, e essa opcao deve ser usada deliberadamente.
