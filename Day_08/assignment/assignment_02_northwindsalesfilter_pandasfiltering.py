"""
### Assignment 2: Northwind Sales Filter (Pandas Filtering)
#### Scenario
An analyst needs to query the historical sales data in `Northwind_Orders.csv` to evaluate individual salesperson performance. You need to write a filter that retrieves order details for a specific employee and destination country.

#### Problem Description
Write a function `filter_sales_by_employee(csv_path, employee_name, target_country)`:
1. `csv_path` is a string pointing to `Northwind_Orders.csv`.
2. **Load Data**: Read the CSV file into a Pandas DataFrame.
3. **Filtering**: Filter the DataFrame to find all rows where:
   - `"employee_name"` matches `employee_name` (case-sensitive, e.g. `"Steven Buchanan"`).
   - `"ship_country"` matches `target_country` (case-sensitive, e.g. `"France"`).
4. **Slicing**: Extract only the columns: `["order_id", "product_name", "total_item_revenue"]`.
5. **Return**: The filtered subset DataFrame. Keep the original index of the matching rows. If no rows match, return an empty DataFrame with columns `["order_id", "product_name", "total_item_revenue"]`.

#### Example Walkthrough
```python
csv_path = "Northwind_Orders.csv"
sales_df = filter_sales_by_employee(csv_path, "Steven Buchanan", "France")
print(sales_df.head(2))

# Expected Console Output:
#     order_id             product_name  total_item_revenue
# 0      10248           Queso Cabrales               168.0
# 1      10248  Singaporean Hokkien...                98.0
```

---

## Medium Assignments
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
