"""
sales_analytics_pipeline.py
Complete End-to-End Data Science Pipeline using Pandas, Matplotlib, and Seaborn.
Demonstrates:
  1. Data Loading & Inspection
  2. Data Cleaning & Type Casting
  3. Feature Engineering (Profit, Margin %, Age Grouping, Date parsing)
  4. Aggregation & KPI reporting
  5. Multi-panel Visualization Dashboard
"""

import os
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def find_sales_csv() -> Path:
    """Finds Sales.csv regardless of where the script is executed from."""
    candidates = [
        Path("Sales.csv"),
        Path("../Sales.csv"),
        Path("Day_11/Sales.csv"),
        Path(__file__).resolve().parent.parent / "Sales.csv"
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError("Could not locate Sales.csv. Please ensure it is in Day_11/.")


def load_and_clean_data(file_path: Path) -> pd.DataFrame:
    """Loads Sales.csv, handles data cleaning, and engineers features."""
    print(f"Loading data from: {file_path}")
    df = pd.read_csv(file_path)
    print(f"-> Successfully loaded {len(df):,} records with {df.shape[1]} columns.")

    # 1. Clean currency columns
    currency_cols = ["Price Per Toy", "Total Line Revenue", "Total COGS"]
    for col in currency_cols:
        df[col] = df[col].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)

    # 2. Parse Date
    df["Date"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["YearMonth"] = df["Date"].dt.to_period("M")

    # 3. Clean Cashier ID
    cashier_split = df["Cashier ID"].str.split("|", expand=True)
    df["Cashier_Initials"] = cashier_split[0]

    # 4. Feature Engineering
    df["Line_Profit"] = df["Total Line Revenue"] - df["Total COGS"]
    df["Profit_Margin_Pct"] = (df["Line_Profit"] / df["Total Line Revenue"]) * 100

    # 5. Demographic Bins
    age_bins = [0, 18, 35, 55, 100]
    age_labels = ["Kids (<18)", "Young Adults (18-35)", "Middle-Aged (36-55)", "Seniors (56+)"]
    df["Age_Group"] = pd.cut(df["Purchaser Age"], bins=age_bins, labels=age_labels, right=True)

    # 6. Boolean Flags
    for flag_col in ["Member?", "Coupon?", "Parking Validation?"]:
        df[flag_col] = df[flag_col].map({"Yes": True, "No": False})

    return df


def print_executive_summary(df: pd.DataFrame):
    """Prints formatted summary business KPIs."""
    total_rev = df["Total Line Revenue"].sum()
    total_cogs = df["Total COGS"].sum()
    total_profit = df["Line_Profit"].sum()
    total_units = df["Units Sold"].sum()
    overall_margin = (total_profit / total_rev) * 100

    print("\n" + "=" * 55)
    print("           RETAIL STORE EXECUTIVE SUMMARY          ")
    print("=" * 55)
    print(f"Total Transactions Processed: {len(df):,}")
    print(f"Total Physical Units Sold:    {total_units:,}")
    print(f"Total Gross Revenue:          ${total_rev:,.2f}")
    print(f"Total Wholesale Cost (COGS):  ${total_cogs:,.2f}")
    print(f"Total Net Store Profit:       ${total_profit:,.2f}")
    print(f"Overall Net Profit Margin:    {overall_margin:6.2f}%")
    print("=" * 55)

    print("\nTop 5 Toys by Total Revenue:")
    top_5 = df.groupby("Toy Name").agg(
        Units_Sold=("Units Sold", "sum"),
        Revenue=("Total Line Revenue", "sum"),
        Profit=("Line_Profit", "sum")
    ).sort_values(by="Revenue", ascending=False).head(5)
    
    for idx, (toy, row) in enumerate(top_5.iterrows(), 1):
        print(f"  {idx}. {toy:<30} | Units: {row['Units_Sold']:>4} | Revenue: ${row['Revenue']:>8,.2f} | Profit: ${row['Profit']:>8,.2f}")

    print("\nRevenue Breakdown by Toy Brand:")
    brand_summary = df.groupby("Toy Company").agg(
        Transactions=("Invoice Number", "count"),
        Units=("Units Sold", "sum"),
        Revenue=("Total Line Revenue", "sum"),
        Profit=("Line_Profit", "sum")
    )
    for brand, row in brand_summary.iterrows():
        margin = (row["Profit"] / row["Revenue"]) * 100
        print(f"  * {brand:<8}: Revenue = ${row['Revenue']:,.2f} | Profit = ${row['Profit']:,.2f} ({margin:.1f}% margin)")
    print("=" * 55 + "\n")


def generate_visual_dashboard(df: pd.DataFrame, output_path: str = "sales_dashboard.png"):
    """Creates a 4-panel data visualization dashboard using Matplotlib and Seaborn."""
    sns.set_theme(style="whitegrid", palette="deep")
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
    fig.suptitle("Toy Retail Analytics Dashboard (2010 - 2012)", fontsize=16, fontweight="bold", y=0.98)

    # 1. Panel 1: Top Toys by Revenue (Horizontal Bar Chart)
    ax1 = axes[0, 0]
    toy_rev = df.groupby("Toy Name")["Total Line Revenue"].sum().sort_values(ascending=True)
    bars = ax1.barh(toy_rev.index, toy_rev.values, color="#1f77b4", edgecolor="black", height=0.6)
    ax1.set_title("Revenue by Product (USD $)", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Total Revenue ($)")
    ax1.set_xlim(0, max(toy_rev.values) * 1.18)
    for bar in bars:
        w = bar.get_width()
        ax1.text(w + 80, bar.get_y() + bar.get_height() / 2, f"${w:,.0f}", va="center", fontsize=8)

    # 2. Panel 2: Monthly Sales Trend (Seasonality)
    ax2 = axes[0, 1]
    monthly = df.groupby("YearMonth")["Total Line Revenue"].sum()
    x_labels = [str(p) for p in monthly.index]
    ax2.plot(x_labels, monthly.values, marker="o", color="#d62728", linewidth=2, markersize=5)
    ax2.set_title("Monthly Sales Trend (Q4 Holiday Surge)", fontsize=12, fontweight="bold")
    ax2.set_ylabel("Revenue ($)")
    ax2.set_xticks(range(0, len(x_labels), 3))
    ax2.set_xticklabels([x_labels[i] for i in range(0, len(x_labels), 3)], rotation=40, ha="right")

    # 3. Panel 3: Age Distribution by Toy Brand (Seaborn Boxplot)
    ax3 = axes[1, 0]
    sns.boxplot(data=df, x="Toy Company", y="Purchaser Age", palette=["#4c72b0", "#dd8452"], ax=ax3, width=0.4)
    ax3.set_title("Purchaser Age Spread by Toy Brand", fontsize=12, fontweight="bold")
    ax3.set_xlabel("Toy Brand")
    ax3.set_ylabel("Purchaser Age (Years)")

    # 4. Panel 4: Payment Tender Method by Member Status (Seaborn Countplot)
    ax4 = axes[1, 1]
    sns.countplot(
        data=df,
        x="Payment",
        hue="Member?",
        order=df["Payment"].value_counts().index,
        palette="muted",
        ax=ax4
    )
    ax4.set_title("Payment Methods Segmented by Member Status", fontsize=12, fontweight="bold")
    ax4.set_xlabel("Payment Tender")
    ax4.set_ylabel("Transaction Count")
    ax4.legend(title="Member?", loc="upper right")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    # Save the chart image
    save_file = Path(output_path)
    plt.savefig(save_file, dpi=300)
    print(f"Visual dashboard saved successfully to: {save_file.resolve()}")
    try:
        plt.show()
    except Exception:
        pass


if __name__ == "__main__":
    csv_file = find_sales_csv()
    df_cleaned = load_and_clean_data(csv_file)
    print_executive_summary(df_cleaned)
    generate_visual_dashboard(df_cleaned, output_path="sales_dashboard.png")
