import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Healthcare ependiture by age and sex dataset
df = pd.read_csv('/content/age and Sex.csv')

print(df.isna().sum())

df_melted = df.melt(id_vars=['Payer', 'Service', 'Age Group', 'Sex'],
                    var_name='Year',
                    value_name='Health Expenditure')

#converting year to numeric
df_melted['Year'] = pd.to_numeric(df_melted['Year'], errors='coerce')

df_melted = df_melted.dropna(subset=['Health Expenditure'])

#Remove rows where any of the grouping columns have 'Total'
df_melted = df_melted[~df_melted['Payer'].str.contains('Total', case=False, na=False)]
df_melted = df_melted[~df_melted['Service'].str.contains('Total', case=False, na=False)]
df_melted = df_melted[~df_melted['Sex'].str.contains('Total', case=False, na=False)]
df_melted = df_melted[~df_melted['Age Group'].str.contains('Total', case=False, na=False)]

sns.set(style="whitegrid")

#bar plot: Total expenditure by Payer
payer_total = df_melted.groupby('Payer')['Health Expenditure'].sum().reset_index()
sns.set_theme(style='whitegrid')
plt.figure(figsize=(12, 7))
sns.barplot(
    data=payer_total,
    x='Health Expenditure',
    y='Payer',
    palette=sns.color_palette("mako", len(payer_total))  
)
plt.title("Total Healthcare Expenditure by Payer", fontsize=18, fontweight='bold', color='black')
plt.xlabel("Total Expenditure (in Millions)", fontsize=14, fontweight='bold')
plt.ylabel("Payer", fontsize=14, fontweight='bold')
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

#Adding values at the end of each bar for better clarity
for container in plt.gca().containers:
    plt.gca().bar_label(container, fmt='%.0f', padding=3, fontsize=12)

plt.tight_layout()
plt.show()

#Bar plot: Total expenditure by Age Group

#Group by Age Group and calculate total healthcare expenditure
age_total = df_melted.groupby('Age Group')['Health Expenditure'].sum().reset_index()

sns.set_theme(style='whitegrid')
plt.figure(figsize=(12, 7))
palette = sns.color_palette("crest", len(age_total))

#barplot
sns.barplot(
    data=age_total,
    x='Health Expenditure',
    y='Age Group',
    palette=palette
)
plt.title("Total Healthcare Expenditure by Age Group", fontsize=18, fontweight='bold', color='black')
plt.xlabel("Total Expenditure (INR)", fontsize=14, fontweight='bold')
plt.ylabel("Age Group", fontsize=14, fontweight='bold')

#removing scientific notations
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

#Adding values at the end of each bar for better clarity
for container in plt.gca().containers:
    plt.gca().bar_label(container, fmt='%.0f', padding=3, fontsize=12, color='black')
plt.tight_layout()
plt.show()
