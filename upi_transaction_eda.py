import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#dataset 1- Phonepe transaction data
df = pd.read_csv("/content/agg_trans.csv")

print(df.isna().sum())

df['Year'] = df['Year'].astype(int)
df['Quarter'] = df['Quarter'].astype(str)

#Line Plot: Yearly UPI Transaction Amount
yearly_data = df.groupby("Year")["Transaction_amount"].sum().reset_index()
yearly_data["Transaction_amount"] /= 1e12  #converting amount to trillion for readability

plt.figure(figsize=(12, 6))  
sns.set_style("whitegrid")  

#line plot
sns.lineplot(data=yearly_data, x="Year", y="Transaction_amount", marker='o', color='royalblue', linewidth=2)

plt.title("UPI Transaction Amount Growth (2018-2022)", fontsize=16, fontweight='bold', color='black')
plt.xlabel("Year", fontsize=14, fontweight='bold')
plt.ylabel("Transaction Amount (in Trillions INR)", fontsize=14, fontweight='bold')
plt.xticks(ticks=yearly_data["Year"], labels=yearly_data["Year"].astype(int), fontsize=12)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

#Bar Plot: UPI Transaction Count by Region
region_data = df.groupby("Region")["Transaction_count"].sum().reset_index()
region_data["Transaction_count"] /= 1e9  #converting to billions for readability

plt.figure(figsize=(12, 6))
sns.set_style("whitegrid")

#bar plot
sns.barplot(data=region_data, x="Region", y="Transaction_count", palette=sns.color_palette("cubehelix", as_cmap=False))
plt.title("Total UPI Transaction Count by Region", fontsize=16, fontweight='bold', color='black')
plt.xlabel("Region", fontsize=14, fontweight='bold')
plt.ylabel("Transaction Count (in Billions)", fontsize=14, fontweight='bold')
plt.xticks(fontsize=12)

#Annotating the bars with the actual values
for i in range(len(region_data)):
    plt.text(i, region_data["Transaction_count"][i] + 0.1, f'{region_data["Transaction_count"][i]:.2f}',
             ha='center', va='bottom', fontsize=10, color='black')
    
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


#Heatmap: Quarter-wise UPI Transaction Amount by Year
pivot_table = df.pivot_table(values="Transaction_amount", index="Year", columns="Quarter", aggfunc="sum")
pivot_table /= 1e12  #converting to trillions for better readability

plt.figure(figsize=(10, 6))  
sns.set_style("white")  

#heatmap
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, cbar_kws={"label": "Transaction Amount (in Trillions INR)"})
plt.title("Heatmap of UPI Transaction Amount (Year vs Quarter)", fontsize=16, fontweight='bold', color='black')
plt.xlabel("Quarter", fontsize=14, fontweight='bold')
plt.ylabel("Year", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
