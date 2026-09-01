# Day 9: Data Wrangling with Pandas & Data Visualization (Static & Interactive)

Welcome to Day 9! Today we will expand our Pandas data analytics toolkit and explore data visualization using both static and interactive plotting libraries. We will cover:
1. **Data Wrangling & Cleansing**: Detecting nulls, filling/dropping missing entries, and string manipulation.
2. **Merging & Joining**: Reconciling different relational DataFrames using joins.
3. **Grouping & Aggregations**: Compiling database-like groupings and multi-aggregations.
4. **Pivot Tables**: Reshaping tables to summarize metrics across index-column intersections.
5. **Static Visualization (Matplotlib)**: Plotting line graphs, bar charts, and pie charts with axis metadata.
6. **Enhanced Plots (Seaborn)**: Styling box plots, scatter plots, and distribution trends.
7. **Interactive Visualization (Plotly)**: Generating dynamic line charts, bubble charts, and grouped bar plots that support zooming, hovering, and toggling series.

> [!NOTE]
> **Jupyter Notebook & Virtual Environment Recommended**: For the data science and plotting modules (Days 8 and 9), it is highly recommended to run your code inside an isolated virtual environment and use Jupyter Notebooks.
>
> **Step A: Setup & Activate Virtual Environment**
> * macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
> * Windows (CMD): `python -m venv .venv && .venv\Scripts\activate.bat`
> * Windows (PS): `python -m venv .venv && .venv\Scripts\Activate.ps1`
>
> **Step B: Install Packages & Run Jupyter**
> 1. Install packages: `pip install jupyter numpy scipy pandas matplotlib seaborn plotly`
> 2. Launch Jupyter: `jupyter notebook` (or open the `.ipynb` file in VS Code selecting the `.venv` kernel).

---

## Part 1: Data Wrangling & Cleansing in Pandas

Real-world datasets contain anomalies, missing attributes, or raw text columns. We must sanitize this data before modeling. We use the **[Northwind_Orders.csv](../Northwind_Orders.csv)** dataset.

### 1. Handling Missing Data
* `isna()` / `isnull()`: Returns a boolean mask of elements that are null.
* `fillna(value)`: Replaces null values with a specified constant, column mean, or interpolation.

```python
import pandas as pd

# Load the Northwind dataset
df = pd.read_csv("Northwind_Orders.csv")

# 1. Detect missing values across all columns
print("Missing values per column:\n", df.isna().sum())

# 2. Fill missing values in 'ship_region' with a default string
df["ship_region"] = df["ship_region"].fillna("Unknown")
print("\nMissing values in ship_region after fill:", df["ship_region"].isna().sum())
```

### 2. String Manipulation on Columns
Pandas provides a `.str` accessor to execute vectorized string operations.
```python
# Convert category names to lowercase
df["category_name"] = df["category_name"].str.lower()

# Create a composite product descriptor key: "category: product_name"
df["product_descriptor"] = df["category_name"] + ": " + df["product_name"]
print(df[["product_descriptor"]].head(3))
```

---

## Part 2: Merging and Joining DataFrames

To combine relational datasets based on shared keys, use `pd.merge()`. Here we merge our main orders dataset with a supplementary table mapping countries to continents.

```python
# 1. Create a supplementary DataFrame mapping countries to continents
continent_data = pd.DataFrame({
    "customer_country": ["Germany", "Mexico", "UK", "Sweden", "France", "Spain", "Canada", "Argentina", "Brazil", "USA"],
    "continent": ["Europe", "North America", "Europe", "Europe", "Europe", "Europe", "North America", "South America", "South America", "North America"]
})

# 2. Left Join: Merge continent info into our main orders DataFrame on 'customer_country'
df_merged = pd.merge(df, continent_data, on="customer_country", how="left")
print(df_merged[["order_id", "customer_country", "continent"]].head(5))
```

---

## Part 3: Grouping & Aggregations

The `.groupby()` method splits a DataFrame into groups and applies aggregate operations (like sum, mean, count).

```python
# Group by category name and sum the quantities and revenue
category_summary = df.groupby("category_name")[["quantity_ordered", "total_item_revenue"]].sum()
print("Category Summaries:\n", category_summary)

# Group by employee name and get multiple statistics on their transactions (.agg)
employee_stats = df.groupby("employee_name")["total_item_revenue"].agg(["sum", "mean", "count"])
print("\nEmployee Sales Statistics:\n", employee_stats.head(5))
```

---

## Part 4: Pivot Tables

A pivot table summarizes metrics across row-column intersections.

```python
# Create pivot table summarizing sales revenue by Country (rows) and Category (columns)
pivot_df = df.pivot_table(
    index="customer_country", 
    columns="category_name", 
    values="total_item_revenue", 
    aggfunc="sum", 
    fill_value=0.0
)
print("Sales Pivot Table:\n", pivot_df.head(5))
```

---

## Part 5: Static Visualization (Matplotlib & Seaborn)

### 1. Basic Line Plots (Matplotlib)
Plot monthly sales revenue trends.

```python
import matplotlib.pyplot as plt

# Parse date and extract year-month
df["order_date"] = pd.to_datetime(df["order_date"])
df["year_month"] = df["order_date"].dt.to_period("M")

# Group and calculate monthly revenue
monthly_revenue = df.groupby("year_month")["total_item_revenue"].sum()

# Convert PeriodIndex to strings for plotting
months_str = [str(m) for m in monthly_revenue.index]

plt.figure(figsize=(10, 4))
plt.plot(months_str, monthly_revenue.values, color="green", marker="o", linestyle="-", label="Monthly Revenue")
plt.title("Northwind Sales Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.close()
```

### 2. Statistical Box Plots (Seaborn)
Show the distribution of unit prices sold across different product categories.

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
sns.set_theme(style="whitegrid")

# Create box plot
sns.boxplot(data=df, x="category_name", y="unit_price_sold", palette="Set3")
plt.title("Product Unit Prices Sold by Category")
plt.xlabel("Product Category")
plt.ylabel("Unit Price Sold ($)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("category_price_distribution.png")
plt.close()
```

---

## Part 6: Interactive Visualization (Plotly)

Unlike Matplotlib and Seaborn, **Plotly** generates interactive HTML objects, permitting users to toggle legend items, zoom in, and hover to see coordinates.

```python
import plotly.express as px

# Create an interactive scatter plot comparing quantity ordered and price sold
fig = px.scatter(
    df.head(500), # Plot first 500 rows for performance
    x="list_unit_price", 
    y="quantity_ordered", 
    size="total_item_revenue", 
    color="category_name", 
    hover_name="product_name",
    title="Product Orders: Price vs Quantity (First 500 records)"
)

# Save as a standalone HTML file
fig.write_html("interactive_orders_plot.html")
```

---

## Practical Examples (Interactive & Runnable)

### Example 1: Sales Analysis by Category
Aggregates total revenue per category and saves a static horizontal bar chart.

```python
import pandas as pd
import matplotlib.pyplot as plt

def analyze_category_sales(csv_path, output_image_path):
    df = pd.read_csv(csv_path)
    
    # Calculate total revenue per category
    category_sales = df.groupby("category_name")["total_item_revenue"].sum().sort_values()
    
    plt.figure(figsize=(10, 5))
    category_sales.plot(kind="barh", color="coral")
    plt.title("Total Revenue by Product Category")
    plt.xlabel("Total Revenue ($)")
    plt.ylabel("Product Category")
    plt.tight_layout()
    plt.savefig(output_image_path)
    plt.close()
    print("Category Sales Analysis Completed.")

analyze_category_sales("Northwind_Orders.csv", "category_revenue.png")
```

### Example 2: Interactive Customer Sales Bubble Plot (Plotly)
Aggregates sales performance by customer country and plots it interactively.

```python
import plotly.express as px
import pandas as pd

def build_country_sales_distribution(csv_path, output_html_path):
    df = pd.read_csv(csv_path)
    
    # Group by customer country and compute statistics
    country_df = df.groupby("customer_country").agg(
        total_revenue=("total_item_revenue", "sum"),
        total_quantity=("quantity_ordered", "sum"),
        unique_products=("product_id", "nunique")
    ).reset_index()
    
    # Generate interactive scatter/bubble chart
    fig = px.scatter(
        country_df,
        x="total_quantity",
        y="total_revenue",
        size="unique_products",
        color="customer_country",
        hover_name="customer_country",
        title="Country-level Sales Performance (Bubble Size = Unique Products Purchased)"
    )
    
    fig.write_html(output_html_path)
    print(f"Interactive bubble plot written to {output_html_path}")

build_country_sales_distribution("Northwind_Orders.csv", "country_sales_bubble.html")
```
