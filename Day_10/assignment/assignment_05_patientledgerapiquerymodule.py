"""
### Assignment 5: Patient Ledger API & Query Module
#### Scenario
A hospital database tracks patient check-ups. You are writing a Flask web API to query patient tables. The API must receive optional query filters, compile dynamic parameterized SQL statements safely, and return structured JSON records.

#### Problem Description
Implement a Flask application connected to a local SQLite database named `clinic.db`:
1. **Database Initialization**:
   - Before the app receives requests, check if the table `patients` exists. If not, create it:
     `id INTEGER PRIMARY KEY, name TEXT, age INTEGER, ailment TEXT, doctor TEXT`.
   - If the table is empty, insert three dummy records:
     - `(1, "John Doe", 45, "Flu", "Dr. Smith")`
     - `(2, "Jane Roe", 30, "Migraine", "Dr. Jones")`
     - `(3, "Bob Vance", 50, "Flu", "Dr. Smith")`
2. **API Endpoint 1: `GET /api/patients`**:
   - Expect optional search parameters in the query string (`request.args`): `ailment` and `doctor`.
   - **Dynamic SQL**: Compile a safe parameterized SQL SELECT statement dynamically:
     - If `ailment` is provided, append `WHERE ailment = ?` to the query.
     - If `doctor` is provided, append `AND doctor = ?` (or `WHERE doctor = ?` if no ailment was provided).
     - Execute the query on `clinic.db` using parameter lists/tuples. Do not format parameters directly into the query string.
   - **Response**: Map matching rows to dictionaries:
     `{"id": row[0], "name": row[1], "age": row[2], "ailment": row[3], "doctor": row[4]}`.
     Return this list as a JSON payload using `jsonify()` with an HTTP status code of `200`.
3. **API Endpoint 2: `POST /api/patients/add`**:
   - Extract json parameters `name`, `age`, `ailment`, and `doctor` using `request.get_json()`.
   - **Validation**: If any parameter is missing, or if `age` is not a positive integer, return a JSON error payload: `{"status": "Bad Request", "error": "Missing or invalid fields."}` with an HTTP status code of `400`.
   - **Execution**: Insert the new record into `clinic.db` using a parameterized SQL query. Commit changes.
   - **Response**: Return a success JSON payload: `{"status": "Created", "message": "Patient record added successfully."}` with an HTTP status code of `201`.
4. Ensure all database connections and cursors are closed cleanly inside your route handlers.
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
