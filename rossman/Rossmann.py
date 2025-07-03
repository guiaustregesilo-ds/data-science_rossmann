import pickle
import pandas as pd
from   flask            import Flask, request, Response
from   rossman.Rossmann import Rossmann

# Loading model
model = pickle.load(open('C:/Users/Guilherme/Documents/repos/DS em Produção/model/model_rossmann_xgb_tuned.pkl', 'rb'))

# Initialize API
app = Flask(__name__)

@app.route("/rossmann/predict", methods=['POST'])
def rossman_predict():
    test_json = request.get_json()

    if test_json: # there is data
        if isinstance( test_json, dict): # unique example
            test_raw = pd.DataFrame (test_json, index=[0])

        else: # multiple examples
            test_raw = pd.DataFrame(test_json, columns=test_json.keys())

        # Instantiate Rossmann class
        pipeline = Rossmann()

        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        # feature engineering
        df2 = pipeline.feature_engineering(df1)

        # data preparation
        df3 = pipeline.data_preparation(df2)

        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df3)

        return df_response

    else:
        return Response('{}', status=200, mimetype='application/json')

    df1 = pd.DataFrame(test_json)
    df2 = pipeline_data_preparation.transform(df1)
    df3 = pipeline_modeling.transform(df2)

if __name__ == "__main__":
    app.run('127.0.0.1', port=5000, debug=True)