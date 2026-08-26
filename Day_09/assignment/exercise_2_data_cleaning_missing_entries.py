"""
Exercise 2: Data Cleaning (Missing Entries)

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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
