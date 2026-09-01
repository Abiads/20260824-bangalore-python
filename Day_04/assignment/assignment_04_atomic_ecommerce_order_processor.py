"""
### Assignment 4: Atomic E-Commerce Order Processor
#### Scenario
You are building an ordering subsystem for an online store. Orders containing multiple products must be processed **atomically**: either the entire order completes successfully, or the entire transaction fails. If one item in the order is out of stock or is unrecognized, no stock should be deducted for any other item (rollback).

#### Problem Description
1. Define two custom exceptions:
   - `ProductNotFoundError` (raised when a product ID is not present in the catalog).
   - `OutOfStockError` (raised when the customer's ordered quantity exceeds the available stock).
2. Write a function `process_order(catalog, order)`:
   - `catalog` is a dictionary containing product database records. Format:
     ```python
     catalog = {
         "P01": {"price": 100.0, "stock": 5},
         "P02": {"price": 50.0, "stock": 2}
     }
     ```
   - `order` is a dictionary containing product IDs (keys) and quantities ordered (values). Format: `{"P01": 2, "P02": 1}`.
   - **Validation Phase**: Before modifying any inventory levels:
     - Check if all ordered keys exist in the catalog. If a product ID does not exist, raise `ProductNotFoundError` with message: `"Product '<product_id>' not found in store catalog."`
     - Check if the catalog contains sufficient stock for each item ordered. If the ordered quantity exceeds available stock, raise `OutOfStockError` with message: `"Product '<product_id>' is out of stock. Requested: <requested_qty>, Available: <available_stock>."`
   - **Execution Phase**: If (and only if) all products pass validation:
     - Deduct the ordered quantities from the stock numbers in the catalog dictionary.
     - Calculate and return the total cost of the order (float).
     - If an exception was raised during validation, the catalog must remain completely unchanged.

#### Example Walkthrough
```python
catalog = {
    "P01": {"price": 10.0, "stock": 5},
    "P02": {"price": 20.0, "stock": 10}
}

# 1. Successful Order
total = process_order(catalog, {"P01": 2, "P02": 1})
# Returns: 40.0
# Catalog stock changes to: P01 stock = 3, P02 stock = 9

# 2. Failed Order (Triggers Rollback)
# Current Catalog: {"P01": {"price": 10.0, "stock": 3}, "P02": {"price": 20.0, "stock": 9}}
try:
    total = process_order(catalog, {"P01": 2, "P02": 15})
except OutOfStockError as e:
    print(e) # Output: Product 'P02' is out of stock. Requested: 15, Available: 9.

# Verify Catalog Stock: P01 must remain at 3 (NOT decreased to 1).
print(catalog["P01"]["stock"]) # Output: 3
```
"""

class ProductNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass

def process_order(catalog: dict, order: dict) -> float:
    for pid, qty in order.items():
        if pid not in catalog:
            raise ProductNotFoundError(f"Product '{pid}' not found in store catalog.")
        
        available_stock = catalog[pid]["stock"]
        if qty > available_stock:
            raise OutOfStockError(
                f"Product '{pid}' is out of stock. Requested: {qty}, Available: {available_stock}."
            )
    total_cost = 0.0
    for pid, qty in order.items():
        catalog[pid]["stock"] -= qty
        total_cost += catalog[pid]["price"] * qty
        
    return total_cost


if __name__ == "__main__":
    store_catalog = {
        "P01": {"price": 10.0, "stock": 5},
        "P02": {"price": 20.0, "stock": 10}
    }
    
    print("Initial Catalog:", store_catalog)
    
    order_1 = {"P01": 2, "P02": 1}
    cost = process_order(store_catalog, order_1)
    print(f"Order 1 Total Cost: {cost}")
    print("Catalog after Order 1:", store_catalog)
    
    order_2 = {"P01": 2, "P02": 15}
    try:
        process_order(store_catalog, order_2)
    except OutOfStockError as e:
        print("Caught expected OutOfStockError:", e)
        
    print("Catalog after failed Order 2 (unmodified):", store_catalog)
