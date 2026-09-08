"""
Day 11 - Practice Exercise 4: Profit Margin Distribution Plot
============================================================
Task:
    Using Seaborn, generate a histogram with a KDE curve
    (sns.histplot(data=df, x='Profit_Margin_Pct', kde=True))
    to visualize which profit margins are most common across transactions.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


def plot_profit_margin_distribution(
    file_path: Path | None = None,
    output_image: str = "exercise4_margin_distribution.png",
    show_plot: bool = True,
) -> pd.Series:
    """Calculates profit margins and visualizes their distribution using Seaborn."""
    if file_path is None:
        file_path = get_dataset_path()

    print(f"Loading dataset from: {file_path}")
    df = pd.read_csv(file_path)

    # Clean currency columns
    for col in ["Total Line Revenue", "Total COGS"]:
        df[col] = (
            df[col]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.strip()
            .astype(float)
        )

    # Calculate profit margin percentage
    df["Profit_Margin_Pct"] = (
        (df["Total Line Revenue"] - df["Total COGS"]) / df["Total Line Revenue"]
    ) * 100

    margin_stats = df["Profit_Margin_Pct"].describe()
    print("\n" + "=" * 55)
    print("           PROFIT MARGIN SUMMARY STATISTICS           ")
    print("=" * 55)
    print(margin_stats.round(2))
    print("=" * 55)

    # Plot histogram with KDE
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5.5))

    sns.histplot(
        data=df,
        x="Profit_Margin_Pct",
        kde=True,
        bins=15,
        color="#17becf",
        edgecolor="white",
        line_kws={"linewidth": 2.5, "color": "#1f77b4"},
        ax=ax,
    )

    # Reference lines for mean and median
    mean_margin = df["Profit_Margin_Pct"].mean()
    median_margin = df["Profit_Margin_Pct"].median()
    ax.axvline(mean_margin, color="#d62728", linestyle="--", linewidth=1.8, label=f"Mean: {mean_margin:.1f}%")
    ax.axvline(median_margin, color="#2ca02c", linestyle=":", linewidth=1.8, label=f"Median: {median_margin:.1f}%")

    ax.set_title("Distribution of Transaction Profit Margins (%)", fontsize=14, fontweight="bold", pad=12)
    ax.set_xlabel("Profit Margin (%)", fontsize=11)
    ax.set_ylabel("Number of Transactions", fontsize=11)
    ax.legend(loc="upper left")

    plt.tight_layout()

    # Determine save path relative to script directory
    script_dir = Path(__file__).parent if "__file__" in globals() else Path(".")
    save_path = script_dir / output_image
    plt.savefig(save_path, dpi=300)
    print(f"\nPlot successfully saved to: {save_path.resolve()}")

    if show_plot:
        plt.show()

    plt.close()
    return df["Profit_Margin_Pct"]


if __name__ == "__main__":
    plot_profit_margin_distribution(show_plot=False)
