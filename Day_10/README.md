# Day 10: Web Frameworks (Part 1) — Introduction & Core Routing

Welcome to Day 10! Today we explore web development concepts and micro-framework web routing in Python. We will cover:
1. **Web Architectures**: Understanding Client-Server request cycles and MVC (Model-View-Controller) / MTV (Model-Template-View) design patterns.
2. **Comparing Frameworks**: Highlighting differences between lightweight Flask micro-frameworks and full-stack Django platforms.
3. **Flask Routing**: Defining routes, handling path parameters (strings, integers), and parsing HTTP methods (GET, POST).
4. **Jinja2 Templates & Redirects**: Dynamically rendering HTML views, executing form validations, and routing users using redirect hooks.
5. **Web API endpoints**: Returning clean JSON payloads and binding REST endpoints to SQLite databases.

> [!NOTE]
> **Prerequisites**: It is highly recommended to run the web server examples and assignments inside an isolated virtual environment.
>
> **Step A: Setup & Activate Virtual Environment**
> * macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
> * Windows (CMD): `python -m venv .venv && .venv\Scripts\activate.bat`
> * Windows (PS): `python -m venv .venv && .venv\Scripts\Activate.ps1`
>
> **Step B: Install Flask**
> ```bash
> pip install flask
> ```

---

## Part 1: Web Architectures & Frameworks

### 1. Client-Server Flow
```text
+----------+      HTTP Request (URL, GET/POST)     +----------+
|  Client  | ------------------------------------> |  Server  |
| (Browser)| <------------------------------------ | (Python) |
+----------+      HTTP Response (HTML/JSON, 200/404) +----------+
```

### 2. MVC vs. MTV Architectures
* **MVC (Model-View-Controller)**:
  - **Model**: Manages database access and business logic.
  - **View**: Renders visual representation (HTML page).
  - **Controller**: Coordinates between Model and View, handling requests.
* **MTV (Model-Template-View)**: Used by **Django**.
  - **Model**: Database layer (same as MVC).
  - **Template**: Renders pages (similar to MVC View).
  - **View**: Acts as Controller (handles requests, loads models, maps templates).

### 3. Flask vs. Django
| Feature | Flask | Django |
| :--- | :--- | :--- |
| **Philosophy** | Micro-framework (modular, simple, choose-your-own-addons). | Full-stack (opinionated, "batteries-included" toolkit). |
| **Database Support** | No native database ORM (must import extensions like SQLAlchemy). | Built-in ORM, admin panel, and automatic migrations. |
| **Best For** | Microservices, lightweight web APIs, quick prototyping. | Large-scale enterprise applications, complex web applications. |

---

## Part 2: Flask Micro-framework Basics

### 1. Simple App Setup & Path Parameters
```python
from flask import Flask, jsonify

app = Flask(__name__)

# Basic GET route returning plain text
@app.route("/")
def home():
    return "Welcome to the API!"

# Dynamic path parameter: <student_name> matches string parameter
@app.route("/greet/<student_name>")
def greet(student_name):
    return f"<h1>Hello, {student_name}!</h1>"

# Dynamic integer parameter: <int:num> converts path parameter to int
@app.route("/square/<int:num>")
def calculate_square(num):
    result = num ** 2
    # Returns a JSON response with HTTP 200
    return jsonify({"input": num, "square": result}), 200

if __name__ == "__main__":
    # Start local development server
    app.run(debug=True, port=5000)
```

### 2. Handling POST Requests & Redirects
Use `request.form` to parse incoming HTML form inputs, and `redirect()` to guide navigation.

```python
from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Basic form template
form_html = """
<form method="POST" action="/login">
    Username: <input type="text" name="user_input"><br>
    <input type="submit" value="Submit">
</form>
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Extract form field named 'user_input'
        username = request.form.get("user_input")
        if username == "admin":
            # Redirect to the dashboard view
            return redirect(url_for("dashboard"))
        return "Unauthorized Access!", 403
    return render_template_string(form_html)

@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome Administrator.</h1>"

if __name__ == "__main__":
    app.run(debug=True)
```

---

## Practical Examples (Interactive & Runnable)

### Example: SQLite database API micro-service (Flask)
Demonstrates setting up a Flask app that queries database tables and returns JSON results based on request arguments.

```python
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'Alice')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'Bob')")
    conn.commit()
    conn.close()

@app.route("/api/users", methods=["GET"])
def get_users():
    # Read query parameter e.g., /api/users?name=Alice
    filter_name = request.args.get("name")
    
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    if filter_name:
        cursor.execute("SELECT * FROM users WHERE name = ?", (filter_name,))
    else:
        cursor.execute("SELECT * FROM users")
        
    rows = cursor.fetchall()
    conn.close()
    
    # Build list of dicts
    users_list = [{"id": r[0], "name": r[1]} for r in rows]
    return jsonify(users_list), 200

if __name__ == "__main__":
    init_db()
    # Runs in standard background mode
    # app.run(port=5000)
```
