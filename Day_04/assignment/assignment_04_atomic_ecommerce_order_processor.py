"""
Assignment 4: Atomic E-Commerce Order Processor

Scenario:
Atomic order processing: all items must succeed or transaction rolls back completely.

Problem Description:
1. Define custom exceptions:
   - `ProductNotFoundError`
   - `OutOfStockError`
2. `process_order(catalog, order)`:
   - Validation Phase:
     - Check if all product IDs exist in catalog (raise `ProductNotFoundError("Product '<id>' not found in store catalog.")`).
     - Check if catalog has enough stock (raise `OutOfStockError("Product '<id>' is out of stock. Requested: <qty>, Available: <stock>.")`).
   - Execution Phase:
     - Deduct stock from catalog.
     - Calculate and return total cost (float).
"""

class ProductNotFoundError(Exception):
    pass

class OutOfStockError(Exception):
    pass

def process_order(catalog: dict, order: dict) -> float:
    # 1. Validation Phase (Checks without modifying state)
    for prod_id, qty in order.items():
        if prod_id not in catalog:
            raise ProductNotFoundError(f"Product '{prod_id}' not found in store catalog.")
        avail = catalog[prod_id]["stock"]
        if qty > avail:
            raise OutOfStockError(f"Product '{prod_id}' is out of stock. Requested: {qty}, Available: {avail}.")
            
    # 2. Execution Phase
    total = 0.0
    for prod_id, qty in order.items():
        catalog[prod_id]["stock"] -= qty
        total += catalog[prod_id]["price"] * qty
        
    return total

if __name__ == "__main__":
    catalog = {
        "P01": {"price": 10.0, "stock": 5},
        "P02": {"price": 20.0, "stock": 10}
    }
    total = process_order(catalog, {"P01": 2, "P02": 1})
    print("Order 1 Total:", total)
    print("Catalog after Order 1:", catalog)
    
    try:
        process_order(catalog, {"P01": 2, "P02": 15})
    except OutOfStockError as e:
        print("Caught expected OutOfStockError:", e)
    print("Catalog after failed order (verified atomic):", catalog)

