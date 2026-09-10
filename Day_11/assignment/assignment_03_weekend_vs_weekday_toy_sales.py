from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "Sales.csv"
if not csv_path.exists():
    csv_path = Path("Sales.csv")

df = pd.read_csv(csv_path)
df["Total Line Revenue"] = df["Total Line Revenue"].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)
df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

df["Is_Weekend"] = df["Date"].dt.dayofweek >= 5
df["Day_Type"] = df["Is_Weekend"].map({True: "Weekend", False: "Weekday"})

sales_by_day_type = df.groupby("Day_Type").agg(
    Transactions=("Invoice Number", "count"),
    Total_Revenue=("Total Line Revenue", "sum")
)
sales_by_day_type["Pct_of_Revenue"] = (sales_by_day_type["Total_Revenue"] / sales_by_day_type["Total_Revenue"].sum()) * 100

print("Weekday vs Weekend Performance:")
print(sales_by_day_type.round(2))
