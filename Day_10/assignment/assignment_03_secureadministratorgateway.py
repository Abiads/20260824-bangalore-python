"""
### Assignment 3: Secure Administrator Gateway
#### Scenario
You are developing an administrative gateway. Access to the control panel requires validation. If credentials pass, the router redirects the administrator to the dashboard; if they fail, they are directed to an unauthorized error page.

#### Problem Description
Implement a Flask application containing the following endpoints:
1. **Route `/login` (GET, POST)**:
   - **`GET` Request**: Returns a string containing a raw HTML form with two input text boxes (names `"username"` and `"password"`) pointing to `POST /login`:
     ```html
     <form method="POST" action="/login">
         Username: <input type="text" name="username"><br>
         Password: <input type="password" name="password"><br>
         <input type="submit" value="Login">
     </form>
     ```
   - **`POST` Request**: Reads the form parameters `username` and `password` from `request.form`.
     - If `username` matches `"admin"` **and** `password` matches `"cdac@acts2026"`:
       - Redirect the client to the `/dashboard` route (using `redirect(url_for('dashboard'))`).
     - If the credentials do not match:
       - Redirect the client to the `/login-failed` route.
2. **Route `/dashboard` (GET)**:
   - Returns a formatted HTML page heading: `"<h1>Welcome to the Admin Dashboard!</h1>"`.
3. **Route `/login-failed` (GET)**:
   - Returns a JSON error response payload: `{"status": "Unauthorized", "message": "Invalid credentials provided."}` with an HTTP status code of `401`.

---
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
