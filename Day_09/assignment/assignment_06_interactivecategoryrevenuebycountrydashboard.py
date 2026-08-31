"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
