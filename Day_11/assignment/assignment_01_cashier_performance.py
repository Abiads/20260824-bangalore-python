from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "Sales.csv"
if not csv_path.exists():
    csv_path = Path("Sales.csv")

df = pd.read_csv(csv_path)
df["Total Line Revenue"] = df["Total Line Revenue"].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)
df["Cashier_Initials"] = df["Cashier ID"].str.split("|", expand=True)[0]

cashier_revenue = df.groupby("Cashier_Initials")["Total Line Revenue"].sum().sort_values(ascending=False)
print("Top 5 Cashiers by Revenue Processed:")
print(cashier_revenue.head(5).map("${:,.2f}".format))
