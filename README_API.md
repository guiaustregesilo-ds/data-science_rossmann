# API Rossmann - Instruções

## Status Atual ✅
- ✅ Status Code 200 - API funcionando
- ✅ Arquivos de parâmetro copiados corretamente
- ✅ Caminhos corrigidos para funcionar localmente e no Heroku
- ⚠️ **MODELO DUMMY** - Você precisa salvar o modelo XGBoost treinado corretamente

## Problema com o Modelo

O arquivo `model_rossmann_xgb_tuned.pkl` contém um DataFrame (resultados de métricas) em vez do modelo treinado XGBoost.

### Solução: Salvar o Modelo Corretamente

No seu notebook Jupyter, após treinar o modelo XGBoost, você precisa salvá-lo assim:

```python
import pickle

# Após treinar seu modelo (ex: model = xgboost.XGBRegressor())
# Treine seu modelo aqui...

# Salvar apenas o modelo treinado
with open('../model/model_rossmann_xgb_tuned.pkl', 'wb') as f:
    pickle.dump(model, f)

# NÃO salve DataFrames ou dicionários com métricas
```

## Como testar a API localmente

1. Certifique-se de que todos os arquivos estão na pasta correta:
   - `parameter/*.pkl` (5 arquivos de scaler)
   - `model/model_rossmann_xgb_tuned.pkl` (modelo XGBoost)

2. Inicie a API:
```bash
cd api
python handler.py
```

3. Faça uma requisição de teste (agora retorna Status 200):
```bash
curl -X POST http://localhost:5000/rossmann/predict \
  -H "Content-Type: application/json" \
  -d '{"Store": 1, "DayOfWeek": 5, "Date": "2015-07-31", "Open": 1, "Promo": 1, "StateHoliday": "0", "SchoolHoliday": 1, "StoreType": "a", "Assortment": "a", "CompetitionDistance": 1270.0, "CompetitionOpenSinceMonth": 9.0, "CompetitionOpenSinceYear": 2008.0, "Promo2": 0, "Promo2SinceWeek": null, "Promo2SinceYear": null, "PromoInterval": null}'
```

## Deploy no Heroku

Após salvar o modelo correto:

```bash
# 1. Adicionar arquivos ao git
git add parameter/*.pkl model/*.pkl api/ Procfile requirements.txt runtime.txt .gitignore

# 2. Commit
git commit -m "Preparação para deploy Heroku com modelo correto"

# 3. Criar app no Heroku (apenas uma vez)
heroku create nome-da-sua-app

# 4. Push
git push heroku main

# 5. Ver logs
heroku logs --tail
```

## Estrutura de Arquivos Necessários

```
DS em Produção/
├── api/
│   ├── handler.py          # Handler da API
│   └── rossmann/
│       ├── __init__.py
│       └── Rossmann.py     # Classe de processamento
├── parameter/
│   ├── competition_distance_scaler.pkl
│   ├── competition_time_month_scaler.pkl
│   ├── promo_time_week_scaler.pkl
│   ├── store_type_scaler.pkl
│   └── year_scaler.pkl
├── model/
│   └── model_rossmann_xgb_tuned.pkl  # MODELO XGBOOST (não DataFrame!)
├── Procfile
├── requirements.txt
├── runtime.txt
└── .gitignore
```

## Próximos Passos

1. **IMPORTANTE**: Salve o modelo XGBoost treinado corretamente (não o DataFrame de resultados)
2. Substitua o `DummyModel` no `handler.py` pelo modelo real
3. Teste novamente localmente
4. Faça o deploy no Heroku


