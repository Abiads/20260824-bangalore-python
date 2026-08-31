"""
### Assignment 1: Product Order Vector Processor (NumPy Vectorization)
#### Scenario
You are writing a billing module for the Northwind e-commerce system. The system processes order items by calculating subtotals, applying discounts, and computing final checkout costs.

#### Problem Description
Write a function `process_order_vector(quantities, unit_prices, discounts)`:
1. The parameters are lists of size 5 containing item details from an order:
   - `quantities` (list of integers): The count of items ordered.
   - `unit_prices` (list of floats): The list price per unit.
   - `discounts` (list of floats): The discount percentage per item (e.g. `0.05` represents a 5% discount).
2. **Vector Conversion**: Convert all three input lists into 1D NumPy arrays.
3. **Calculations**:
   - Calculate the **raw subtotal** for each of the 5 items:
     $$\text{Subtotal} = \text{quantities} \times \text{unit\_prices}$$
     *(Perform this as a vectorized element-wise multiplication; do not write loops).*
   - Calculate the **discounted price** for each of the 5 items:
     $$\text{Discounted Price} = \text{Subtotal} \times (1.0 - \text{discounts})$$
   - Calculate the **total order cost** by summing all of the discounted prices.
4. **Return**: A tuple containing:
   `(subtotals_array, discounted_prices_array, total_order_cost)`.

#### Example Walkthrough
```python
import numpy as np

qty = [2, 10, 5, 1, 4]
prices = [15.0, 10.0, 20.0, 100.0, 25.0]
disc = [0.0, 0.10, 0.0, 0.05, 0.20]

subtotals, final_prices, total = process_order_vector(qty, prices, disc)

print(subtotals)    # Output: [ 30. 100. 100. 100. 100.]
print(final_prices) # Output: [30. 90. 100. 95. 80.]
print(total)        # Output: 395.0
```

---
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
