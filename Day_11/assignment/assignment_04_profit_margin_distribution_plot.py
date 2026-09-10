from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

csv_path = Path(__file__).resolve().parent / "Sales.csv"
if not csv_path.exists():
    csv_path = Path("Sales.csv")

df = pd.read_csv(csv_path)
for col in ["Total Line Revenue", "Total COGS"]:
    df[col] = df[col].astype(str).str.replace("$", "", regex=False).str.strip().astype(float)

df["Profit_Margin_Pct"] = ((df["Total Line Revenue"] - df["Total COGS"]) / df["Total Line Revenue"]) * 100

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=df, x="Profit_Margin_Pct", kde=True, bins=15, color="#17becf", edgecolor="white", ax=ax)
ax.set_title("Distribution of Transaction Profit Margins (%)", fontsize=13, fontweight="bold")
ax.set_xlabel("Profit Margin (%)")
ax.set_ylabel("Number of Transactions")

plt.tight_layout()
plt.savefig(Path(csv_path).parent / "exercise4_margin_distribution.png", dpi=300)
plt.show()
