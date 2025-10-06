from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('final_random_forest_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        features = [
            data['Home_Price_Index'],
            data['HPI_rolling'],
            data['CPI'],
            data['Population_Monthly']
        ]
        prediction = model.predict([features])
        return jsonify({'predicted_price': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets PORT dynamically
    app.run(host='0.0.0.0', port=port, debug=True)
