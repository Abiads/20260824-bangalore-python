"""
### Assignment 4: Shipping Freight Slicing (Pandas loc vs. iloc)
#### Scenario
The logistics team audits shipping freight costs in `Northwind_Orders.csv`. You need to write two slicing functions to extract chunks of freight transactions using both row labels and integer coordinates.

#### Problem Description
Write two separate slicing functions:
1. **`extract_freight_by_label(df, start_row_label, end_row_label, col_names)`**:
   - Uses label-based indexing (`.loc`) to slice the DataFrame from `start_row_label` to `end_row_label` (inclusive) and extract only the columns listed in `col_names`.
   - Returns the sliced DataFrame.
2. **`extract_freight_by_position(df, row_start_idx, row_end_idx, col_indices)`**:
   - Uses position-based indexing (`.iloc`) to slice the DataFrame from row index `row_start_idx` to `row_end_idx` (exclusive) and columns at integer indices specified in the list `col_indices`.
   - Returns the sliced DataFrame.

#### Example Walkthrough
```python
import pandas as pd

df = pd.read_csv("Northwind_Orders.csv")

# Slicing rows 10 to 12 (inclusive) with columns 'order_id' and 'freight'
loc_res = extract_freight_by_label(df, 10, 12, ["order_id", "freight"])
print(loc_res)

# Slicing rows 10 to 12 (exclusive, i.e. 10 and 11) with columns index 0 (order_id) and 13 (freight)
iloc_res = extract_freight_by_position(df, 10, 12, [0, 13])
print(iloc_res)
```
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
