# app/__init__.py
from flask import Flask
import joblib
import numpy as np

def create_app():
    # Create the Flask application
    app = Flask(__name__)

    # Load the model and scaler
    model_path = '../models/kmeans_model.pkl'
    scaler_path = '../models/scaler.pkl'
    km = joblib.load(model_path)
    scaler = joblib.load(scaler_path)

    # Register routes
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/predict', methods=['POST'])
    def predict():
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

        scaled_features = scaler.transform(features)
        prediction = km.predict(scaled_features)

        return jsonify({'cluster': int(prediction[0])})

    return app
