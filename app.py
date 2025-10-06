from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Root route for Render homepage
@app.route('/')
def home():
    return "✅ US Home Price Prediction API is running. Use POST /predict to get predictions."

# Load the trained model
model = joblib.load('final_random_forest_model.pkl')

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        # Extract features from JSON
        features = [
            data['Home_Price_Index'],
            data['HPI_rolling'],
            data['CPI'],
            data['Population_Monthly']
        ]
        prediction = model.predict([features])
        return jsonify({'predicted_price': float(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Bind to Render's dynamic port
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
