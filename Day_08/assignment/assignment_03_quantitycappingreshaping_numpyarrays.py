"""
### Assignment 3: Quantity Capping & Reshaping (NumPy Arrays)
#### Scenario
An inventory forecast model processes transaction quantities from `Northwind_Orders.csv`. Due to stocking limits, any quantity ordering count above a threshold must be identified and capped, and the flat data must be reshaped into a grid for analysis.

#### Problem Description
Write a function `cap_and_grid_quantities(quantities_list, max_allowed_qty)`:
1. `quantities_list` is a list of 24 integers representing product quantities ordered in transactions.
2. **Boolean Masking**: Convert the list to a 1D NumPy array. Create a boolean mask to locate all elements in the array that are strictly greater than `max_allowed_qty`. Count the number of elements that exceed this threshold.
3. **Capping**: Replace all values in the array that exceed `max_allowed_qty` with `max_allowed_qty`.
4. **Reshaping**: Reshape the capped 1D array into a 2D array of shape `(6, 4)` (6 rows, 4 columns).
5. **Column Averages**: Calculate the average quantity along the columns (mean along axis 0).
6. **Return**: A tuple containing:
   `(capped_count, reshaped_grid, column_averages_array)`.

#### Example Walkthrough
```python
import numpy as np

raw_qtys = [12, 10, 5, 9, 40, 10, 35, 15, 6, 15, 20, 40, 25, 40, 6, 15, 12, 40, 20, 30, 2, 8, 4, 30]

count, grid, col_avgs = cap_and_grid_quantities(raw_qtys, 25)
print(count)      # Output: 6  (values 40, 35, 40, 40, 40, 30 are capped)
print(grid.shape) # Output: (6, 4)
print(col_avgs)   # Output: 1D array of 4 average values (axis 0)
```

---
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
