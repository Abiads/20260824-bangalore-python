"""
Day 11 - Section 4: Complete End-to-End Analytics Pipeline
==========================================================
Script: sales_analytics_pipeline.py
Dataset: Day_11/Sales.csv

Performs data loading, currency & cashier parsing, feature engineering,
executive KPI generation, and saves an executive 4-panel dashboard.
"""

import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def find_dataset() -> Path:
    """Locate Sales.csv across multiple candidate directory trees."""
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
    raise FileNotFoundError("Could not find 'Sales.csv'.")


def load_and_clean_data(file_path: Path | str) -> pd.DataFrame:
    """Loads Sales.csv and performs type conversions and feature engineering."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Could not find dataset at '{file_path}'. Check your path.")

    df = pd.read_csv(path)
    print(f"Loaded {len(df)} transactions from {path.name}.")

    # 1. Clean currency columns
    currency_cols = ["Price Per Toy", "Total Line Revenue", "Total COGS"]
    for col in currency_cols:
        df[col] = df[col].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)

    # 2. Parse Date & extract time components
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["YearMonth"] = df["Date"].dt.to_period("M")

    # 3. Clean Cashier ID
    cashier_split = df["Cashier ID"].str.split("|", expand=True)
    df["Cashier_Initials"] = cashier_split[0]

    # 4. Feature engineering
    df["Line_Profit"] = df["Total Line Revenue"] - df["Total COGS"]
    df["Profit_Margin_Pct"] = (df["Line_Profit"] / df["Total Line Revenue"]) * 100

    # 5. Age categorization
    age_bins = [0, 18, 35, 55, 100]
    age_labels = ["Kids (<18)", "Young Adults (18-35)", "Middle-Aged (36-55)", "Seniors (56+)"]
    df["Age_Group"] = pd.cut(df["Purchaser Age"], bins=age_bins, labels=age_labels, right=True)

    return df


def print_executive_summary(df: pd.DataFrame):
    """Prints key business metrics to the console."""
    total_rev = df["Total Line Revenue"].sum()
    total_cogs = df["Total COGS"].sum()
    total_profit = df["Line_Profit"].sum()
    total_units = df["Units Sold"].sum()
    overall_margin = (total_profit / total_rev) * 100

    print("\n" + "=" * 50)
    print("           EXECUTIVE KPI SUMMARY           ")
    print("=" * 50)
    print(f"Total Transactions:   {len(df):,}")
    print(f"Total Units Sold:     {total_units:,}")
    print(f"Total Gross Revenue:  ${total_rev:,.2f}")
    print(f"Total COGS:           ${total_cogs:,.2f}")
    print(f"Total Net Profit:     ${total_profit:,.2f}")
    print(f"Overall Profit Margin:{overall_margin:6.2f}%")
    print("=" * 50)

    print("\nTop 3 Toys by Total Revenue:")
    top_3 = df.groupby("Toy Name")["Total Line Revenue"].sum().nlargest(3)
    for rank, (toy, rev) in enumerate(top_3.items(), 1):
        print(f"  {rank}. {toy:<30} ${rev:,.2f}")
    print("=" * 50 + "\n")


def generate_dashboard(df: pd.DataFrame, output_image: str = "sales_analytics_dashboard.png", show_plot: bool = False):
    """Generates a 4-panel comprehensive visual dashboard."""
    sns.set_theme(style="whitegrid")
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 11))
    fig.suptitle("Retail Toy Store Analytics Dashboard (2010 - 2012)", fontsize=18, fontweight="bold", y=0.98)

    # --- Panel 1: Top Toys by Revenue (Horizontal Bar Chart) ---
    ax1 = axes[0, 0]
    toy_rev = df.groupby("Toy Name")["Total Line Revenue"].sum().sort_values(ascending=True)
    bars = ax1.barh(toy_rev.index, toy_rev.values, color="#2b5c8f", edgecolor="black", height=0.6)
    ax1.set_title("Total Revenue by Toy Item", fontsize=13, fontweight="bold")
    ax1.set_xlabel("Revenue (USD $)")
    ax1.set_xlim(0, max(toy_rev.values) * 1.2)
    for bar in bars:
        w = bar.get_width()
        ax1.text(w + 100, bar.get_y() + bar.get_height() / 2, f"${w:,.0f}", va="center", fontsize=8)

    # --- Panel 2: Monthly Sales Trend (Seasonality) ---
    ax2 = axes[0, 1]
    monthly = df.groupby("YearMonth")["Total Line Revenue"].sum()
    x_dates = [str(p) for p in monthly.index]
    ax2.plot(x_dates, monthly.values, marker="o", color="#c0392b", linewidth=2.2, markersize=5)
    ax2.set_title("Monthly Revenue Trend (Q4 Holiday Surge)", fontsize=13, fontweight="bold")
    ax2.set_ylabel("Revenue (USD $)")
    ax2.set_xticks(range(0, len(x_dates), 3))
    ax2.set_xticklabels([x_dates[i] for i in range(0, len(x_dates), 3)], rotation=40, ha="right")

    # --- Panel 3: Age Distribution by Brand (Boxplot) ---
    ax3 = axes[1, 0]
    sns.boxplot(data=df, x="Toy Company", y="Purchaser Age", hue="Toy Company", palette="Set2", legend=False, ax=ax3, width=0.45)
    ax3.set_title("Customer Age Spread: Duplo vs. Lego", fontsize=13, fontweight="bold")
    ax3.set_xlabel("Toy Brand")
    ax3.set_ylabel("Purchaser Age (Years)")

    # --- Panel 4: Payment Method by Member Status (Countplot) ---
    ax4 = axes[1, 1]
    sns.countplot(
        data=df,
        x="Payment",
        hue="Member?",
        order=df["Payment"].value_counts().index,
        ax=ax4,
        palette="muted",
    )
    ax4.set_title("Payment Methods by Loyalty Membership", fontsize=13, fontweight="bold")
    ax4.set_xlabel("Payment Tender")
    ax4.set_ylabel("Number of Purchases")
    ax4.legend(title="Member?", loc="upper right")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    script_dir = Path(__file__).parent if "__file__" in globals() else Path(".")
    save_path = script_dir / output_image
    plt.savefig(save_path, dpi=300)
    print(f"Dashboard saved successfully as '{save_path.resolve()}'.")
    if show_plot:
        plt.show()
    plt.close()


if __name__ == "__main__":
    csv_file = find_dataset()
    data = load_and_clean_data(csv_file)
    print_executive_summary(data)
    generate_dashboard(data, output_image="sales_analytics_dashboard.png", show_plot=False)
