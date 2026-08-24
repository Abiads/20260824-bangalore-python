# Day 09 Practice Assignments: Pandas Wrangling & Data Visualization

## Objective
Perform data cleanups, group data aggregates, and render comparative plots.

---

### Exercise 1: Grouping and Aggregation
Using the employee DataFrame from Day 8:
1. Group the employees by `Department`.
2. Compute the average and maximum salary for each department.
3. Print the aggregated summary.

---

### Exercise 2: Data Cleaning (Missing Entries)
Create a DataFrame with missing values:
```python
import pandas as pd
import numpy as np
data = {
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Score': [85, np.nan, 90, np.nan, 95],
    'Age': [20, 21, np.nan, 22, 20]
}
df = pd.DataFrame(data)
```
1. Fill the missing values in `Score` with the mean score of the remaining students.
2. Fill the missing values in `Age` using the forward-fill method (`ffill`).
3. Print the cleaned DataFrame.

---

### Exercise 3: Temperature Variation Plot
You are given average monthly temperature data for City A and City B.
```python
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temp_A = [15, 17, 22, 28, 33, 35, 34, 32, 30, 26, 20, 16]
temp_B = [5, 8, 12, 18, 22, 26, 28, 27, 23, 17, 11, 7]
```
Write a python program using `matplotlib.pyplot` to plot a line graph showing the temperature trends of both cities over the months:
* Set labels for X and Y axes.
* Include a legend to distinguish City A and City B.
* Add gridlines to the plot.

---

### Exercise 4: Merging and Joining DataFrames
Create two DataFrames:
* `df_emp`: columns `Emp_ID`, `Name`, `Dept_Code`
* `df_dept`: columns `Dept_Code`, `Dept_Name`, `Location`
Write a program to perform a **left join** and an **inner join** of these DataFrames using Pandas' `pd.merge()`.

---

### Exercise 5: Sales Pivot Table
Given a DataFrame representing product sales transactions:
```python
sales_data = {
    'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
    'Product': ['Apple', 'Apple', 'Banana', 'Banana', 'Apple', 'Banana'],
    'Sales': [1200, 1500, 800, 1100, 1300, 1200]
}
```
Create a pivot table showing the total sales summarized by `Region` (rows) and `Product` (columns).

---

### Exercise 6: Correlation Scatter Plot
Write a script using Seaborn to plot a scatter plot demonstrating correlation between two numeric variables in the Seaborn built-in `"tips"` dataset (e.g., plot `total_bill` vs `tip`). Add a regression trendline.

---

### Exercise 7: Distribution Pie Chart
Using Matplotlib, plot a pie chart showing the categorical distribution of student grade distributions (e.g., count of A's, B's, C's, etc.) from a custom list of marks. Add percentage labels.

---

### Exercise 8: Outlier Detection Box Plot
Create a box plot using Seaborn to display the distribution of salaries across different departments, highlighting any potential outliers in the dataset.
