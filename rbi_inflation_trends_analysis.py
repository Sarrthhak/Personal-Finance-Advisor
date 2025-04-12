import pandas as pd

#Inflation data from RBI (skipping first six rows)
df = pd.read_csv("RBIB Table No. 18 _ Consumer Price Index (Base 2010=100).csv", skiprows=6)

#renaming columns
df.columns = [
    "Serial",
    "Month",
    "Commodity Description",
    "Provisional / Final",
    "Rural Index",
    "Rural Inflation",
    "Urban Index",
    "Urban Inflation",
    "Combined Index",
    "Combined Inflation"
]

#"Month" is full of NaN
df = df.dropna(subset=["Month"])

cols_to_convert = [
    "Rural Index", "Rural Inflation",
    "Urban Index", "Urban Inflation",
    "Combined Index", "Combined Inflation"
]
for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.reset_index(drop=True, inplace=True)

#display first few rows to verify
df.head()

#drop Serial column
df.drop(columns=['Serial'], inplace=True)

#dropping rows where Commodity Description is missing
df = df.dropna(subset=['Commodity Description'])

numeric_cols = [
    'Rural Index', 'Rural Inflation',
    'Urban Index', 'Urban Inflation',
    'Combined Index', 'Combined Inflation'
]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

df.dropna(subset=numeric_cols, how='all', inplace=True)

df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

df.isna().sum()

inflation_cols = ['Rural Inflation', 'Urban Inflation', 'Combined Inflation']
df[inflation_cols] = df[inflation_cols].apply(pd.to_numeric, errors='coerce')

#extracting month
df['Year'] = df['Month'].str[-4:].astype(int)

#group by year and calculating average inflation
yearly_inflation = df.groupby('Year')[inflation_cols].mean().reset_index()


sns.set_theme(style='whitegrid')
plt.figure(figsize=(12, 7))

colors = {
    "Rural Inflation": "#1f77b4",    # muted blue
    "Urban Inflation": "#ff7f0e",    # muted orange
    "Combined Inflation": "#2ca02c"  # muted green
}

#plot
for label in inflation_cols:
    plt.plot(
        yearly_inflation['Year'],
        yearly_inflation[label],
        marker='o',
        markersize=8,
        linewidth=2,
        label=label.replace(" Inflation", ""),
        color=colors[label]
    )

plt.title('Average Inflation Over the Years', fontsize=18, fontweight='bold', color='black')
plt.xlabel('Year', fontsize=14, fontweight='bold')
plt.ylabel('Inflation (%)', fontsize=14, fontweight='bold')
plt.xticks(yearly_inflation['Year'], fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Inflation Type', title_fontsize=12, fontsize=10, loc='best')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()
