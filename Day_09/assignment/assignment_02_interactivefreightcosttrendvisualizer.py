"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
