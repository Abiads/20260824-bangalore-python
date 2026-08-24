# Day 03 Practice Assignments: Working with Lists

## Objective
Implement modifications, traversals, and transformations on lists, including list comprehensions.

---

### Exercise 1: Duplicate Remover
Write a program that accepts a list of elements and returns a new list containing only the unique elements in the original order of occurrence. Do not use Python's built-in `set` conversion.
* **Sample Input**: `[1, 2, 2, 3, 4, 4, 1, 5]`
* **Sample Output**: `[1, 2, 3, 4, 5]`

---

### Exercise 2: Merge and Sort Lists
Write a program that takes two lists of integers, merges them, and sorts the resulting list in ascending order.
* **Sample Input**: `list1 = [5, 1, 9]`, `list2 = [8, 2, 4]`
* **Sample Output**: `[1, 2, 4, 5, 8, 9]`

---

### Exercise 3: Second Largest Element
Write a function that finds the second largest number in a list of integers. Return `None` if the list has fewer than 2 unique elements.
* **Sample Input**: `[12, 35, 1, 10, 34, 1]`
* **Sample Output**: `34`

---

### Exercise 4: List Comprehension Challenge
Write a list comprehension statement that filters a list of numbers from 1 to 100, keeping only those numbers that are divisible by both 3 and 5.
* **Sample Output**: `[15, 30, 45, 60, 75, 90]`

---

### Exercise 5: Multi-dimensional List Index Finder
Write a function `find_element_indices(nested_list, target)` that searches for a target item inside a 2D list (grid of elements) and returns its row and column index as a tuple `(row, col)`. Return `(-1, -1)` if not found.
* **Sample Input**: `grid = [['a', 'b'], ['c', 'd']]`, `target = 'c'`
* **Sample Output**: `(1, 0)`

---

### Exercise 6: Matrix Transpose
Write a program that computes the transpose of a 3x3 matrix represented as a list of lists.
* **Sample Input**: `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
* **Sample Output**: `[[1, 4, 7], [2, 5, 8], [3, 6, 9]]`

---

### Exercise 7: Right Shift List by K
Write a script that accepts a list and an integer $K$, and shifts the list elements to the right by $K$ positions. Elements shifted off the end should wrap around to the beginning.
* **Sample Input**: `lst = [1, 2, 3, 4, 5]`, `K = 2`
* **Sample Output**: `[4, 5, 1, 2, 3]`

---

### Exercise 8: List Intersection without Sets
Write a function that returns the intersection (common elements) of two list structures without converting them to sets. Do not allow duplicate common values in the output.
* **Sample Input**: `l1 = [1, 2, 2, 3]`, `l2 = [2, 2, 4]`
* **Sample Output**: `[2]`
