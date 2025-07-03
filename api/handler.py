import pickle
import pandas as pd
from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann

# Load model
model = pickle.load(open('C:/Users/Guilherme/Documents/repos/DS em Produção/model/model_rossmann_xgb_tuned.pkl', 'rb'))

# Initialize API
app = Flask(__name__)

@app.route('/rossmann/predict', methods=['POST'])
def rossmann_predict():
    test_json = request.get_json()

    if test_json:
        # Caso seja apenas um exemplo
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # Pipeline de previsões
        pipeline = Rossmann()

        # Etapas de preparação
        df1 = pipeline.data_cleaning(test_raw)
        df2 = pipeline.feature_engineering(df1)
        df3 = pipeline.data_preparation(df2)

        # Previsão
        df_response = pipeline.get_prediction(model, test_raw, df3)

        # Retorno da API
        return Response(df_response, status=200, mimetype='application/json')

    else:
        return Response("{}", status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
