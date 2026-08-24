# Day 10 Practice Assignments: Advanced Visualization & Flask/Django

## Objective
Configure interactive charts and build routing handlers in Python micro-frameworks.

---

### Exercise 1: Plotly Scatter Plots
Write a script using `plotly.graph_objects` or `plotly.express` to generate an interactive 2D scatter plot:
* Use a random distribution of 50 data points (X and Y coordinates).
* Style the markers (dots) based on a third numerical array representing size or color intensity.
* Show the interactive chart in the browser with hover text labels on the points.

---

### Exercise 2: Flask Routing and Templates
Build a micro-web application using Flask that includes:
1. A route `/greet/<name>` that returns a customized HTML message reading: `"Hello, [name]! Welcome to CDAC."`
2. A route `/square/<int:num>` that calculates the square of the integer passed in the URL path and returns it as a JSON payload: `{"number": num, "square": num * num}`.

---

### Exercise 3: Interactive Stock Prices Chart
Write a program using `plotly.express` to plot interactive line charts representing mock stock prices for three different tech companies over a 30-day window, permitting the user to hover and toggle individual graphs.

---

### Exercise 4: Flask Redirect Handlers
Write a Flask route `/login` that accepts a POST request containing a username form input.
* If user writes `"admin"`, redirect to a page `/dashboard` rendering a welcome page.
* If user writes anything else, redirect to `/login-failed`.

---

### Exercise 5: Django MVT Architecture Layout
Write a markdown document inside your Day 10 folder explaining how a URL request flows through Django's MVT (Model-View-Template) system, detailing which files (`urls.py`, `views.py`, `models.py`, templates) are involved at each step.

---

### Exercise 6: Interactive Population Bar Chart
Use Plotly to generate a horizontal bar chart displaying the population statistics of 10 major countries. Color the bars based on the continent the country belongs to.

---

### Exercise 7: Nested JSON API response
Implement a Flask route `/api/students` that returns a nested JSON list of students, where each student has nested details representing their courses and scores.

---

### Exercise 8: Custom CSS styling in Jinja Templates
Expand the Flask greeting application to use external stylesheets (`style.css`) placed inside a `static` folder. Style the background, fonts, and headings of the templates.
