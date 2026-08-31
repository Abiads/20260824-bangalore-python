"""
### Assignment 6: Inventory Management API with JSON Schema Validation
#### Scenario
A warehouse stock-control ledger is exposed as a web service. The dashboard requires a RESTful JSON API to update quantity metrics of inventory parts. The API must validate incoming payload schemas, check item presence in SQLite databases, commit transaction edits, and handle error scenarios.

#### Problem Description
Implement a Flask application connected to a local SQLite database named `store.db`:
1. **Database Initialization**:
   - On start, verify if table `items` exists:
     `id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE, quantity INTEGER, price REAL`.
   - Pre-populate the table with two records if empty:
     - `("Laptop", 15, 1200.0)`
     - `("Mouse", 50, 25.0)`
2. **API Endpoint 1: `GET /api/items`**:
   - Queries and returns all rows in `items` table.
   - Maps columns to a list of dicts: `[{"id": row[0], "name": row[1], "quantity": row[2], "price": row[3]}, ...]`
   - Returns a JSON response with HTTP status code `200`.
3. **API Endpoint 2: `PUT /api/items/update`**:
   - Expects a JSON request body (`request.get_json()`) containing:
     - `"name"` (string)
     - `"quantity"` (integer)
   - **Schema Validation**:
     - Verify both `"name"` and `"quantity"` keys are present in the JSON body.
     - Check that `"quantity"` is an integer and is greater than or equal to `0`.
     - If the validation fails, return a JSON error response: `{"error": "Invalid request payload. Ensure name and non-negative integer quantity are provided."}` with an HTTP status code of `400`.
   - **Database Check & Update**:
     - Connect to `store.db`. Execute a query to check if an item matching `"name"` (case-sensitive) exists in the table.
     - If the item does not exist, return a JSON error response: `{"error": "Item '<name>' not found in inventory."}` with an HTTP status code of `404`.
     - If it exists, update its `"quantity"` to the new integer value. Commit the transaction.
     - Return a JSON success response: `{"message": "Stock updated successfully.", "name": "<name>", "new_quantity": <quantity>}` with an HTTP status code of `200`.
4. Close SQL connections and cursors cleanly within the route functions.
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
