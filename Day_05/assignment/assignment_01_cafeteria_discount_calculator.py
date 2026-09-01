"""
### Assignment 1: CDAC Cafeteria Discount Calculator
#### Scenario
The CDAC Cafeteria needs a modular pricing function to calculate student bills. The cafeteria offers main combo meals, optional side-dishes, standard tax rates, promotional discounts, and delivery charges.

#### Problem Description
Write a function named `calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0)` that calculates the final bill.
1. `base_price` (float): The cost of the main combo meal.
2. `*items` (floats): A variable-length positional argument list representing prices of additional side items.
3. `tax_rate` (float): The tax percentage (default `0.05` for 5% tax). This **must** be a keyword-only parameter.
4. `discount` (float): A percentage value (e.g., `10.0` represents a 10% discount, default `0.0`) applied directly to the subtotal before taxes.
5. `delivery_fee` (float): A flat shipping surcharge added to the final total after taxes (default `0.0`).

**Calculation Rules:**
1. Sum the `base_price` and all side item prices (`*items`) to compute the raw subtotal.
2. Deduct the discount from the raw subtotal to compute the discounted subtotal:
   $$\text{Discounted Subtotal} = \text{Raw Subtotal} \times \left(1 - \frac{\text{discount}}{100}\right)$$
3. Compute the tax value by multiplying the discounted subtotal by `tax_rate`.
4. Add the tax and `delivery_fee` to the discounted subtotal to get the final bill.
5. Return the final total rounded to **2 decimal places**.

#### Example Walkthrough
```python
# 1. Standard meal, no sides, default tax, no discount, no delivery
total1 = calculate_cafeteria_bill(100.0)
# Subtotal = 100.0
# Tax = 100.0 * 0.05 = 5.0
# Return: 105.00

# 2. Meal with sides, custom tax rate, 10% discount, flat delivery fee
total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
# Raw Subtotal = 100.0 + (20.0 + 30.0) = 150.0
# Discounted Subtotal = 150.0 * (1 - 10/100) = 135.0
# Tax = 135.0 * 0.08 = 10.8
# Final Total = 135.0 + 10.8 + 15.0 = 160.8
# Return: 160.80
```
"""

def calculate_cafeteria_bill(base_price: float, *items: float, tax_rate: float = 0.05, discount: float = 0.0, delivery_fee: float = 0.0) -> float:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    total1 = calculate_cafeteria_bill(100.0)
    print("Total 1:", total1)  # Expected: 105.00
    
    total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
    print("Total 2:", total2)  # Expected: 160.80

