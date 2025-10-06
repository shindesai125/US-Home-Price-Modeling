from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model = joblib.load("final_random_forest_model.joblib")

# Feature names and units
FEATURE_NAMES = [
    ('Home_Price_Index', 'Index Value'),
    ('Mortgage_Rate', '%'),
    ('Unemployment_Rate', '%'),
    ('Housing_Starts', 'Units'),
    ('CPI', 'Index Value'),
    ('Population_Monthly', 'Millions'),
    ('HPI_rolling', 'Index Value'),
    ('Year', 'YYYY'),
    ('Month', 'MM'),
    ('Post_COVID', '0 = No, 1 = Yes'),
    ('Log_Unemployment', 'Log Value'),
    ('CPI_Growth', '% Growth'),
    ('Mortgage_Rate_Level', '0 = Low, 1 = Med, 2 = High')
]

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            values = [float(request.form[feature]) for feature, _ in FEATURE_NAMES]
            features = np.array([values])
            log_price = model.predict(features)[0]
            actual_price = np.exp(log_price)
            prediction = f"The predicted House Price is: ${actual_price*1000:,.2f}"
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template("index.html", features=FEATURE_NAMES, prediction=prediction)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
