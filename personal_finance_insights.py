import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib.ticker as ticker

#Indian personal finance and habits dataset
df = pd.read_csv('/content/data.csv')

print(df.isna().sum())

sns.set(style="whitegrid")
plt.figure(figsize=(12, 8))

#Grouped bar plot: average spending, davings, and disposable income by income group
bins = [0, 20000, 40000, 60000, 80000, 100000, np.inf]
labels = ['<20K', '20K-40K', '40K-60K', '60K-80K', '80K-100K', '>100K']
df['Income_Group'] = pd.cut(df['Income'], bins=bins, labels=labels)

#total spending from all categories
spending_cols = [
    'Groceries', 'Transport', 'Eating_Out', 'Entertainment',
    'Utilities', 'Healthcare', 'Education', 'Miscellaneous'
]
df['Total_Spending'] = df[spending_cols].sum(axis=1)

grouped = df.groupby('Income_Group')[
    ['Total_Spending', 'Desired_Savings', 'Disposable_Income']
].mean().reset_index()

#grouped plot
plt.figure(figsize=(12, 6))
ax = grouped.plot(
    x='Income_Group',
    kind='bar',
    figsize=(12, 6),
    width=0.8,
    color=['steelblue', 'mediumseagreen', 'indianred'],
    edgecolor='black'
)
plt.title(
    "Average Spending, Savings, and Disposable Income by Income Group",
    fontsize=18, fontweight="bold", color="black"
)
plt.ylabel("Average Amount (INR)", fontsize=14, fontweight="bold")
plt.xlabel("Income Group", fontsize=14, fontweight="bold")
plt.xticks(rotation=0, fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
#anootations for each bar
for bar in ax.patches:
    bar_height = bar.get_height()
    ax.annotate(
        f"{bar_height:,.0f}",
        (bar.get_x() + bar.get_width() / 2, bar_height),
        ha='center', va='bottom', fontsize=10, color="black"
    )
plt.tight_layout()
plt.show()

#Correalation heatmap
cols_to_plot = ['Income', 'Disposable_Income', 'Desired_Savings', 'Groceries', 'Healthcare']

#pairplot
pair_plot = sns.pairplot(
    df[cols_to_plot],
    diag_kind="kde",
    palette="coolwarm", 
    plot_kws={'alpha': 0.7, 's': 50, 'edgecolor': 'k'},
    diag_kws={'shade': True, 'linewidth': 2}  
)

#looping through all axes to format all
for ax in pair_plot.axes.flatten():
    if ax is not None:
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: format(x, ',.0f')))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: format(y, ',.0f')))

        ax.tick_params(axis='both', labelsize=10)

        ax.grid(True, linestyle='--', alpha=0.5)

plt.suptitle(
    "Pairwise Relationships Among Financial Features",
    fontsize=18,
    fontweight="bold",
    color="black",
    y=1.02
)
plt.tight_layout()
plt.show()

#Boxplot - Expenses by City Tier
sns.set_theme(style='whitegrid')
plt.figure(figsize=(14, 6))

#Melt the DataFrame for easier plotting by expense type
melted_df = df.melt(
    id_vars=['City_Tier'],
    value_vars=['Groceries', 'Healthcare', 'Utilities', 'Education', 'Entertainment'],
    var_name='Expense_Type',
    value_name='Amount'
)


palette = sns.color_palette("Set2")
#boxplot
ax = sns.boxplot(
    x='Expense_Type',
    y='Amount',
    hue='City_Tier',
    data=melted_df,
    palette=palette,
    showfliers=True  
)
plt.title("Expense Distribution by City Tier", fontsize=18, fontweight='bold', color='black')
plt.xlabel("Expense Type", fontsize=14, fontweight='bold')
plt.ylabel("Amount (INR)", fontsize=14, fontweight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='City Tier', title_fontsize=12, fontsize=10, loc='best')
plt.tight_layout()
plt.show()
