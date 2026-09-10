from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "Sales.csv"
if not csv_path.exists():
    csv_path = Path("Sales.csv")

df = pd.read_csv(csv_path)
coupon_stats = df.groupby("Coupon?").agg(
    Avg_Units_Per_Transaction=("Units Sold", "mean"),
    Total_Transactions=("Invoice Number", "count")
)
print("Coupon Usage Comparison:")
print(coupon_stats.round(2))
