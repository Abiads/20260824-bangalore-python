# Day 10: RESTful APIs with Flask & Numerical Computing with NumPy

Welcome to Day 10! Today's session bridges two foundational pillars of modern software engineering and data-driven Python development:

1. **RESTful Web Services using Flask**: Transitioning from traditional server-side rendered HTML applications (covered in Day 9) to building decoupled, stateless JSON web services that power Single Page Applications (React, Angular, Vue), mobile applications (iOS/Android), and distributed microservices.
2. **Numerical Computing with NumPy**: Entering the scientific and data science ecosystem. We explore why standard Python lists are inefficient for numerical computing, how NumPy achieves near-C performance through contiguous memory and vectorization, the mechanics of $N$-dimensional arrays (`ndarray`), indexing/slicing (and the critical view vs. copy distinction), universal functions, broadcasting rules, multi-axis aggregations, and practical data normalization.

---

## Table of Contents

- [Day 10: RESTful APIs with Flask \& Numerical Computing with NumPy](#day-10-restful-apis-with-flask--numerical-computing-with-numpy)
  - [Table of Contents](#table-of-contents)
- [SECTION A: Fundamentals of REST API using Flask](#section-a-fundamentals-of-rest-api-using-flask)
  - [Part 1: Architectural Foundations of REST](#part-1-architectural-foundations-of-rest)
    - [1. What is an API?](#1-what-is-an-api)
    - [2. Server-Side Rendering (SSR) vs. REST API Decoupling](#2-server-side-rendering-ssr-vs-rest-api-decoupling)
    - [3. Roy Fielding's 6 REST Architectural Constraints](#3-roy-fieldings-6-rest-architectural-constraints)
  - [Part 2: RESTful URI Design \& HTTP Semantics](#part-2-restful-uri-design--http-semantics)
    - [1. Resource-Oriented URI Conventions](#1-resource-oriented-uri-conventions)
    - [2. HTTP Verbs in REST Semantics](#2-http-verbs-in-rest-semantics)
    - [3. Safety and Idempotency Matrix](#3-safety-and-idempotency-matrix)
    - [4. Standard HTTP Status Codes in REST APIs](#4-standard-http-status-codes-in-rest-apis)
  - [Part 3: Core Flask Tools for REST APIs](#part-3-core-flask-tools-for-rest-apis)
    - [1. Returning JSON: `jsonify` vs. `json.dumps`](#1-returning-json-jsonify-vs-jsondumps)
    - [2. Parsing Incoming Requests: `request.get_json()` and `request.args`](#2-parsing-incoming-requests-requestget_json-and-requestargs)
    - [3. Dynamic URL Parameters and Variable Converters](#3-dynamic-url-parameters-and-variable-converters)
    - [4. Centralized Error Handling with `@app.errorhandler`](#4-centralized-error-handling-with-apperrorhandler)
  - [Part 4: Practical Project: Building a Products CRUD REST API with Flask \& SQLite](#part-4-practical-project-building-a-products-crud-rest-api-with-flask--sqlite)
    - [1. Project Structure](#1-project-structure)
    - [2. Database Schema \& Helper Module (`database.py`)](#2-database-schema--helper-module-databasepy)
    - [3. The REST API Application (`app.py`)](#3-the-rest-api-application-apppy)
    - [4. Testing Endpoints with `curl`](#4-testing-endpoints-with-curl)


