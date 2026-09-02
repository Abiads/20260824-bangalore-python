"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
