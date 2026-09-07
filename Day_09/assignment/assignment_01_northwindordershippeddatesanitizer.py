"""
### Assignment 1: Northwind Order Shipped Date Sanitizer
#### Scenario
The shipping logs in `Northwind_Orders.csv` contain missing shipped dates for orders that are still in transit. Before executing monthly calculations, you need to clean these nulls based on the destination country.

#### Problem Description
Write a function `sanitize_order_dates(df)` that processes the Northwind orders DataFrame:
1. `df` is the Pandas DataFrame loaded from `Northwind_Orders.csv`.
2. **Conditional Shipped Date Fill**:
   - For rows where the `"shipped_date"` is null (`NaN`):
     - If the shipping destination country (`"ship_country"`) is `"USA"` or `"Canada"`, fill the missing `"shipped_date"` with `"In-Transit: Domestic"`.
     - If it is any other country, fill it with `"In-Transit: International"`.
3. **Region Fill**:
   - For rows where `"ship_region"` is null (`NaN`), fill it with the string `"No-Region"`.
4. **Return**: The sanitized DataFrame.

#### Example Walkthrough
```python
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("Northwind_Orders.csv")

# Verify there are missing shipped dates
print("Null dates before:", df["shipped_date"].isna().sum())

clean_df = sanitize_order_dates(df)

# Verify nulls are resolved
print("Null dates after:", clean_df["shipped_date"].isna().sum())
print(clean_df[clean_df["shipped_date"].str.startswith("In-Transit")][["ship_country", "shipped_date"]].head(2))
```
"""
import pandas as pd
import numpy as np

def solve():
    df = pd.read_csv("Northwind_Orders.csv")

    # Ensure shipped_date is treated as string-like or NaN
    # Fill null shipped_date based on ship_country
    # 1. Define the condition: ship_country is USA or Canada
    domestic_condition = df["ship_country"].isin(["USA", "Canada"])
    
    # 2. Use loc with np.nan to find nulls that satisfy the condition
    df.loc[domestic_condition & df["shipped_date"].isna(), "shipped_date"] = "In-Transit: Domestic"
    
    # 3. Fill the remaining null shipped_date values (International)
    df["shipped_date"] = df["shipped_date"].fillna("In-Transit: International")

    # Fill null ship_region with "No-Region"
    df["ship_region"] = df["ship_region"].fillna("No-Region")

    print("Null dates after:", df["shipped_date"].isna().sum())
    print(df[df["shipped_date"].str.startswith("In-Transit")][["ship_country", "shipped_date"]].head(2))

if __name__ == "__main__":
    solve()
