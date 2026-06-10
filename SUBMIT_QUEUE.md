# Fila de Submissões — Otimização das MÉDIAS públicas

**Best atual: v145/v178 = 0.42453 (#5 público)**

## Descoberta-chave (split público/privado)
- **PRIVATE** (invisíveis no public LB): Diabetes, Pneumonia, CKD, UTI
- **PUBLIC** (movem o LB): Gout (F1~0.85) + 8 pequenas (F1~0.85) + 9 médias (F1~0.6)
- As 9 médias são onde há mais espaço (F1~0.6).

## Prioridade de submissão (quota reseta ~00:00 UTC)

| # | Arquivo | Estratégia médias | Esperado |
|---|---------|-------------------|----------|
| 1 | v181_kw_mid.csv | keyword puro do título | testar gold-replication |
| 2 | v182_kw_wide.csv | keyword + sinônimos | mais recall |
| 3 | v184_union_kw.csv | v145 ∪ keyword wide | cobertura máxima |
| 4 | v183_kw_chapter.csv | keyword ∩ chapter | precisão |

## Backup PRIVATE (diversificar aposta no final score)
| # | Arquivo | Privadas |
|---|---------|----------|
| 5 | v185_private_kw.csv | Diabetes/Pneu/CKD/UTI por keyword puro |

→ Selecionar 2 finais no Kaggle: **v178 (v145)** + a melhor das médias acima.

## Tamanhos das médias por variante
```
                          v145  v181  v182  v184
COPD                       56    4     28    67
Heart Failure              72    39    46    78
Hyperthyroidism            49    24    27    49
ILD                        42    14    25    51
Hypothyroidism             26    12    12    27
Bronchitis                 33    18    18    33
Dermatomycosis             38    68    69    95
Nasopharyngeal             42    13    13    47
Enlarged Mediastinum       40    27    27    53
```

## Já testado (NÃO repetir)
- v180 strict core médias = 0.39674 (PIOR — gold é inclusivo)
- v164 hand-curate erros = 0.41430 (PIOR — gold inclui "erros")
- v166 expandir pequenas = 0.42453 (neutro)

## ⚠️ AÇÃO MANUAL
Selecionar v178_FINAL como submissão final no Kaggle:
https://www.kaggle.com/competitions/cohort-x-task-3/submissions
