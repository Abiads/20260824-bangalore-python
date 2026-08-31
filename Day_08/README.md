# Day 8: Data Science Foundations — NumPy & Pandas (Part 1)

Welcome to Day 8! Today we begin our data science module, transitioning from general-purpose programming to numerical data processing and tabular data analysis. We will cover:
1. **NumPy Fundamentals**: Array creation, shapes, sizes, and dimensions.
2. **Indexing & Slicing**: 1D and 2D arrays, and filtering using boolean masks.
3. **Vectorization & Linear Algebra**: Mathematical operations, matrix multiplication, and aggregates.
4. **Introduction to SciPy**: Optimization and curve minimization.
5. **Introduction to Pandas**: Series, DataFrames, indexing with `.loc`/`.iloc`, and filtering.

> [!NOTE]
> **Jupyter Notebook & Virtual Environment Recommended**: For the data science and plotting modules (Days 8 and 9), it is highly recommended to run your code inside an isolated virtual environment and use Jupyter Notebooks.
>
> **Step A: Setup & Activate Virtual Environment**
> * macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
> * Windows (CMD): `python -m venv .venv && .venv\Scripts\activate.bat`
> * Windows (PS): `python -m venv .venv && .venv\Scripts\Activate.ps1`
>
> **Step B: Install Packages & Run Jupyter**
> 1. Install packages: `pip install jupyter numpy scipy pandas matplotlib seaborn plotly`
> 2. Launch Jupyter: `jupyter notebook` (or open the `.ipynb` file in VS Code selecting the `.venv` kernel).

---

## Part 1: NumPy Fundamentals

**NumPy** (Numerical Python) is the foundational package for scientific computing in Python. It provides the **`ndarray`** (N-dimensional array) object, which is a fast, space-efficient container for homogeneous numerical data.

### 1. Why NumPy?
* **Contiguous Memory**: NumPy arrays are stored in contiguous blocks of memory, allowing vector processors to perform calculations at hardware speeds.
* **No Loops Required**: Operations on NumPy arrays are vectorized, meaning element-wise calculations are performed natively in compiled C code.

### 2. Creating Arrays
You can initialize NumPy arrays in several ways:

```python
import numpy as np

# 1. From a Python List
arr_from_list = np.array([1, 2, 3, 4])

# 2. Array of zeros or ones
zeros = np.zeros((3, 4))  # Shape: 3 rows, 4 columns
ones = np.ones((2, 3))    # Shape: 2 rows, 3 columns

# 3. Sequential ranges
seq_range = np.arange(0, 10, 2)  # Output: [0, 2, 4, 6, 8]

# 4. Linearly spaced intervals
linspace_arr = np.linspace(0, 1, 5)  # Output: [0.  , 0.25, 0.5 , 0.75, 1.  ]

# 5. Identity matrix
identity_matrix = np.eye(3)  # 3x3 Identity matrix
```

### 3. Array Properties
Every array has properties describing its structure:
```python
matrix = np.array([[10, 20], [30, 40]])

print("Dimensions:", matrix.ndim)  # Output: 2
print("Shape:", matrix.shape)      # Output: (2, 2)
print("Total size:", matrix.size)   # Output: 4
print("Data type:", matrix.dtype)   # Output: int64 (or int32)
```

---

## Part 2: Indexing, Slicing & Boolean Masking

### 1. 2D Array Slicing
Slicing in NumPy follows the syntax `array[row_slice, col_slice]`.

```python
# 3x3 matrix
mat = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Extract first two rows, last two columns
sub_mat = mat[0:2, 1:3]
print(sub_mat)
# Output:
# [[2 3]
#  [5 6]]

# Extract column at index 1
col_1 = mat[:, 1]
print(col_1)  # Output: [2, 5, 8]
```

### 2. Boolean Masking (Filtering)
You can filter arrays without loop conditions by applying comparison operations directly, which returns a boolean index mask.

```python
data = np.array([10, 15, 20, 25, 30])

# Create boolean mask
mask = data > 20
print("Mask:", mask)  # Output: [False, False, False, True, True]

# Apply mask
filtered_data = data[mask]
print("Filtered:", filtered_data)  # Output: [25, 30]
```

---

## Part 3: Vectorization & Linear Algebra

### 1. Element-wise Operations
Arithmetic operations on arrays apply element-by-element:
```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)  # Output: [5, 7, 9]
print(x * y)  # Output: [4, 10, 18] (Element-wise multiplication)
```

### 2. Matrix Multiplication
For standard linear algebra matrix multiplication, use the `@` operator or `np.dot()`:
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product
C = A @ B
print(C)
# Output:
# [[19 22]
#  [43 50]]
```

### 3. Aggregate Operations & Axes
You can aggregate values (sum, mean, max) across the entire matrix or along specific axes.
* `axis=0`: Operations perform **column-wise** (down rows).
* `axis=1`: Operations perform **row-wise** (across columns).

```python
numbers = np.array([
    [10, 20],
    [30, 40]
])

print("Total Sum:", np.sum(numbers))               # Output: 100
print("Column-wise Sum (axis=0):", np.sum(numbers, axis=0))  # Output: [40, 60]
print("Row-wise Mean (axis=1):", np.mean(numbers, axis=1))    # Output: [15., 35.]
print("Index of Max (flat):", np.argmax(numbers))  # Output: 3 (points to 40)
```

---

## Part 4: Introduction to SciPy

**SciPy** builds on the NumPy array object to provide algorithms for optimization, integration, interpolation, and statistics.

### Example: Optimizing a Mathematical Function
We use `scipy.optimize.minimize` to find the local minimum of a simple 1D quadratic curve: $f(x) = x^2 - 4x + 4$.

```python
from scipy.optimize import minimize

# Define the target function
def cost_function(x):
    return x**2 - 4*x + 4

# Provide initial guess
initial_guess = 0.0

# Run optimization
result = minimize(cost_function, initial_guess)

print("Optimization Successful:", result.success)
print("Minimum location x:", result.x[0])  # Output: 2.00000...
print("Minimum function value f(x):", result.fun) # Output: 0.0
```

---

## Part 5: Introduction to Pandas

While NumPy is ideal for homogeneous array calculations, **Pandas** is designed for working with heterogeneous (tabular) data (similar to a SQL table or Excel sheet). For this module, we will use the **[Northwind_Orders.csv](../Northwind_Orders.csv)** dataset.

### 1. Loading Data and Inspecting Properties
To load a CSV file, use `pd.read_csv()`.

```python
import pandas as pd

# Load the Northwind Orders dataset
df = pd.read_csv("Northwind_Orders.csv")

# Inspect basic properties
print("Shape (rows, columns):", df.shape)
print("\nColumn names:\n", list(df.columns[:10])) # Show first 10 columns
print("\nFirst 3 rows:\n", df.head(3))
```

### 2. Slicing with `.loc` vs. `.iloc`
* **`.loc`**: Label-based indexing (uses row index labels and column names).
* **`.iloc`**: Position-based indexing (uses integer offsets starting from 0).

```python
# Slicing with .loc (using column labels)
print("--- Slicing with .loc ---")
print(df.loc[0:2, ["product_name", "quantity_ordered", "total_item_revenue"]])

# Slicing with .iloc (using integer column positions)
# 2: product_name, 7: quantity_ordered, 9: total_item_revenue
print("\n--- Slicing with .iloc ---")
print(df.iloc[0:3, [2, 7, 9]])
```

### 3. Basic Aggregations & Column Operations
```python
# Compute aggregate statistics
average_revenue = df["total_item_revenue"].mean()
total_quantity = df["quantity_ordered"].sum()

print(f"Average Item Revenue: ${average_revenue:.2f}")
print(f"Total Items Ordered: {total_quantity}")
```

---

## Practical Examples (Interactive & Runnable)

### Example 1: Matrix Feature Scaling (Normalizer)
Using NumPy vectorization to scale features of an array to normal standard ranges $[0, 1]$.

```python
import numpy as np

def min_max_normalize(data_matrix):
    # Minimum and Maximum values of each column (axis=0)
    col_mins = np.min(data_matrix, axis=0)
    col_maxs = np.max(data_matrix, axis=0)
    
    # Range of each column
    col_ranges = col_maxs - col_mins
    
    # Scaled matrix: (X - min) / range
    # Broadcasting takes care of dimensions automatically
    scaled_matrix = (data_matrix - col_mins) / col_ranges
    return scaled_matrix

# Run Example
raw_features = np.array([
    [10.0, 100.0],
    [20.0, 300.0],
    [15.0, 200.0]
])

normalized = min_max_normalize(raw_features)
print("Normalized Features:\n", normalized)
```

### Example 2: Pandas Data Filtering and Column Transformations
Loads the Northwind Orders dataset, filters for high-value orders shipped to Germany, and extracts relevant sales details.

```python
import pandas as pd

# 1. Load the Northwind dataset
df = pd.read_csv("Northwind_Orders.csv")

# 2. Filter: select high-value items (> $2000.0) shipped to Germany
germany_high_value = df[(df["customer_country"] == "Germany") & (df["total_item_revenue"] > 2000.0)]

# 3. Slicing: get order ID, product name, customer name, and item revenue
summary = germany_high_value.loc[:, ["order_id", "product_name", "customer_company_name", "total_item_revenue"]]

print(f"Total matching items: {len(summary)}")
print("\nFirst 5 matching records:\n", summary.head(5))
```
