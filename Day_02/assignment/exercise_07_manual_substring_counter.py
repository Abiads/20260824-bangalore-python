"""
Exercise 7: Manual Substring Counter

Write a program that prompts the user to enter a main text string and a substring. Count how many times the substring appears in the main string **without using Python's built-in `.count()` method**.

- **Sample Input**: (User inputs main string `"banana"` and substring `"an"`)
- **Sample Output**: `2`

--------------------------------------------------

💡 Useful Functions & Methods (Note: Do NOT use `.count()`):
1. `len(str)` -> Get lengths `len(main_str)` and `len(sub_str)`.
2. Slicing with sliding window:
   - Slice a window of size `len(sub)`: `main_str[i : i + len(sub)]`
   - Loop index `i` in range: `range(len(main_str) - len(sub_str) + 1)`
3. Alternative: `str.find(sub, start_index)` in a `while` loop, advancing start index.

📋 Step-by-Step Logic:
1. Initialize counter `count = 0`.
2. If `len(sub) > len(main)` or `len(sub) == 0`, return 0.
3. Iterate `i` from `0` to `len(main) - len(sub)`.
4. If `main[i : i + len(sub)] == sub`, increment `count += 1`.
5. Print `count`.
"""

def solve():
    # TODO: Implement your solution following the hints above
    pass

if __name__ == "__main__":
    solve()
