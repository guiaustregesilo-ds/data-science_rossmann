# Setup para Deploy no Heroku

## Comandos para deploy:

```bash
# 1. Login no Heroku
heroku login

# 2. Criar aplicação no Heroku (execute uma vez)
heroku create nome-da-sua-app

# 3. Enviar código para o Heroku
git add .
git commit -m "Preparação para deploy"
git push heroku main

# 4. Verificar logs
heroku logs --tail
```

## Estrutura de arquivos necessários:

- ✅ `Procfile` - Define como rodar a aplicação
- ✅ `requirements.txt` - Dependências Python
- ✅ `runtime.txt` - Versão do Python
- ✅ `.gitignore` - Arquivos ignorados pelo Git

## Importante:

- Certifique-se de que todos os arquivos `.pkl` na pasta `parameter/` e `model/` estejam commitados
- A API estará disponível em: `https://nome-da-sua-app.herokuapp.com/rossmann/predict`

## Testar localmente antes de deploy:

```bash
cd api
python handler.py
```

Depois teste com:
```bash
curl -X POST http://localhost:5000/rossmann/predict \
  -H "Content-Type: application/json" \
  -d @test_data.json
```


