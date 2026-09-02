"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
