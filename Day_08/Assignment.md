# Day 8 Practice Assignments: NumPy & SciPy Foundations

## Objective
Apply NumPy operations for data normalization, boolean filtering, matrix transformations, and dot products on the Northwind dataset. Access Pandas DataFrames loaded from `Northwind_Orders.csv` using `.loc` and `.iloc` slicing, and compute shipping cost optimizations using SciPy.

---

## Easy Assignments

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

---

## Difficult Assignments

### Assignment 5: Coordinates Alignment for Port Shipments (NumPy Linear Algebra)
#### Scenario
A shipping port logs the $(x, y)$ coordinate offsets of customer cities relative to a central hub. To calibrate satellite distances, the coordinates must be translated relative to a new port dock and rotated to align with the camera angle.

#### Problem Description
Write a function `align_customer_coordinates(coordinates, angle_degrees, dock_offset)`:
1. `coordinates` is a 2D NumPy array of shape `(N, 2)` representing $(x, y)$ coordinate offsets.
2. `angle_degrees` is the rotation angle in degrees (float). Convert this angle to radians:
   $$\theta = \text{angle\_degrees} \times \frac{\pi}{180}$$
3. Construct the 2D **Rotation Matrix** $R$:
   $$R = \begin{pmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{pmatrix}$$
4. **Determinant Verification**: Calculate the determinant of the rotation matrix $R$ using `np.linalg.det(R)`.
   - If the absolute difference between the determinant and `1.0` is greater than `1e-6` (i.e. $|\text{det} - 1.0| > 10^{-6}$), raise a `ValueError` with the message `"Invalid rotation matrix."`
5. **Transformation Sequence**:
   - **Translation**: Translate the points by adding `dock_offset` (a 1D array of shape `(2,)` representing $[dx, dy]$) to `coordinates` using broadcasting.
   - **Rotation**: Rotate the translated points by multiplying them by the rotation matrix.
     $$\text{Aligned Coordinates} = \text{Translated Coordinates} \times R^T$$
6. Return a tuple containing: `(rotation_determinant, aligned_coordinates)`.

#### Example Walkthrough
```python
import numpy as np

coords = np.array([
    [10.0, 0.0],
    [0.0, 10.0],
    [10.0, 10.0]
])
offset = np.array([-5.0, 5.0])
angle = 90.0

det, aligned = align_customer_coordinates(coords, angle, offset)
print(det)  # Output: 1.0 (very close to 1.0)
print(np.round(aligned))
# Step 1: Translate -> [[5.0, 5.0], [-5.0, 15.0], [5.0, 15.0]]
# Step 2: Rotate 90 deg -> [[-5.0, 5.0], [-15.0, -5.0], [-15.0, 5.0]]
```

---

### Assignment 6: Shipping Cost Decay Optimizer (SciPy Optimization)
#### Scenario
A logistics company analyzes Northwind shipping freight costs. The average freight charge per unit decays exponentially as the total quantity of items ordered in a batch increases. The freight charge is modeled by:
$$\text{freight}(q) = a \cdot e^{-b \cdot q} + 10.0$$
where $q$ is the quantity ordered, $a$ is the maximum shipping surcharge, and $b$ is the cost decay coefficient. You need to write a SciPy optimization script to fit parameters $a$ and $b$ to observed transaction data by minimizing the Sum of Squared Errors (SSE).

#### Problem Description
Write a function `optimize_freight_model(quantity_array, observed_freight_array)`:
1. `quantity_array` is a 1D NumPy array representing quantities $q$.
2. `observed_freight_array` is a 1D NumPy array of the same size representing observed freight costs.
3. **Objective Error Function**: Define a local error function `calculate_sse(params)`:
   - `params` is a list or tuple: `[a, b]`.
   - Calculate the modeled freight for each quantity $q$ in `quantity_array`:
     $$\text{modeled}(q) = a \cdot e^{-b \cdot q} + 10.0$$
   - Compute and return the Sum of Squared Errors (SSE) between the model and observed data:
     $$\text{SSE} = \sum \left( \text{modeled}(q) - \text{observed}(q) \right)^2$$
4. **Optimization**:
   - Use `scipy.optimize.minimize` to find parameters `[a, b]` that minimize `calculate_sse`.
   - Set the initial guess to `[100.0, 0.05]`.
   - Enforce parameter bounds to ensure physical validity: $a \ge 0.0$ and $b \ge 0.001$.
5. **Return**: A dictionary containing:
   `{"a": opt_a, "b": opt_b, "sse": min_sse}`
   where all values are rounded to **4 decimal places**.

#### Example Walkthrough
```python
import numpy as np

# Mock experimental data (quantities and matching observed freights)
q_data = np.array([5, 10, 15, 20, 30, 40, 50])
observed_f = np.array([90.5, 75.2, 60.1, 50.8, 35.4, 25.1, 18.0])

fit_results = optimize_freight_model(q_data, observed_f)
print(fit_results)
# Expected Output format:
# {'a': <value>, 'b': <value>, 'sse': <value>}
```
