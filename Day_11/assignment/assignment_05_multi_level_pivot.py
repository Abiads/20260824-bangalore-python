from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "Sales.csv"
if not csv_path.exists():
    csv_path = Path("Sales.csv")

df = pd.read_csv(csv_path)

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
print("Units Sold: Target Age Group vs Toy Brand:")
print(age_pivot)
