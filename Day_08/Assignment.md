# Day 08 Practice Assignments: NumPy & SciPy Foundations

## Objective
Use NumPy arrays for mathematical conversions, matrix multiplications, and boolean filters.

---

### Exercise 1: Identity and Diagonal Arrays
1. Use NumPy to create a 5x5 Identity matrix.
2. Extract the diagonal elements.
3. Replace the diagonal values with the number `9` and print the resulting matrix.

---

### Exercise 2: Matrix Multiplications
Create two 3x3 NumPy matrices filled with random integers between 1 and 10.
1. Perform element-wise multiplication.
2. Perform standard dot product matrix multiplication.
3. Print the determinant of the first matrix (Hint: Use `np.linalg.det`).

---

### Exercise 3: Pandas Indexing and Slicing
Create a Pandas DataFrame from the following dictionary:
```python
data = {
    'Employee_ID': [101, 102, 103, 104, 105],
    'Name': ['Kishori', 'Rajan', 'Esha', 'Revati', 'Vinod'],
    'Department': ['HR', 'IT', 'Finance', 'Design', 'IT'],
    'Salary': [45000, 60000, 55000, 50000, 70000]
}
```
1. Print the first 3 rows of the DataFrame.
2. Filter and print employees who work in the `'IT'` department.
3. Find the average salary of the employees in the dataset.

---

### Exercise 4: Array Shape Conversions
Create a 1D NumPy array with 24 sequential integers from 1 to 24.
1. Reshape the array into a 2D matrix of size 4x6.
2. Reshape the array into a 3D matrix of size 2x3x4.
3. Verify that the array elements match in all states.

---

### Exercise 5: Finding Maxima Indices along Axes
Create a 4x4 random matrix using NumPy.
1. Find the index of the maximum value of the entire matrix.
2. Find the index of the maximum values along each column (axis 0).
3. Find the index of the maximum values along each row (axis 1).

---

### Exercise 6: SciPy Local Minima Finder
Write a Python script using `scipy.optimize` to find the local minimum of the quadratic equation:
$$f(x) = x^2 + 10\sin(x) + 2$$
Print the optimized coordinates of $x$.

---

### Exercise 7: Standard Normalizing Scale
Write a function that accepts a 2D NumPy array and normalizes its column features so that all values in each column are scaled to range between 0 and 1.
* **Normalization Formula**: $X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}$

---

### Exercise 8: Date Column Transformations in Pandas
Create a Pandas Series containing a list of date strings (e.g., `["2026-08-01", "2026-08-15"]`). Convert them into datetime objects, and extract the year, month, and day components into a structured DataFrame.
