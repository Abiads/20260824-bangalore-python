"""
Day 11 - Practice Exercise 5: Multi-Level Pivot Table
====================================================
Task:
    Create a pivot table showing total units sold where rows are
    'Suggested Age' categories, columns are 'Toy Company', and
    values are 'Units Sold' (aggregated by 'sum').

Expected Result:
    Understand product distribution and brand specialization by target age.
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


def analyze_age_brand_pivot(file_path: Path | None = None) -> pd.DataFrame:
    """Constructs a multi-level pivot table of Units Sold across Age Categories and Brands."""
    if file_path is None:
        file_path = get_dataset_path()

    print(f"Loading dataset from: {file_path}")
    df = pd.read_csv(file_path)

    age_pivot = pd.pivot_table(
        data=df,
        values="Units Sold",
        index="Suggested Age",
        columns="Toy Company",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="Total",
    )

    print("\n" + "=" * 60)
    print("      UNITS SOLD: TARGET AGE GROUP VS. TOY BRAND      ")
    print("=" * 60)
    print(age_pivot)
    print("=" * 60)

    print("\nBusiness Insights & Market Segmentation:")
    print("- Duplo dominates the early childhood segment (ages 4 to 7):")
    print(f"  * 6 and up: {age_pivot.loc['6 and up', 'Duplo']} units (vs {age_pivot.loc['6 and up', 'Lego']} for Lego)")
    print(f"  * 7 and up: {age_pivot.loc['7 and up', 'Duplo']} units (vs {age_pivot.loc['7 and up', 'Lego']} for Lego)")
    print("- Lego captures the older demographic (ages 8 and 9+):")
    print(f"  * 8 and up: {age_pivot.loc['8 and up', 'Lego']} units (0 Duplo)")
    print(f"  * 9 and up: {age_pivot.loc['9 and up', 'Lego']} units (0 Duplo)")
    print("- Strategic takeaway: The two brands have a clear, complementary age bifurcation")
    print("  with virtually zero catalog cannibalization.")

    return age_pivot


if __name__ == "__main__":
    analyze_age_brand_pivot()
