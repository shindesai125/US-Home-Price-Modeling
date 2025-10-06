# US Home Price Modeling Project

This project analyzes and models the key macroeconomic and demographic factors influencing US home prices from 2000 to 2025 using publicly available data and machine learning techniques.

---

## 📁 Files Included

```
US_Home_Price_Modeling/
|
├── Final_Report.pdf / Final_Report.md     # Detailed project report
├── final_random_forest_model.pkl          # Exported trained model (Random Forest)
├── home_price_modeling.py                 # Python script version of the Colab notebook
├── home_price_modeling.ipynb              # Original Jupyter Notebook
└── README.md                               # This file
```

---

## 📌 Project Objective

To predict the US Home Price Index based on macroeconomic indicators using regression models.

---

## 📊 Data Sources

- **Home Price Index (HPI)**: S&P Case-Shiller Index via [FRED](https://fred.stlouisfed.org/series/CSUSHPINSA)
- **Mortgage Rates**: [FRED - MORTGAGE30US](https://fred.stlouisfed.org/series/MORTGAGE30US)
- **Unemployment Rate**: [FRED - UNRATE](https://fred.stlouisfed.org/series/UNRATE)
- **Median Household Income**: US Census Bureau
- **Housing Starts**: [FRED - HOUST](https://fred.stlouisfed.org/series/HOUST)
- **Consumer Price Index (CPI)**: [FRED - CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL)
- **Population Estimates**: [US Census Bureau](https://www.census.gov/data.html)

---

## 🔧 How to Run

1. Ensure you have Python 3.10+ and the following packages installed:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn joblib
```

2. Run the script:

```bash
python home_price_modeling.py
```

3. Load the model for inference (example):

```python
import joblib
model = joblib.load('final_random_forest_model.pkl')
```

---

## 🧠 Model Details

- Final model: **Random Forest Regressor**
- Performance:
  - R² Score: 0.9998
  - RMSE: 0.0023
- Trained on top features:
  - Home\_Price\_Index
  - HPI\_rolling
  - CPI
  - Population\_Monthly

---

## 📄 Author

Sai Shinde\
**Date Completed**: June 13, 2025
GitHub: [@shindesai125](https://github.com/shindesai125)

---

## ✅ Notes

- All data used in this project is publicly available.
- The notebook was built using Google Colab.
- The `.pkl` model can be integrated into web apps for live predictions.

Feel free to explore and reuse this project with attribution. 🚀


US Home Price Modeling

Small project for experimenting with U.S. home price modeling. This repo contains:

- `app.py` — application entry (project code)
- `requirements.txt` — Python dependencies
- `render.yaml` — deployment/render config
- `.gitignore` — ignores common temp files and environments

Quick start

1. Open PowerShell in this folder:

```powershell
cd 'C:\Users\shind\OneDrive\Desktop\US-Home-Price-Modeling'
```

2. Run the bundled setup script to finish Git setup, make an initial commit, and optionally create a GitHub repository:

```powershell
# Make sure the script is allowed to run (one-time, if your execution policy blocks it):
# Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
.\n+.\setup-repo.ps1

# To create a GitHub repo and push (requires GitHub CLI `gh`):
.\setup-repo.ps1 -CreateGitHub -RepoName "my-repo-name"
```

What the script does

- Ensures `git` is available and initializes a repo if needed
- Prompts to set `git` global `user.name` and `user.email` if they aren't configured
- Stages all files and creates an initial commit
- Renames the branch to `main`
- If requested and you have `gh` installed, creates a remote repo and pushes

If you prefer, you can run the Git commands manually — ask and I will walk you through each step.
