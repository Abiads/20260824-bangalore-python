"""
Day 11 - Practice Exercise 3: Weekend vs. Weekday Toy Sales
==========================================================
Task:
    Create a boolean column 'Is_Weekend' (True if the transaction day is
    Saturday or Sunday, False otherwise).
    Compute the total revenue generated on weekends vs. weekdays.

Hint:
    df['Date'].dt.dayofweek >= 5
"""

from pathlib import Path
import pandas as pd


def get_dataset_path() -> Path:
    """Find Sales.csv across common working directories."""
    candidates = [
        Path("Sales.csv"),
        Path("Day_11/Sales.csv"),
        Path("../Sales.csv"),
        Path("data/Sales.csv"),
        Path("../ds-workspace/data/Sales.csv"),
        Path(__file__).parent / "Sales.csv",
        Path(__file__).parent.parent / "Sales.csv",
        Path(__file__).parent.parent / "ds-workspace" / "data" / "Sales.csv",
    ]
    for p in candidates:
        if p.exists():
            return p.resolve()
    raise FileNotFoundError("Could not find 'Sales.csv'. Please ensure it exists in Day_11.")


def analyze_weekend_vs_weekday(file_path: Path | None = None) -> pd.DataFrame:
    """Computes and compares sales performance metrics across weekdays and weekends."""
    if file_path is None:
        file_path = get_dataset_path()

    print(f"Loading dataset from: {file_path}")
    df = pd.read_csv(file_path)

    # Clean currency column
    df["Total Line Revenue"] = (
        df["Total Line Revenue"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.strip()
        .astype(float)
    )

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")

    # Day of week: Monday=0, Tuesday=1, ..., Saturday=5, Sunday=6
    df["Is_Weekend"] = df["Date"].dt.dayofweek >= 5
    df["Day_Type"] = df["Is_Weekend"].map({True: "Weekend", False: "Weekday"})

    sales_by_day_type = df.groupby("Day_Type").agg(
        Transactions=("Invoice Number", "count"),
        Total_Units=("Units Sold", "sum"),
        Total_Revenue=("Total Line Revenue", "sum"),
        Avg_Order_Value=("Total Line Revenue", "mean"),
    )

    total_rev = sales_by_day_type["Total_Revenue"].sum()
    sales_by_day_type["Pct_of_Revenue"] = (sales_by_day_type["Total_Revenue"] / total_rev) * 100

    print("\n" + "=" * 75)
    print("                 WEEKDAY VS WEEKEND TOY SALES PERFORMANCE                 ")
    print("=" * 75)
    print(sales_by_day_type.round(2))
    print("=" * 75)

    print("\nSummary Breakdown:")
    for day_type, row in sales_by_day_type.iterrows():
        print(
            f"- {day_type:<8}: {int(row['Transactions'])} transactions, "
            f"${row['Total_Revenue']:,.2f} total revenue "
            f"({row['Pct_of_Revenue']:.2f}% of total, avg ticket ${row['Avg_Order_Value']:.2f})"
        )

    return sales_by_day_type


if __name__ == "__main__":
    analyze_weekend_vs_weekday()
