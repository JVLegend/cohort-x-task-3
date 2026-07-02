# Estrategia CohortX Task 3 - Revisao 2026-07-01

Tags: #JoaoVictor #Kaggle #Academia #Tecnologia

Documento de estrategia (fonte da verdade do "o que fazer"). Os docs operacionais
(`OPERACAO_DIARIA.md`, `SUBMIT_QUEUE.md`, `PLAN_TOMORROW.md`) descrevem o "como
enviar". Este descreve "no que gastar as balas".

## Revisao 2 (2026-07-01, tarde) - o que os dados provam, nao so a intuicao

Tres achados novos, todos verificados direto em `data/Task_3.xlsx` (aba Train) e
`data/icd_dict.csv`. Ver o loop de feedback offline em `src/train_scorer.py`.

**Achado 1 - o gold e determinístico: escolher o NO ICD certo, expandir todos os
descendentes.** Para cada raiz presente no gold do Train, `gold == {todos os codigos
do dicionario que comecam com aquele no}`. Confirmado em 55/55 (H65), 117/117 (I63),
231/231 (T17), etc. A "inteligencia" nao esta em escolher codigos avulsos; esta em
escolher os NOS certos. A expansao e mecanica.

**Achado 2 - a granularidade do no importa muito, e nem sempre e 3-char.** O gold
mistura niveis. Aortic ASSOC usa `A50` inteiro (38 codigos) mas so `A539` e `M352`
(Marfan) - nao `A53`/`M35` cheios. Stroke ASSOC usa so `H340`+`H341` (10 de 63 codigos
de H34). SOB DIFF usa `T180` (4 de 66). Medido no `train_scorer`: expandir a familia
3-char cheia em vez do no curado derruba Aortic ASSOC de 1.000 para **0.748** e Stroke
ASSOC de 1.000 para **0.274**. Super-expandir mata a precisao. Regra pratica: escolher
o no mais especifico que ainda cobre a intencao clinica, nao o capitulo inteiro.

**Achado 3 - preencher ASSOC/DIFF NAO e de graca; e uma aposta por celula.** A metrica
e set-F1 por celula: celula vazia com predicao vazia = F1 **1.0** (ja embolsado hoje).
No Train, 4 das 10 celulas ASSOC/DIFF (40%) tem gold VAZIO (Ischemic HD ambos, Stroke
DIFF, SOB ASSOC). Se voce preenche uma celula cujo gold e vazio, cai de 1.0 para 0.0.
Logo, encher ASSOC/DIFF em TODAS as condicoes privadas em bloco e provavelmente EV
negativo. A decisao correta e por (condicao, bucket): so preencher onde a ligacao
clinica e forte e obvia; deixar vazio e a resposta certa em ~40% dos casos. Acertar o
no certo numa celula grande vale F1=1.0 = +1/69 ~ +0.0145 no macro; e alto retorno,
mas so quando a curadoria acerta o no E a granularidade.

**Consequencia operacional - o loop de feedback grátis (`src/train_scorer.py`).** Ate
agora, toda ideia custava uma bala do Kaggle. Existe gold local para 5 condicoes x 3
buckets. O scorer reproduz a metrica oficial (self-check = 1.0000). Fluxo novo:
curar nos -> pontuar offline no Train -> so submeter o que ja provou a regra de
expansao/granularidade. Balas do Kaggle passam a confirmar apostas privadas, nao a
descobrir se o recipe presta.

## TL;DR

1. **Achado principal:** a premissa que sustenta toda a operacao das ultimas semanas
   esta errada. A operacao assume que `ASSOCIATION` e `DIFF` do gold sao vazios e por
   isso preenche `Not Applicable` nas 23 condicoes. A aba **Train** do proprio
   `data/Task_3.xlsx` mostra o contrario: em 6 dos 10 pares ASSOC/DIFF dos exemplos
   rotulados o gold esta **populado** com familias ICD coerentes. Voce esta zerando
   cerca de dois tercos do espaco de rotulos (ASSOC e DIFF = 46 das 69 celulas).
2. **Por que passou batido:** no public split, as condicoes visiveis (COPD e Enlarged
   Mediastinum) parecem ter ASSOC/DIFF vazios, entao todo probe que preencheu ASSOC/DIFF
   caiu no publico. A licao tirada foi "gold nao tem ASSOC/DIFF". A licao correta e
   "preencher ASSOC/DIFF ERRADO cai; as condicoes que decidem o PRIVATE estao invisiveis".
3. **O que mudar:** parar de gastar 20 balas/dia lapidando COPD + Enlarged Mediastinum
   (2 de 23 condicoes, ganho maximo de milesimos) e redirecionar quota para popular
   ASSOC/DIFF nas condicoes invisiveis no publico, que e onde o private score e decidido.
4. **Alavanca ja disponivel:** o proprio README lista "LLM grande sem rate limit" como o
   que faltou para top-3. Isso esta disponivel agora. A curadoria pode ser feita por LLM
   e congelada num arquivo estatico (dicionario Python), o que continua sendo offline e
   reproduzivel - exatamente o que o host exige.

## Onde voce esta (estado real)

- Public best: `0.42453`, rank #9/112. Estavel ha semanas (plateau real).
- Topo do publico: #1 `1.00000` (provavel gabarito/host), #2 `0.75416`, #3 `~0.51`.
  Alvo realista e a faixa 0.45-0.55 (top 3-5), nao o 1.0.
- A metrica e macro-F1 sobre 3 categorias x 23 condicoes = 69 celulas. Baseline "tudo
  vazio" da ~0.222 (registro historico), o que implica que a maioria das celulas tem gold
  nao vazio. Hoje voce so disputa a coluna KEEP (23 celulas) e concede ASSOC+DIFF.
- Infra operacional: madura demais para o retorno. `cohortx_ops.py` tem ~67 KB de
  guards, preflight, contingencia, reserva e retries de cron. Isso e robusto, mas nao
  move score. O gargalo nunca foi orquestracao; foi modelagem. (Regra 2: simplicidade.)

## O erro estrategico central: ASSOC e DIFF concedidos

Evidencia direta da aba Train (gold real, 5 exemplos):

| Exemplo | ASSOCIATION (familias) | DIFF (familias) |
|---|---|---|
| URTI | H65, H66 (otite media) | J12-J22, J40 (pneumonia/bronquite) |
| Aortic Aneurysm | A50, A53 (sifilis), M35 (tec. conjuntivo) | I21 (IAM), I63 (AVC) |
| Ischemic Heart Disease | vazio | vazio |
| Stroke | H34 (oclusao retiniana) | vazio |
| Shortness of Breath | vazio | R53, T17, T18 (fraqueza/corpo estranho) |

Padrao clinico claro e aprendivel:
- **ASSOCIATION** = complicacoes, sequelas, agentes etiologicos e comorbidades fortemente
  ligadas (URTI -> otite media; aneurisma -> sifilis, Marfan/tec. conjuntivo).
- **DIFF** = diagnosticos diferenciais, quadros de apresentacao parecida e causa diferente
  (URTI -> pneumonia; aneurisma -> IAM/AVC; dispneia -> corpo estranho/fraqueza).

Consequencia numerica (estimativa, rotulada como estimativa): dos 46 pares ASSOC/DIFF, se
~60% forem nao vazios como no train (~27 celulas), hoje voce marca F1=0 em todas elas. Se
metade delas chegar a F1~0.5, isso vale por volta de +0.05 a +0.10 no macro-F1 - uma ordem
de grandeza acima dos milesimos que os probes de COPD perseguem. Numero a confirmar por
submissao; nao usar como fato.

Por que os probes antigos (v47 KEEP=ASSOC=0.310, v48 KEEP=DIFF=0.203) cairam: preencheram
ASSOC/DIFF com os codigos de KEEP (errado) e em TODAS as condicoes, inclusive as visiveis
no publico cujo gold ASSOC/DIFF e vazio. Preencher errado e pior que vazio. Isso nao prova
que o gold e vazio; prova que o conteudo estava errado e no lugar errado.

## Segundo lever: granularidade de KEEP

O gold KEEP do train e generoso: Stroke = 526 codigos em 11 familias; URTI = 152 em 21
familias (inclui ate B97 agentes virais). O gold agrupa a familia clinica inteira ate os
codigos terminais. Isso valida a expansao por prefixo que voce ja usa, mas sugere que
condicoes pequenas do seu set podem estar ESTREITAS demais (Epistaxis 8, Thyroiditis 10,
Hyperparathyroidism 8, Hematemesis 11). Revisar se cobrem a familia inteira + agentes/
sequelas obvios. Ao mesmo tempo, condicoes grandes e invisiveis (Diabetes 418, Gout 164,
Pneumonia 115, CKD 94, UTI 91) podem estar incluindo familias erradas (ex.: Diabetes com
O24/Z/P alem de E08-E13) e derrubando precisao no private sem aparecer no publico.

## Terceiro lever: parar de overfitar o publico

- Só COPD e Enlarged Mediastinum mexem no publico. Lapidar essas duas com 20 balas/dia
  otimiza 2 de 23 condicoes e da zero sinal sobre as 21 que decidem o private.
- "Public-neutro = hedge privado seguro" e um pressuposto NAO testado. As mudancas
  invisiveis no publico podem ajudar OU atrapalhar o private; hoje voce acumula hedges as
  cegas (ver `reports/final-candidates.md`, com 18/20 finais sendo hedges public-neutros
  quase identicos - baixa diversidade, cobre pouca variancia privada).
- Manter no maximo 2-4 balas/dia para probes publicos de COPD/Mediastinum. O resto vai
  para o experimento de ASSOC/DIFF e correcao de familias KEEP.

## Plano revisado

### Fase A - Experimento ASSOC/DIFF (proximas 1-2 janelas, baixo risco, alto upside)

Objetivo: adicionar ASSOC/DIFF sem custo no publico e ganhar no private.

Passo 0 (offline, bloqueante, zero balas): calibrar o recipe no `src/train_scorer.py`.
Escrever um spec de nos para as condicoes do Train e confirmar que a regra
expandir-descendentes na granularidade certa bate o gold (alvo: macro perto de 1.0 nas
celulas nao vazias). So depois disso vale gastar bala.

Design que isola o efeito e protege o publico:
1. Base = `v178_FINAL.csv`.
2. Preencher ASSOC/DIFF **seletivamente**, por (condicao, bucket), so onde a ligacao
   clinica e forte e obvia (ver Achado 3: encher em bloco e EV negativo porque ~40% das
   celulas tem gold vazio e ja valem F1=1.0). Deixar COPD e Enlarged Mediastinum vazios
   (o publico indica gold vazio la). Deixar vazio tambem toda condicao onde nao ha
   ASSOC/DIFF clinicamente inequivoco.
3. Curar na granularidade do no, nao do capitulo: preferir o no mais especifico que
   cobre a intencao (ex.: `M352` Marfan, nao `M35`; `H340`/`H341`, nao `H34`). Validar
   cada no candidato contra os analogos do Train no scorer.
4. Enviar em lotes que isolam o sinal, cada um sobre `v178_FINAL`:
   - Lote A: só DIFF preenchido (conds selecionadas).
   - Lote B: só ASSOC preenchido (conds selecionadas).
   - Lote C: ASSOC + DIFF juntos (conds selecionadas).
5. Leitura: se o publico permanecer `0.42453`, esta confirmado custo publico zero e o
   candidato vira aposta privada forte. Se cair, alguma dessas condicoes nao era tao
   invisivel; reverter aquela familia.

Curadoria (offline, reproduzivel): mapear por condicao as familias ASSOC e DIFF (tabela
seed abaixo), depois expandir cada familia para todos os codigos descendentes em
`data/icd_dict.csv`. A escolha das familias e feita por LLM/curadoria clinica e congelada
num dict Python versionado. Nada roda online no pipeline final.

### Fase B - Correcao de familias KEEP

- Auditar condicoes grandes e invisiveis (Diabetes, Gout, Pneumonia, CKD, UTI, Heart
  Failure) por familia: manter a familia core, remover familias fora do escopo clinico.
- Auditar condicoes pequenas (Epistaxis, Thyroiditis, Hyperparathyroidism, Hematemesis)
  para cobertura completa da familia + sequelas obvias, seguindo a granularidade do train.
- Testar cada correcao. Nas invisiveis, a leitura e private (public-neutro esperado).

### Fase C - Selecao final diversificada

Trocar os 18 hedges quase identicos por candidatos genuinamente diversos, para cobrir a
variancia do private:
1. `v178_FINAL` (ancora publica).
2. v178 + ASSOC/DIFF populado (private conds) - a aposta principal nova.
3. KEEP com familias corrigidas.
4. Uma versao keyword-pure.
5. Combinacoes das anteriores.
Manter 1-2 slots para o melhor probe publico de COPD/Mediastinum, se algum superar 0.42453.

## Tabela seed ASSOC/DIFF (curadoria inicial, revisar antes de submeter)

Famílias propostas por condicao. Expandir cada uma para os descendentes no dicionario.
COPD e Enlarged Mediastinum ficam vazias de proposito (public movers).

| Condicao | ASSOCIATION (familias) | DIFF (familias) |
|---|---|---|
| Epistaxis | D68, D69 (coagulopatia), I10 (HAS) | R58, K920 (hemorragia GI) |
| Intracranial Pressure | G91 (hidrocefalia), H47 (papiledema) | G43/R51 (cefaleia), C71/D33 (tumor) |
| Chronic Obstructive Pulmonary Disease | (vazio - public mover) | (vazio - public mover) |
| Enlarged Mediastinum | (vazio - public mover) | (vazio - public mover) |
| Gout | E79 (hiperuricemia), N18 (DRC) | M00 (artrite septica), M11 (condrocalcinose), M05/M06 (AR) |
| Latent Adrenal Insufficiency | E31 (poliendocrino), E03 (hipotireoid) | E86/R53 (fadiga/desidratacao) |
| Dermatomycosis | B37 (candidiase), E11 (diabetes) | L40 (psoriase), L20-L30 (eczema) |
| Pleurisy | J90, J91 (derrame pleural), A15 (TB) | J18 (pneumonia), I26 (TEP) |
| Bronchitis | J44 (COPD) | J18 (pneumonia), J45 (asma) |
| Thyroiditis | E03 (hipo), E05 (hiper) | E04 (bocio) |
| Nasopharyngeal Carcinoma | B27 (EBV), C77 (mets linfonodo) | C10/C14 (outros faringe), J33 (polipo) |
| CKD | I12/I13 (HAS renal), E112 (nefropatia DM), D63 (anemia) | N17 (IRA) |
| Hypothyroidism | E06 (tireoidite), E01/E04 (bocio) | E05 (hiper) |
| Hematemesis | K25-K27 (ulcera), I85 (varizes), K29 (gastrite) | K921 (melena), R042 (hemoptise) |
| Heart Failure | I42 (miocardiopatia), I48 (FA), N18 (DRC) | J44 (COPD), I26 (TEP) |
| Hypergonadism | (incerto - deixar vazio ate curar) | (incerto - deixar vazio ate curar) |
| UTI | N10/N12 (pielonefrite), A41 (sepse) | N30 (cistite), N34 (uretrite), N76 (vaginite) |
| Diabetes | E112-E116 (complicacoes), E66 (obesidade) | E10/E13 (outros DM), R73 (glicemia alterada) |
| Interstitial Lung Disease | M35 (tec. conjuntivo), D86 (sarcoidose) | J18 (pneumonia), I50 (IC) |
| Hypoparathyroidism | E835 (hipocalcemia) | E21 (hiperpara), E55 (def. vit D) |
| Hyperparathyroidism | E835 (hipercalcemia), N25 (osteodistrofia renal) | E20 (hipopara), C-malignidade hipercalcemia |
| Hyperthyroidism | E06 (tireoidite), I48 (FA) | E03 (hipo), F41 (ansiedade) |
| Pneumonia | A41 (sepse), J90 (derrame), J96 (insuf. resp.) | J20/J40 (bronquite), A15 (TB), C34 (ca pulmao), I50 (IC) |

## Riscos e ressalvas

- Estimativa de +0.05 a +0.10 e teorica; so a submissao confirma. Nao anunciar como fato.
- Preencher ASSOC/DIFF errado e pior que vazio. Curar com cuidado e testar por lote.
- O experimento e uma aposta PRIVADA: o public LB nao vai confirmar o ganho. Confie no
  design (custo publico zero) + coerencia clinica, nao no numero publico.
- Nao mexer em ASSOC/DIFF de COPD e Enlarged Mediastinum (gold provavelmente vazio la).
- Manter a solucao final offline/reproduzivel: curadoria por LLM vira arquivo estatico. O
  forum (auditado via `reports/2026-07-02-intel.md`) permite modelos Hugging Face
  baixaveis e dados CC/Public Domain, mas veta APIs online/dados proprietarios no
  processamento e cita servidor de 15 GB RAM como alvo pratico.

## Proximos passos concretos

1. (feito) `src/train_scorer.py`: loop de feedback offline contra o gold do Train.
   Self-check = 1.0000. Rodar `--self-check` para o teto e `--spec f.json` para calibrar.
2. Curar o dict de nos ASSOC/DIFF na granularidade certa e pontuar no scorer ANTES de
   gastar bala. So promover nos que reproduzem o padrao do Train.
3. (feito 2026-07-02) `src/v281_300_assoc_diff.py`: le o dict de nos curado, expande
   descendentes via `icd_dict.csv`, gera os lotes DIFF-only/ASSOC-only/ambos sobre o novo
   anchor publico `v209`, preenchendo so as condicoes selecionadas e preservando
   COPD/Mediastinum vazios.
4. (feito 2026-07-02) Validar com `cohortx_ops.py validate-plan` e deixar pronto para
   envio via o pipeline existente depois do reset (a infra de quota/dedupe/guard continua
   util - muda o CONTEUDO, nao o encanamento).
5. Ler o public de cada lote apos a janela de 2026-07-03: confirmar neutralidade publica
   dos probes privados antes de promover a final.
6. (feito 2026-07-02) Preparar paraquedas de quota para 2026-07-04:
   `src/v321_340_july4_contingency.py` + `plans/2026-07-04-public-contingency.csv`.
   Usar apenas se o adaptativo pos-score de `v293`-`v300` nao gerar
   `plans/2026-07-04.csv` a tempo.
7. (feito 2026-07-02) Preparar adaptativo pos-ASSOC/DIFF:
   `src/v301_320_post_assocdiff_followups.py` combina os probes `v281`-`v292` que forem
   public-neutral com o melhor KEEP publico de `v293`-`v300` e o hedge privado `v185`,
   gerando `plans/2026-07-04.csv` (`v301`-`v320`) quando os scores estiverem completos.
8. Rodar Fase B (familias KEEP) em paralelo nas balas restantes; usar o scorer para
   checar a granularidade das raizes KEEP curadas (Aortic/Stroke tem raizes nao-cheias).
9. (feito 2026-07-02) Reescrever `reports/final-candidates.md` com selecao diversificada
   (Fase C): anchor publico, hedge privado `v185`, promocao de ASSOC/DIFF public-neutral
   e filtro contra mutacoes KEEP-only grandes demais.
10. (feito 2026-07-02) Endurecer a operacao de cota apos duplicatas no historico Kaggle:
    cota segue as linhas brutas aceitas pelo servidor, o preflight mostra diagnostico de
    duplicatas e o `submit-plan` usa ledger local para nao repetir arquivo em retries.
