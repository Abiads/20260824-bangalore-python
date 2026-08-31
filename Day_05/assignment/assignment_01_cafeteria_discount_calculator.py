"""
Assignment 1: CDAC Cafeteria Discount Calculator

Scenario:
The CDAC Cafeteria needs a modular pricing function to calculate student bills.
Offers main combo meals, optional side-dishes, tax, promotional discounts, and delivery.

Problem Description:
Write `calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0)`:
1. `base_price` (float): Cost of main meal.
2. `*items` (floats): Additional side item prices.
3. `tax_rate` (float): Keyword-only parameter (default 0.05).
4. `discount` (float): Percentage discount applied to subtotal before taxes (default 0.0).
5. `delivery_fee` (float): Shipping surcharge added after taxes (default 0.0).

Calculation:
- Raw Subtotal = base_price + sum(items)
- Discounted Subtotal = Raw Subtotal * (1 - discount/100)
- Tax = Discounted Subtotal * tax_rate
- Final Total = Discounted Subtotal + Tax + delivery_fee
- Return final total rounded to 2 decimal places.
"""

def calculate_cafeteria_bill(base_price: float, *items: float, tax_rate: float = 0.05, discount: float = 0.0, delivery_fee: float = 0.0) -> float:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    total1 = calculate_cafeteria_bill(100.0)
    print("Total 1:", total1)  # Expected: 105.00
    
    total2 = calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0)
    print("Total 2:", total2)  # Expected: 160.80

