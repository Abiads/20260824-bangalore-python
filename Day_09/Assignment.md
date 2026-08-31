# Day 9 Practice Assignments: Pandas Wrangling & Data Visualization (Static & Interactive)

## Objective
Apply Pandas operations for missing data cleaning, column concatenation, table merging/joining, grouping aggregates, and pivot table construction. Render custom charts using Matplotlib/Seaborn and interactive figures using Plotly Express on the real `Northwind_Orders.csv` dataset.

---

## Easy Assignments

### Assignment 1: Northwind Order Shipped Date Sanitizer
#### Scenario
The shipping logs in `Northwind_Orders.csv` contain missing shipped dates for orders that are still in transit. Before executing monthly calculations, you need to clean these nulls based on the destination country.

#### Problem Description
Write a function `sanitize_order_dates(df)` that processes the Northwind orders DataFrame:
1. `df` is the Pandas DataFrame loaded from `Northwind_Orders.csv`.
2. **Conditional Shipped Date Fill**:
   - For rows where the `"shipped_date"` is null (`NaN`):
     - If the shipping destination country (`"ship_country"`) is `"USA"` or `"Canada"`, fill the missing `"shipped_date"` with `"In-Transit: Domestic"`.
     - If it is any other country, fill it with `"In-Transit: International"`.
3. **Region Fill**:
   - For rows where `"ship_region"` is null (`NaN`), fill it with the string `"No-Region"`.
4. **Return**: The sanitized DataFrame.

#### Example Walkthrough
```python
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("Northwind_Orders.csv")

# Verify there are missing shipped dates
print("Null dates before:", df["shipped_date"].isna().sum())

clean_df = sanitize_order_dates(df)

# Verify nulls are resolved
print("Null dates after:", clean_df["shipped_date"].isna().sum())
print(clean_df[clean_df["shipped_date"].str.startswith("In-Transit")][["ship_country", "shipped_date"]].head(2))
```

---

### Assignment 2: Interactive Freight Cost Trend Visualizer
#### Scenario
A logistics coordinator requires an interactive line graph showing shipping freight charges handled by different carrier firms over time. The graph must allow toggling shipping lines and hovering to view exact shipment costs.

#### Problem Description
Write a function `generate_freight_chart(df, output_html_path)`:
1. `df` is the Pandas DataFrame loaded from `Northwind_Orders.csv`.
2. **Interactive Charting**:
   - Use Plotly Express (`plotly.express` as `px`) to generate a line chart (`px.line()`):
     - Set the X-axis to `"order_date"`.
     - Set the Y-axis to `"freight"`.
     - Set the line color category to `"shipper_company_name"`.
     - Enable markers on the data points.
     - Add a custom title: `"Northwind Order Freight Costs by Shipping Carrier"`.
3. **Save**: Save the interactive chart as a standalone HTML file to `output_html_path` using `fig.write_html()`.

---

## Medium Assignments

### Assignment 3: Product Supplier Performance Reconciler
#### Scenario
You have product catalog details and order transactions stored in separate sheets. To evaluate supplier performance, you must join these tables and aggregate total sales quantity and revenue per supplier.

#### Problem Description
Write a function `reconcile_supplier_performance(df_orders, df_suppliers)`:
1. `df_orders` is a DataFrame with columns: `["order_id", "product_id", "total_item_revenue", "quantity_ordered"]`.
2. `df_suppliers` is a DataFrame with columns: `["product_id", "supplier_company_name", "supplier_country"]`.
3. **Merge**: Perform an **inner join** on `"product_id"` using `pd.merge()`.
4. **Aggregation**: Group the records by `"supplier_company_name"`. Calculate:
   - The sum of `"total_item_revenue"` (rename/store as `"Total_Revenue"`).
   - The sum of `"quantity_ordered"` (rename/store as `"Total_Quantity"`).
5. **Return**: A new DataFrame indexed by `"supplier_company_name"` containing the columns `["Total_Revenue", "Total_Quantity"]`. Sort the resulting DataFrame's index alphabetically.

#### Example Walkthrough
```python
import pandas as pd

# Extract subsets from main dataset to simulate separate tables
df_full = pd.read_csv("Northwind_Orders.csv")
orders_subset = df_full[["order_id", "product_id", "total_item_revenue", "quantity_ordered"]]
suppliers_subset = df_full[["product_id", "supplier_company_name", "supplier_country"]].drop_duplicates()

summary_df = reconcile_supplier_performance(orders_subset, suppliers_subset)
print(summary_df.head(3))

# Expected Console Output:
#                             Total_Revenue  Total_Quantity
# supplier_company_name                                    
# Aux joyeux ecclésiastiques       33827.65             769
# Bigfoot Breweries                26335.50             940
# Cooperativa de Quesos...         21980.20             800
```

---

### Assignment 4: Interactive Product Sales Bubble Plot
#### Scenario
To perform pricing analysis, a sales manager wants a bubble plot comparing catalog list prices (X-axis) against order quantities (Y-axis). The bubble sizes must represent total item revenue, colored by the product's category.

#### Problem Description
Write a function `generate_product_sales_bubble(df, output_html_path)`:
1. `df` is the Pandas DataFrame loaded from `Northwind_Orders.csv`.
2. **Plotting**:
   - Use Plotly Express to generate an interactive scatter plot (`px.scatter()`):
     - Set the X-axis to `"list_unit_price"`.
     - Set the Y-axis to `"quantity_ordered"`.
     - Set the bubble sizes (`size` parameter) to `"total_item_revenue"`.
     - Set the colors (`color` parameter) to `"category_name"`.
     - Set the hover overlay name label (`hover_name` parameter) to `"product_name"`.
     - Add the title: `"Product Sales Analysis: Price, Quantity & Revenue"`.
3. **Save**: Save the interactive chart as a standalone HTML file to `output_html_path` using `fig.write_html()`.

---

## Difficult Assignments

### Assignment 5: Employee Monthly Sales Summary & Pivot Table
#### Scenario
Sales coordinators need to analyze monthly revenue generated by each employee across different product categories. You need to write a module that parses order dates, classifies high-value transactions, and builds a summary pivot table.

#### Problem Description
Write a function `generate_employee_monthly_pivot(df)`:
1. `df` is the Pandas DataFrame loaded from `Northwind_Orders.csv`.
2. **Date Standardizing**: Parse the `"order_date"` column into standard Pandas Datetime objects using `pd.to_datetime()`.
3. **Extract Month**: Extract the full month name (e.g. `"July"`, `"August"`) from the datetime column and store it in a new column named `"order_month"`.
4. **Value Classification**: Add a new column named `"value_class"`:
   - If `"total_item_revenue"` is strictly greater than `1000.0`, the row's value is `"Premium"`.
   - Otherwise, the value is `"Regular"`.
   - Perform this classification using vectorized checks (such as `np.where()`).
5. **Pivot Table**: Build a pivot table summarizing the transactions:
   - **Index (Rows)**: `"employee_name"`
   - **Columns**: `"category_name"`
   - **Values**: Sum of `"total_item_revenue"`
   - Set the pivot table's aggregation function to `"sum"`. Fill any empty pivot intersections (`NaN`) with the value `0.0`.
6. **Return**: The resulting pivot table DataFrame.

---

### Assignment 6: Interactive Category Revenue by Country Dashboard
#### Scenario
Executive leadership requires a country-level e-commerce dashboard. You need to write a module that filters out discontinued products, groups revenues by category and country, and builds an interactive side-by-side grouped bar plot.

#### Problem Description
Write a function `generate_category_country_dashboard(df, output_html_path)`:
1. `df` is the Pandas DataFrame loaded from `Northwind_Orders.csv`.
2. **Data Wrangling**:
   - Filter out and drop all rows where `"product_discontinued"` matches `1` (representing discontinued items).
   - Group the remaining transactions by both `"customer_country"` and `"category_name"`.
   - Calculate the sum of `"total_item_revenue"` for each group.
   - Reset the index of the aggregated DataFrame.
3. **Grouped Bar Plot**:
   - Use Plotly Express to construct a grouped bar plot (`px.bar()`):
     - Set the X-axis to `"category_name"`.
     - Set the Y-axis to `"total_item_revenue"`.
     - Set the bar color category to `"customer_country"`.
     - Set the bar positioning mode (`barmode` parameter) to `"group"` (side-by-side columns).
     - Add the title: `"Northwind Category Revenue by Customer Country (Active Products)"`.
4. **Save**: Save the interactive chart as a standalone HTML file to `output_html_path` using `fig.write_html()`.
