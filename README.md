US Home Price Modeling Project
This project analyzes and models the key macroeconomic and demographic factors influencing US home prices from 2000 to 2025 using publicly available data and machine learning techniques.
________________________________________
📁 Files Included
US_Home_Price_Modeling/
|
├── Final_Report.pdf / Final_Report.md     # Detailed project report
├── final_random_forest_model.pkl          # Exported trained model (Random Forest)
├── home_price_modeling.py                 # Python script version of the Colab notebook
├── home_price_modeling.ipynb              # Original Jupyter Notebook
└── README.md                               # This file
________________________________________
📌 Project Objective
To predict the US Home Price Index based on macroeconomic indicators using regression models.
________________________________________
📊 Data Sources
•	Home Price Index (HPI): S&P Case-Shiller Index via FRED
•	Mortgage Rates: FRED - MORTGAGE30US
•	Unemployment Rate: FRED - UNRATE
•	Median Household Income: US Census Bureau
•	Housing Starts: FRED - HOUST
•	Consumer Price Index (CPI): FRED - CPIAUCSL
•	Population Estimates: US Census Bureau
________________________________________
🔧 How to Run
1.	Ensure you have Python 3.10+ and the following packages installed:
pip install pandas numpy scikit-learn matplotlib seaborn joblib
2.	Run the script:
python home_price_modeling.py
3.	Load the model for inference (example):
import joblib
model = joblib.load('final_random_forest_model.pkl')
________________________________________
🧠 Model Details
•	Final model: Random Forest Regressor
•	Performance:
o	R² Score: 0.9998
o	RMSE: 0.0023
•	Trained on top features:
o	Home_Price_Index
o	HPI_rolling
o	CPI
o	Population_Monthly
________________________________________
📄 Author
Sai Shinde
Date Completed: June 13, 2025
GitHub: [@shindesai125](https://github.com/shindesai125)

________________________________________
✅ Notes
•	All data used in this project is publicly available.
•	The notebook was built using Google Colab.
•	The .pkl model can be integrated into web apps for live predictions.
Feel free to explore and reuse this project with attribution. 🚀
