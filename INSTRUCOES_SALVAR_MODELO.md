# 🎯 COMO SALVAR O MODELO XGBOOST CORRETAMENTE

## ⚠️ Problema Atual
O arquivo `model_rossmann_xgb_tuned.pkl` contém um DataFrame de resultados, não o modelo treinado.

## ✅ Solução - 3 Opções

### OPÇÃO 1: Adicionar célula no final do notebook (RECOMENDADO)

Adicione esta célula **DEPOIS** da célula que treina o modelo (linha ~4614):

```python
# =================================================================
# SALVAR MODELO TREINADO
# =================================================================
import pickle
import os

# Caminho para salvar o modelo
model_path = '../model/model_rossmann_xgb_tuned.pkl'

# Garantir que model_xgb existe e foi treinado
# Execute esta célula APÓS ter treinado o modelo

# Verificar se model_xgb existe
if 'model_xgb' in locals() or 'model_xgb' in globals():
    # Salvar APENAS o modelo (não o DataFrame de resultados!)
    with open(model_path, 'wb') as f:
        pickle.dump(model_xgb, f)
    print(f"✅ Modelo salvo em: {model_path}")
    print(f"Tipo do objeto salvo: {type(model_xgb)}")
else:
    print("❌ Erro: model_xgb não encontrado.")
    print("   Execute primeiro a célula que treina o modelo XGBoost")
```

### OPÇÃO 2: Executar manualmente no terminal do Notebook

Depois de treinar o modelo, execute no terminal do Jupyter:

```python
# No terminal do Jupyter
import pickle

# Salvar o modelo treinado
with open('../model/model_rossmann_xgb_tuned.pkl', 'wb') as f:
    pickle.dump(model_xgb, f)
    
print("Modelo salvo!")
```

### OPÇÃO 3: Criar script Python separado

Crie um arquivo `Notebook/fix_model.py` com:

```python
import pickle
import sys
import os

# Adicione o diretório ao path para importar dados
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# AQUI você precisa treinar o modelo novamente ou carregar do notebook
# Como alternativa, use este código no notebook:

"""
# Cole este código em uma célula no notebook:

# Treinar modelo
model_xgb = xgb.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=param_tuned['n_estimators'],
    eta=param_tuned['eta'],
    max_depth=param_tuned['max_depth'],
    subsample=param_tuned['subsample'],
    colsample_bytree=param_tuned['colsample_bytree'],
    min_child_weight=param_tuned['min_child_weight']
).fit(x_train, y_train)

# Salvar modelo
with open('../model/model_rossmann_xgb_tuned.pkl', 'wb') as f:
    pickle.dump(model_xgb, f)
    
print("Modelo salvo com sucesso!")
"""

print("Execute o código acima no notebook")
```

## 🚀 Depois de Salvar o Modelo

1. **Verifique** que o modelo foi salvo:
```python
import pickle
model = pickle.load(open('../model/model_rossmann_xgb_tuned.pkl', 'rb'))
print(type(model))  # Deve ser <class 'xgboost.core.Booster'> ou similar
print(hasattr(model, 'predict'))  # Deve ser True
```

2. **Atualize o handler.py** para carregar o modelo real (remover DummyModel):
```python
# Substituir DummyModel por:
model = pickle.load(open(model_path, 'rb'))
```

3. **Teste a API**:
```bash
cd api
python handler.py
# Em outro terminal:
curl -X POST http://localhost:5000/rossmann/predict \
  -H "Content-Type: application/json" \
  -d '{"Store": 1, "DayOfWeek": 5, "Date": "2015-07-31", ...}'
```

4. **Deploy no Heroku**:
```bash
git add model/model_rossmann_xgb_tuned.pkl api/handler.py
git commit -m "Adicionar modelo XGBoost treinado"
git push heroku main
```

## ⚡ Ação Rápida

No seu notebook Jupyter, adicione esta célula **AGORA**:

```python
# Salvar modelo treinado (execute APÓS treinar o modelo)
if 'model_xgb' in locals():
    import pickle
    pickle.dump(model_xgb, open('../model/model_rossmann_xgb_tuned.pkl', 'wb'))
    print("✅ Modelo salvo!")
else:
    print("Execute primeiro o treinamento do modelo")
```


