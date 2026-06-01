# Plano para amanha (apos quota Gemini resetar)

## Quota reset
- Google Gemini free tier reseta diariamente.
- Esperado: ~24h apos esgotar (~16:43 BRT hoje), logo ~16:43 amanha estara disponivel.

## Estado do codigo (pronto para rodar)
- `src/v42_gemini_pro.py` esta configurado com `gemini-flash-latest` (Pro deu rate limit duro). 
- Para Pro tentar, editar `MODEL = "gemini-2.5-pro"` e `SLEEP_BETWEEN = 6` (mais cauteloso).
- `.env` ja tem GEMINI_API_KEY.

## Comandos
```bash
cd ~/Documents/GitHub/cohort-x-task-3

# Confirmar que Gemini volta:
curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H "X-goog-api-key: $GEMINI_API_KEY" -X POST \
  -d '{"contents":[{"parts":[{"text":"hello"}]}]}'

# Rodar com Pro (mais lento mas mais inteligente):
sed -i '' 's|gemini-flash-latest|gemini-2.5-pro|; s|SLEEP_BETWEEN = 1|SLEEP_BETWEEN = 6|; s|TOP_N = 400|TOP_N = 500|' src/v42_gemini_pro.py
nohup .venv/bin/python -u src/v42_gemini_pro.py > /tmp/v47_log.txt 2>&1 &

# Aguardar (Pro ~90min com 6s sleep). Depois submeter:
kaggle competitions submit -c cohort-x-task-3 -f submissions/v47_*.csv -m "v47: Gemini 2.5 Pro classifier"
```

## Estrategia
1. **v47** = Gemini Pro com TOP_N=500 (mais candidatos, modelo melhor) - alvo 0.45+
2. **v48** = UNION v33 + v47 - se Pro adicionar codigos novos
3. **v49** = INTERSECT v33 ∩ v47 - se queremos alta precisao
4. **v50** = v33 KEEP + ASSOC/DIFF preenchidos pelo Gemini Pro (testar se Pro identifica corretamente quando preencher vs vazio)

## Tambem testar
- `gemini-pro-latest` (canary do Pro mais recente)
- `gemini-2.5-flash` (estavel, melhor que Flash latest)

## Baselines confirmados
- v33 (retrieval) = 0.36565 (best)
- baseline empty (v15) = 0.222
- v41b (Flash) = 0.316
- LLM 7B local = 0.286-0.296
