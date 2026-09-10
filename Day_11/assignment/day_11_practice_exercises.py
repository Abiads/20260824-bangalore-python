from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_path = Path(__file__).resolve().parent / "Sales.csv"
if not csv_path.exists():
    csv_path = Path("Sales.csv")

df = pd.read_csv(csv_path)

# Exercise 1: Cashier Performance
df["Total Line Revenue"] = df["Total Line Revenue"].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)
df["Cashier_Initials"] = df["Cashier ID"].str.split("|", expand=True)[0]
cashier_revenue = df.groupby("Cashier_Initials")["Total Line Revenue"].sum().sort_values(ascending=False)
print("--- Exercise 1: Cashier Performance ---")
print(cashier_revenue.head(5).map("${:,.2f}".format))

# Exercise 2: Coupon Discount Effectiveness
coupon_stats = df.groupby("Coupon?").agg(
    Avg_Units_Per_Transaction=("Units Sold", "mean"),
    Total_Transactions=("Invoice Number", "count")
)
print("\n--- Exercise 2: Coupon Discount Effectiveness ---")
print(coupon_stats.round(2))

# Exercise 3: Weekend vs. Weekday Toy Sales
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
df["Is_Weekend"] = df["Date"].dt.dayofweek >= 5
df["Day_Type"] = df["Is_Weekend"].map({True: "Weekend", False: "Weekday"})
sales_by_day = df.groupby("Day_Type").agg(
    Transactions=("Invoice Number", "count"),
    Total_Revenue=("Total Line Revenue", "sum")
)
sales_by_day["Pct_of_Revenue"] = (sales_by_day["Total_Revenue"] / sales_by_day["Total_Revenue"].sum()) * 100
print("\n--- Exercise 3: Weekend vs. Weekday Toy Sales ---")
print(sales_by_day.round(2))

# Exercise 4: Profit Margin Distribution Plot
for col in ["Total Line Revenue", "Total COGS"]:
    df[col] = df[col].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)
df["Profit_Margin_Pct"] = ((df["Total Line Revenue"] - df["Total COGS"]) / df["Total Line Revenue"]) * 100
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=df, x="Profit_Margin_Pct", kde=True, bins=15, color="#17becf", edgecolor="white", ax=ax)
ax.set_title("Distribution of Transaction Profit Margins (%)", fontsize=13, fontweight="bold")
ax.set_xlabel("Profit Margin (%)")
ax.set_ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig(Path(csv_path).parent / "exercise4_margin_distribution.png", dpi=300)
plt.close()
print("\n--- Exercise 4: Profit Margin Plot saved to exercise4_margin_distribution.png ---")

# Exercise 5: Multi-Level Pivot Table
age_pivot = pd.pivot_table(
    data=df,
    values="Units Sold",
    index="Suggested Age",
    columns="Toy Company",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="Total"
)
print("\n--- Exercise 5: Multi-Level Pivot Table ---")
print(age_pivot)
