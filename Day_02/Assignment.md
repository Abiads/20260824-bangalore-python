# Day 02 Practice Assignments: Strings & Tuples

## Objective
Work with string manipulation methods, sequence slicing, formatting, and immutable tuples.

---

### Exercise 1: Palindrome Checker
Write a function that checks whether a given string is a palindrome (reads the same forward and backward, ignoring spaces and letter case).
* **Sample Input**: `"A man a plan a canal Panama"`
* **Sample Output**: `True`

---

### Exercise 2: Character Frequency Counter
Write a Python program to count the number of occurrences of each character in a given string. Store the output in a clean, readable format.
* **Sample Input**: `"hello"`
* **Sample Output**:
  ```text
  h: 1
  e: 1
  l: 2
  o: 1
  ```

---

### Exercise 3: Tuple Operations
Given a tuple of numbers: `numbers = (10, 20, 30, 40, 50, 60, 70, 80)`
1. Print the element at index 3.
2. Print the last element of the tuple.
3. Slice the tuple to get elements from index 2 to 5 (inclusive).
4. Check if the value `30` exists in the tuple.

---

### Exercise 4: Reverse a String using Slicing
Write a function that accepts a string input from the user and returns the reversed string using sequence slicing.
* **Sample Input**: `"CDAC Pune"`
* **Sample Output**: `"enuP CADC"`

---

### Exercise 5: Vowel and Consonant Counter
Write a program that accepts a string and counts the total number of vowels and consonants inside it.
* **Sample Input**: `"Python programming"`
* **Sample Output**: `Vowels: 4, Consonants: 13`

---

### Exercise 6: Substring Finder without Built-ins
Write a function to check if a target substring exists inside a primary string *without* using built-in string methods like `.find()`, `.index()`, or the `in` operator.
* **Sample Input**: `primary="Python"`, `target="th"`
* **Sample Output**: `True`

---

### Exercise 7: Star Padding Layout formatter
Write a program that center-aligns a user-supplied text string inside a fixed block of 30 asterisks (`*`).
* **Sample Input**: `"Python"`
* **Sample Output**: `"************Python************"`

---

### Exercise 8: List of Tuples Conversions
Given a list of tuples containing student names and ages: `data = [("John", 25), ("Alice", 22), ("Bob", 24)]`
Convert this list into a list of formatted strings: `["John is 25 years old", "Alice is 22 years old", ...]`
