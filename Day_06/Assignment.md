# Day 06 Practice Assignments: Object-Oriented Programming (OOP)

## Objective
Apply inheritance, encapsulation, polymorphism, and decorators to structure class-based designs.

---

### Exercise 1: Library Management System
Create a basic Class-based Library model.
* **Class Book**: Attributes: `title`, `author`, `isbn`, `available` (Boolean). Methods: `borrow_book()` (mark as unavailable if available), `return_book()`.
* **Class Library**: Attributes: `books` (list). Methods: `add_book(book)`, `list_available_books()`.
* Write a test script to add 3 books, borrow 1, and print the list of available titles.

---

### Exercise 2: Area and Perimeter of Shapes
Implement Polymorphism using shapes.
* Create a base class `Shape` with placeholder methods `area()` and `perimeter()`.
* Create child classes `Rectangle` (attributes: `width`, `height`) and `Circle` (attributes: `radius`) that inherit from `Shape`.
* Override `area()` and `perimeter()` in both child classes. Create objects of both shapes, store them in a list, and print their calculated details in a loop.

---

### Exercise 3: Encapsulated Account Class
Create a class `BankAccount`:
* **Private Attribute**: `__balance`.
* **Methods**:
  * `deposit(amount)`: Adds to the balance if amount is positive.
  * `withdraw(amount)`: Deducts if positive and enough funds exist.
  * `@property` decorator to safely get the current balance.

---

### Exercise 4: Object Counter (Class Methods)
Write a class `Student` that keeps track of the total number of student objects instantiated using a class variable and a `@classmethod` getter.
* **Sample Output**: After instantiating 4 students, calling `Student.get_total_count()` returns `4`.

---

### Exercise 5: Multiple Inheritance System
Demonstrate multiple inheritance in Python.
* Class `Bird` with method `fly()`.
* Class `Fish` with method `swim()`.
* Class `FlyingFish` inheriting from both `Bird` and `Fish`. Create an object of `FlyingFish` and demonstrate it can invoke both actions.

---

### Exercise 6: Vector Math (Operator Overloading)
Create a class `Vector2D` representing Cartesian coordinates $(x, y)$. Overload the `+` operator using the special method `__add__` to allow adding two vector objects together directly.
* **Sample Input**: `v1 = Vector2D(2, 3)`, `v2 = Vector2D(5, 1)`
* **Sample Output**: `v1 + v2` returns a new Vector2D object with coordinates `(7, 4)`.

---

### Exercise 7: Object Strings Representation
Add string representations to your `Vector2D` class by implementing both `__str__` and `__repr__` methods, outputting descriptive logs when printing vector objects.

---

### Exercise 8: Custom Fibonacci Iterator
Design a custom iterator class `FibIterator` that outputs Fibonacci numbers in sequence up to a maximum limit supplied during construction.
