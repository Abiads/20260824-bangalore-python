# Day 07 Practice Assignments: Standard Libs, Debugging & Databases

## Objective
Import standard system utilities, log diagnostics, and execute table queries in relational database schemas.

---

### Exercise 1: Log File Error Extractor
Write a script that reads a text log file `system.log` line-by-line. If a line contains the keyword `"ERROR"` or `"WARNING"`, write that line to a new file named `errors.txt` using file I/O operations.

---

### Exercise 2: Directory File Lister
Using the `os` or `pathlib` standard library modules, write a Python program that accepts a folder path from the user and lists all file names inside it, along with their file sizes in kilobytes (KB).

---

### Exercise 3: Relational Student Database
Write a program that uses the `sqlite3` module:
1. Creates a database `school.db` and a table `students` (fields: `id` integer primary key, `name` text, `grade` real).
2. Insert 5 student records.
3. Write a query to retrieve and print all students who have a grade score above `85.0`.

---

### Exercise 4: Dictionary JSON Encoder & Decoder
Write a program that takes a Python dictionary representing configuration parameters, saves it as a local `.json` file, reads it back, and verifies the parameters match.

---

### Exercise 5: Datetime Offset Calculator
Write a script that prompts the user for two dates (in format `YYYY-MM-DD`) and calculates the exact number of days between them using the `datetime` module.

---

### Exercise 6: Interactive Terminal Debugging (PDB)
Write a Python script containing a logic bug (e.g., variable increment mismatch). Add `breakpoint()` to trigger the Python Debugger (PDB) step-through console. Document what commands you would run in PDB to track variables.

---

### Exercise 7: Custom INI Configuration Reader
Write a program to read configurations from an `.ini` file using Python's standard `configparser` module, extracting database logins and port configurations.

---

### Exercise 8: SQLite Update and Delete CRUD Queries
Write a Python database console application to interact with your `school.db` database from Exercise 3. Allow users to input a student's ID and update their grade, or delete a student record based on user inputs.
