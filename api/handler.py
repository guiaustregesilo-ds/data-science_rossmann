import pickle
import pandas as pd
import numpy as np
import os
from   flask             import Flask, request, Response
from   rossmann.Rossmann import Rossmann

# loading model
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)  # Go up from api/ to root
model_path = os.path.join(root_dir, 'model', 'model_rossmann_xgb_tuned.pkl')

# Try to load the actual model
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    
    # Verify it's actually a model, not a DataFrame
    if not hasattr(model, 'predict'):
        raise ValueError("Loaded object is not a model (no predict method)")
    
    print(f"✅ Model loaded successfully: {type(model)}")
    
except Exception as e:
    print(f"⚠️  WARNING: Could not load model from {model_path}")
    print(f"   Error: {e}")
    print("   Using DummyModel - predictions will be inaccurate!")
    print("   See INSTRUCOES_SALVAR_MODELO.md for instructions")
    
    # Fallback to dummy model
    class DummyModel:
        def predict(self, X):
            import numpy as np
            return np.array([10000.0] * len(X)) if hasattr(X, '__len__') else np.array([10000.0])
    
    model = DummyModel()

# initialize API
app = Flask(__name__) 

@app.route('/rossmann/predict', methods=['POST'])
def rossmann_predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance(test_json, dict): # unique example 
            test_raw = pd.DataFrame(test_json, index=[0])
        else: # multiple examples
            test_raw = pd.DataFrame(test_json, columns=list(test_json[0].keys()))
        
        # Save original input for response
        original_data = test_raw.copy()
        
        # instantiate Rossmann class
        pipeline = Rossmann()
        
        # data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        
        # feature engineering
        df2 = pipeline.feature_engineering(df1)
        
        # data preparation
        df3 = pipeline.data_preparation(df2)
        
        # prediction - only if there is data to predict
        if not df3.empty:
            # Get predictions
            pred = model.predict(df3)
            
            # Convert to exp to get actual sales values
            predictions = np.expm1(pred).flatten()
            
            # Reset index and add predictions to original data
            original_data = original_data.reset_index(drop=True)
            
            # Assign predictions as a simple list/array
            original_data.insert(len(original_data.columns), 'prediction', predictions)
            
            # Convert to JSON
            df_response = original_data.to_json(orient='records', date_format='iso')
            return Response(df_response, status=200, mimetype='application/json')
        else:
            # Return empty response if all rows were filtered out
            return Response('[]', status=200, mimetype='application/json')
    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    import os
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port, debug=True)