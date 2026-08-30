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
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    catalog = {
        "P01": {"price": 10.0, "stock": 5},
        "P02": {"price": 20.0, "stock": 10}
    }
    # Test valid and invalid orders

