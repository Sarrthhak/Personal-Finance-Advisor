# 💰 Personal Finance Advisor using Supervised Learning

A data-driven machine learning project designed to analyze and predict personal finance behavior. Using real-world inspired Indian financial data, the project provides insights into spending habits, forecasts future expenses, and visualizes macroeconomic trends like inflation and digital transaction growth.

---

## 🧠 Project Goals

- 🔍 Classify individuals into categories like Saving, Overspending, and Balanced
- 📈 Predict next month's spending using current financial indicators
- 📊 Analyze inflation data from RBI and digital payment trends from NPCI
- 🧩 Understand feature importance and financial decision-making

---

## 🧪 Machine Learning Models Used

| Model                   | Purpose                                                     |
|------------------------|-------------------------------------------------------------|
| Random Forest Classifier | Classifies individuals based on their spending behavior     |
| Linear Regression       | Predicts next month’s spending using current financial data |

---

## 📁 Project Structure

```plaintext
.
├── data.csv                       # Main dataset with personal finance data
├── inflation_data.csv            # RBI CPI data (cleaned and formatted)
├── upi_transactions.csv          # UPI transaction volume & value
├── finance_behavior_classifier.py   # Random Forest model for classification
├── expense_forecast_regression.py   # Linear Regression model for prediction
├── inflation_trend_plot.py          # Visualizes average inflation over years
├── upi_growth_analysis.py          # Analyzes UPI growth
└── README.md
