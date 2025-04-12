import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

#Indian personal finance and habits dataset
df = pd.read_csv('/content/data.csv') 

#Define spending behavior based on Income and Expenses
df['Total_Expenses'] = df[['Rent', 'Loan_Repayment', 'Insurance', 'Groceries', 'Transport',
                           'Eating_Out', 'Entertainment', 'Utilities', 'Healthcare',
                           'Education', 'Miscellaneous']].sum(axis=1)

#Apply labeling logic
def classify_behavior(row):
    if row['Total_Expenses'] > 1.1 * row['Income']:
        return 'Overspending'
    elif row['Total_Expenses'] < 0.7 * row['Income']:
        return 'Saving'
    else:
        return 'Balanced'

df['Spending_Behavior'] = df.apply(classify_behavior, axis=1)

# Drop non-usable columns
features = df.drop(columns=['Spending_Behavior', 'Total_Expenses'])

features = pd.get_dummies(features)

#labels
labels = df['Spending_Behavior']

#Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42, stratify=labels)

#Train the Model
clf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
clf.fit(X_train, y_train)

#Make Predictions

y_pred = clf.predict(X_test)

#Evaluation
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Create the heatmap with professional styling
plt.figure(figsize=(10, 8))  
sns.heatmap(
    cm,
    annot=True,       
    fmt='d',        
    cmap='coolwarm',      
    cbar_kws={'label': 'Count'}, 
    linewidths=0.5,       
    linecolor='black'
)
plt.title("Confusion Matrix", fontsize=18, fontweight='bold', color='black')
plt.xlabel("Predicted Labels", fontsize=14, fontweight='bold')
plt.ylabel("Actual Labels", fontsize=14, fontweight='bold')
plt.xticks(ticks=range(len(clf.classes_)), labels=clf.classes_, fontsize=12)
plt.yticks(ticks=range(len(clf.classes_)), labels=clf.classes_, fontsize=12, rotation=0)
plt.tight_layout()

#top 10 important ffeature in spending
importances = pd.Series(clf.feature_importances_, index=features.columns).sort_values(ascending=False)

sns.set_theme(style='whitegrid')
plt.figure(figsize=(14, 7))
palette = sns.color_palette("viridis", len(importances[:10]))

#bar plot
sns.barplot(
    x=importances[:10],
    y=importances.index[:10],
    palette=palette
)
plt.title("Top 10 Important Features", fontsize=18, fontweight='bold', color='black')
plt.xlabel("Importance Score", fontsize=14, fontweight='bold')
plt.ylabel("Feature", fontsize=14, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

#Adding values at the end of each bar to display the importance score
for container in plt.gca().containers:
    plt.gca().bar_label(container, fmt='%.2f', padding=5, fontsize=12)

plt.tight_layout()
plt.show()
