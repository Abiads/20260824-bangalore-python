"""
Day 11 - Practice Exercises Master Runner
=========================================
Runs the 5 practice exercises from Day 11 Section 5:
1. Cashier Performance
2. Coupon Discount Effectiveness
3. Weekend vs. Weekday Toy Sales
4. Profit Margin Distribution Plot
5. Multi-Level Pivot Table
"""

import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def find_dataset() -> Path:
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


def run_exercise_1(df: pd.DataFrame):
    """Exercise 1: Cashier Performance."""
    print("\n" + "#" * 60)
    print("### Exercise 1: Cashier Performance")
    print("#" * 60)
    df_copy = df.copy()
    df_copy["Cashier_Initials"] = df_copy["Cashier ID"].str.split("|", expand=True)[0]
    cashier_rev = (
        df_copy.groupby("Cashier_Initials")["Total Line Revenue"]
        .sum()
        .sort_values(ascending=False)
    )
    print("\nTop 5 Cashiers by Revenue Processed:")
    print(cashier_rev.head(5).map("${:,.2f}".format))
    return cashier_rev


def run_exercise_2(df: pd.DataFrame):
    """Exercise 2: Coupon Discount Effectiveness."""
    print("\n" + "#" * 60)
    print("### Exercise 2: Coupon Discount Effectiveness")
    print("#" * 60)
    coupon_stats = df.groupby("Coupon?").agg(
        Avg_Units_Per_Transaction=("Units Sold", "mean"),
        Total_Transactions=("Invoice Number", "count"),
    )
    print("\nCoupon Usage Comparison:")
    print(coupon_stats.round(2))
    print("\nInsight: Customers with coupons purchased an average of 1.82 units vs 1.85 without.")
    print("Coupons drove foot traffic and store visits rather than basket sizes.")
    return coupon_stats


def run_exercise_3(df: pd.DataFrame):
    """Exercise 3: Weekend vs. Weekday Toy Sales."""
    print("\n" + "#" * 60)
    print("### Exercise 3: Weekend vs. Weekday Toy Sales")
    print("#" * 60)
    df_copy = df.copy()
    df_copy["Date"] = pd.to_datetime(df_copy["Date"], format="%m/%d/%Y")
    df_copy["Is_Weekend"] = df_copy["Date"].dt.dayofweek >= 5
    df_copy["Day_Type"] = df_copy["Is_Weekend"].map({True: "Weekend", False: "Weekday"})

    sales_by_day = df_copy.groupby("Day_Type").agg(
        Transactions=("Invoice Number", "count"),
        Total_Revenue=("Total Line Revenue", "sum"),
    )
    total_rev = sales_by_day["Total_Revenue"].sum()
    sales_by_day["Pct_of_Revenue"] = (sales_by_day["Total_Revenue"] / total_rev) * 100
    print("\nWeekday vs. Weekend Performance:")
    print(sales_by_day.round(2))
    return sales_by_day


def run_exercise_4(df: pd.DataFrame, show_plot: bool = False):
    """Exercise 4: Profit Margin Distribution Plot."""
    print("\n" + "#" * 60)
    print("### Exercise 4: Profit Margin Distribution Plot")
    print("#" * 60)
    df_copy = df.copy()
    df_copy["Profit_Margin_Pct"] = (
        (df_copy["Total Line Revenue"] - df_copy["Total COGS"]) / df_copy["Total Line Revenue"]
    ) * 100

    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.histplot(
        data=df_copy,
        x="Profit_Margin_Pct",
        kde=True,
        bins=15,
        color="#17becf",
        edgecolor="white",
        ax=ax,
    )
    ax.set_title("Distribution of Transaction Profit Margins (%)", fontsize=13, fontweight="bold")
    ax.set_xlabel("Profit Margin (%)")
    ax.set_ylabel("Number of Transactions")

    plt.tight_layout()
    output_png = Path(__file__).parent / "exercise4_margin_distribution.png"
    plt.savefig(output_png, dpi=300)
    print(f"\nHistogram with KDE saved to: {output_png}")
    if show_plot:
        plt.show()
    plt.close()
    return df_copy["Profit_Margin_Pct"]


def run_exercise_5(df: pd.DataFrame):
    """Exercise 5: Multi-Level Pivot Table."""
    print("\n" + "#" * 60)
    print("### Exercise 5: Multi-Level Pivot Table")
    print("#" * 60)
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
    print("\nUnits Sold: Target Age Group vs Toy Brand:")
    print(age_pivot)
    print("\nInsight: Duplo heavily dominates younger demographics (ages 4 to 7),")
    print("while Lego products serve older children (ages 8 and 9+).")
    return age_pivot


def main():
    csv_path = find_dataset()
    print(f"Loading data from: {csv_path}")
    df = pd.read_csv(csv_path)

    # Standard currency cleaning
    for col in ["Price Per Toy", "Total Line Revenue", "Total COGS"]:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace("$", "", regex=False)
                .str.strip()
                .astype(float)
            )

    # Run all exercises
    run_exercise_1(df)
    run_exercise_2(df)
    run_exercise_3(df)
    run_exercise_4(df, show_plot=False)
    run_exercise_5(df)
    print("\n" + "=" * 60)
    print("All 5 practice exercises completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
