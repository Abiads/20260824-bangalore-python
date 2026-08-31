"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
