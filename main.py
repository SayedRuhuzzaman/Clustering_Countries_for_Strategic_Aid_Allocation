# app/main.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for the entire app
CORS(app)

# Load model and scaler
model_path = '/Users/gopalmacbook/Downloads/Block 2 & 4/models/clustering_model.pkl'
scaler_path = '/Users/gopalmacbook/Downloads/Block 2 & 4/models/scaler.pkl'

km = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve data from request
    data = request.json
    try:
        features = np.array([[
            float(data['Child_mort']),
            float(data['Exports']),
            float(data['Health']),
            float(data['Imports']),
            float(data['Income']),
            float(data['Inflation']),
            float(data['Life_expec']),
            float(data['Total_fer']),
            float(data['Gdpp'])
        ]])
    except KeyError as e:
        return jsonify({'error': f'Missing data field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid data type: {str(e)}'}), 400

    # Scale features and predict cluster
    scaled_features = scaler.transform(features)
    prediction = km.predict(scaled_features)

    return jsonify({'cluster': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
