"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
