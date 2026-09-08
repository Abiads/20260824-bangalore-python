"""
Day 11 - Practice Exercise 1: Cashier Performance
=================================================
Task:
    Calculate the total sales revenue processed by each cashier initials (Cashier_Initials).

Hint:
    Clean 'Cashier ID' using .str.split('|', expand=True) and use:
    .groupby('Cashier_Initials')['Total Line Revenue'].sum()
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


def analyze_cashier_performance(file_path: Path | None = None) -> pd.DataFrame:
    """Loads Sales data, cleans currency and cashier ID, and calculates revenue by cashier."""
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

    # Extract cashier initials
    df["Cashier_Initials"] = df["Cashier ID"].str.split("|", expand=True)[0]

    # Aggregate by cashier initials
    cashier_stats = (
        df.groupby("Cashier_Initials")
        .agg(
            Total_Revenue=("Total Line Revenue", "sum"),
            Transactions=("Invoice Number", "count"),
            Avg_Ticket=("Total Line Revenue", "mean"),
        )
        .sort_values(by="Total_Revenue", ascending=False)
    )

    print("\n" + "=" * 60)
    print("           CASHIER PERFORMANCE RANKINGS           ")
    print("=" * 60)
    print(f"{'Initials':<10} {'Transactions':<15} {'Avg Ticket':<15} {'Total Revenue':<15}")
    print("-" * 60)
    for initials, row in cashier_stats.iterrows():
        print(
            f"{initials:<10} {int(row['Transactions']):<15} "
            f"${row['Avg_Ticket']:<14.2f} ${row['Total_Revenue']:<14,.2f}"
        )
    print("=" * 60)

    print("\nTop 5 Cashiers by Revenue Processed:")
    top_5 = cashier_stats["Total_Revenue"].head(5).map("${:,.2f}".format)
    print(top_5)

    return cashier_stats


if __name__ == "__main__":
    analyze_cashier_performance()
