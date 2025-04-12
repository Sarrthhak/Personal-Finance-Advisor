import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/data.csv') 

#Calculating total current month spending
spending_columns = ['Groceries', 'Transport', 'Eating_Out', 'Entertainment', 'Utilities',
                    'Healthcare', 'Education', 'Miscellaneous']
df['Total_Spending'] = df[spending_columns].sum(axis=1)

#Simulate 'Next_Month_Spending' for demo 
np.random.seed(42)
df['Next_Month_Spending'] = df['Total_Spending'] * (np.random.normal(loc=1.02, scale=0.05, size=len(df)))

#select feature
X = df[['Income', 'Age', 'Rent', 'Loan_Repayment', 'Insurance', 'Healthcare', 'Utilities', 'Disposable_Income']]
y = df['Next_Month_Spending']

#Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Train Model
model = LinearRegression()
model.fit(X_train, y_train)

#Predict
y_pred = model.predict(X_test)

#Evaluate
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"📏 Mean Absolute Error (MAE): ₹{mae:.2f}")
print(f"📈 R² Score: {r2:.4f}")

