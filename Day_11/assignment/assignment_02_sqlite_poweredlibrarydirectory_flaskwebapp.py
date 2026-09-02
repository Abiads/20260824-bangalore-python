"""
### Assignment 2: SQLite-Powered Library Directory (Flask Web App)
#### Scenario
You are developing a library registry database portal. The backend needs to query book registers from an SQLite database and display them on a web page, and allow users to append new book titles using an HTML form.

#### Problem Description
Implement a complete Flask web application connected to a local SQLite database named `library.db`:
1. **Database Setup**:
   - In your initialization code, check if the table `books` exists. If not, create it:
     `id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT`.
2. **Flask Routes**:
   - **`GET /books`**:
     - Establishes an SQLite database connection and queries all records from the `books` table.
     - Formats and returns an HTML list string containing the book records. Each book must be rendered inside a list element:
       `<li><strong><title></strong> by <author></li>`.
     - Include a simple HTML form pointing to `POST /add-book` at the bottom of the page:
       ```html
       <form method="POST" action="/add-book">
           Title: <input type="text" name="title"><br>
           Author: <input type="text" name="author"><br>
           <input type="submit" value="Add Book">
       </form>
       ```
   - **`POST /add-book`**:
     - Extracts the form fields `"title"` and `"author"` from the request (`request.form.get()`).
     - **Validation**: If either parameter is missing or empty, return a plain text error message `"Error: Title and Author are required!"` with an HTTP status code of `400`.
     - If both are valid, execute a parameterized SQL INSERT query to append the book record to `library.db`, commit the changes, and redirect the client to `/books` (using `redirect(url_for('list_books'))` or direct path).
3. Ensure cursors and database connections are closed cleanly inside each route handler.

*Note: Define the Flask app instance variable as `app`.*
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
