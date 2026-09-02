# Day 10 Practice Assignments: Web Frameworks (Part 1) — Routing & Core Templates

## Objective
Implement Flask applications containing dynamic routes, path variable conversion, conditional redirection, in-memory state tracking, database-connected API querying, and JSON payload validation.

---

## Easy Assignments

### Assignment 1: Academic Greeting Web App
#### Scenario
You are developing a student registration microservice. The routing module needs dynamic handlers to parse student names and compute grades passed as URL path variables.

#### Problem Description
Implement a complete Flask web application containing the following routes:
1. **Route `/` (GET)**:
   - Returns the plain text message: `"Welcome to the CDAC PGCP-AI Registration Portal."`
2. **Route `/greet/<student_name>` (GET)**:
   - Dynamically parses the `<student_name>` variable from the URL path.
   - Returns a formatted HTML heading: `"<h1>Hello, <student_name>! Welcome to CDAC.</h1>"`.
3. **Route `/calculate/grade/<int:marks_obtained>/<int:total_marks>` (GET)**:
   - **Validation**: If `total_marks` is less than or equal to `0`, return a JSON response: `{"error": "Total marks must be greater than zero."}` with an HTTP status code of `400`.
   - **Success**: Calculate the percentage:
     $$\text{Percentage} = \frac{\text{marks\_obtained}}{\text{total\_marks}} \times 100$$
     Round the value to **1 decimal place** (e.g. `82.5`).
   - Return a JSON response: `{"obtained": <marks_obtained>, "total": <total_marks>, "percentage": <percentage>}` with an HTTP status code of `200`.

*Note: Define the Flask app instance variable as `app`. Ensure `app.run` is enclosed within `if __name__ == '__main__':` so it does not block import statements during testing.*

#### Example Walkthrough
* Requesting `GET /greet/Lisa` returns the HTML: `<h1>Hello, Lisa! Welcome to CDAC.</h1>`
* Requesting `GET /calculate/grade/45/50` returns the JSON payload:
  `{"obtained": 45, "total": 50, "percentage": 90.0}` with HTTP 200.
* Requesting `GET /calculate/grade/45/0` returns the JSON payload:
  `{"error": "Total marks must be greater than zero."}` with HTTP 400.

---

### Assignment 2: Dynamic Temperature Converter Web App
#### Scenario
A weather application microservice requires API endpoints to convert temperatures between Celsius and Fahrenheit scales dynamically using float path parameters.

#### Problem Description
Implement a Flask application with the following endpoints:
1. **Route `/convert/c_to_f/<float:celsius>` (GET)**:
   - Takes a floating-point temperature value in Celsius from the path.
   - Performs the conversion to Fahrenheit:
     $$F = C \times 1.8 + 32$$
   - Returns a JSON response: `{"celsius": <celsius>, "fahrenheit": <fahrenheit>}` (with both values rounded to **1 decimal place**) and an HTTP status code of `200`.
2. **Route `/convert/f_to_c/<float:fahrenheit>` (GET)**:
   - Takes a floating-point temperature value in Fahrenheit from the path.
   - Performs the conversion to Celsius:
     $$C = \frac{F - 32}{1.8}$$
   - Returns a JSON response: `{"fahrenheit": <fahrenheit>, "celsius": <celsius>}` (with both values rounded to **1 decimal place**) and an HTTP status code of `200`.

#### Example Walkthrough
* Requesting `GET /convert/c_to_f/0.0` returns JSON:
  `{"celsius": 0.0, "fahrenheit": 32.0}` with HTTP 200.
* Requesting `GET /convert/f_to_c/100.0` returns JSON:
  `{"fahrenheit": 100.0, "celsius": 37.8}` with HTTP 200.

---

## Medium Assignments

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

### Assignment 4: CDAC Course Enrollment System
#### Scenario
A course catalog registrar tracks student enrollments. You need to write a Flask controller that processes course selections via post form fields, stores enrollments in an in-memory roster list, validates duplicate registrations, and permits clearing logs.

#### Problem Description
Implement a Flask application with the following parameters and routes:
1. ** Roster Storage**: Initialize a global list in your script named `ENROLLED_COURSES = []`.
2. **Route `/enroll` (GET, POST)**:
   - **`GET` Request**: Returns an HTML string showing the current list of enrolled courses as a comma-separated list: `"Enrolled: <course1>, <course2>..."`. If no courses are enrolled, display `"Enrolled: None"`.
     - Below the list, include an HTML form to submit new enrollments:
       ```html
       <form method="POST" action="/enroll">
           Course Name: <input type="text" name="course_name"><br>
           <input type="submit" value="Enroll">
       </form>
       ```
   - **`POST` Request**: Reads the form parameter `"course_name"` from the form.
     - Strip any leading/trailing spaces from `"course_name"`.
     - **Validation**:
       - If `"course_name"` is empty, return a plain text error `"Error: Course name cannot be empty."` with HTTP status code `400`.
       - If `"course_name"` (case-insensitive) already exists in the `ENROLLED_COURSES` list, return a plain text error `"Error: Already enrolled in <course_name>."` with HTTP status code `400`.
     - **Success**: Append the original `"course_name"` to `ENROLLED_COURSES`, and redirect the user back to `GET /enroll` with HTTP status code `303` (See Other).
3. **Route `/enroll/clear` (POST)**:
   - Clears all elements from the global `ENROLLED_COURSES` list.
   - Redirects the client back to `/enroll` with HTTP status code `303`.

---

## Difficult Assignments

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

---

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
