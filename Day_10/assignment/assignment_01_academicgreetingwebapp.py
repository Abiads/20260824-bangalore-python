"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
