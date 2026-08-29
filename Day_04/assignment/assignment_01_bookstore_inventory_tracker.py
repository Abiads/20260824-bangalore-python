"""
Assignment 1: Inventory Tracker for CDAC Bookstore

Scenario:
The CDAC Bookstore needs a backend helper module to manage books and their quantities.
The inventory is stored in a Python dictionary where keys are book titles (strings)
and values are quantities in stock (non-negative integers).

Problem Description:
Write a function `manage_bookstore_inventory(inventory, action, book_title, quantity=0)`:
1. `action` can be "add", "sell", or "lookup".
2. "add": Add specified quantity to stock. If not present, create new key.
3. "sell": Decrease stock by quantity.
   - If not found: Print "Error: Book '<book_title>' not found in inventory."
   - If quantity > stock: Print "Error: Insufficient stock for '<book_title>'. Available: <current_stock>."
   - If stock becomes exactly 0: Remove book key entirely.
4. "lookup": Return current stock quantity (or 0 if not found, using safe dictionary access).

Returns the updated inventory dictionary (or stock value for lookup).
"""

def manage_bookstore_inventory(inventory: dict, action: str, book_title: str, quantity: int = 0):
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    inventory = {"Python Basics": 10, "Learning AI": 5}
    print("Initial:", inventory)
    
    # Test your function
    inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
    print("After add:", inventory)

