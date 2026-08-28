"""
Exercise 10: Run-Length String Compression

Write a program that prompts the user to enter a text string and compresses it using run-length encoding (listing character counts next to each repeated character). If the compressed string is not smaller in size than the original string, print the original string.

- **Sample Input**: `"aabcccccaaa"`
- **Sample Output**: `"a2b1c5a3"`
- **Sample Input**: `"abcd"`
- **Sample Output**: `"abcd"` (since `"a1b1c1d1"` is longer than `"abcd"`)

--------------------------------------------------

💡 Useful Functions & Methods:
1. String iteration with counter:
   - Keep track of `current_char` and `count = 1`.
2. `len(str)` -> Compare length of original vs compressed string.

📋 Step-by-Step Logic:
1. If input string is empty, return `""`.
2. Loop through the string from index `1` to `len(s)`.
3. If `s[i] == s[i-1]`, increment `count += 1`.
4. If `s[i] != s[i-1]`, append `f"{s[i-1]}{count}"` to result list and reset `count = 1`.
5. After the loop, append the final group `f"{s[-1]}{count}"`.
6. Join into `compressed_str`.
7. If `len(compressed_str) < len(s)`, print `compressed_str`; otherwise print original string `s`.
"""

def solve():
    text = input("Enter a text string: ")
    
    if len(text) == 0:
        print(text)
        return
    
    compressed = []
    count = 1
    
    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed.append(f"{text[i - 1]}{count}")
            count = 1
    
    compressed.append(f"{text[-1]}{count}")
    compressed_str = ''.join(compressed)
    
    if len(compressed_str) < len(text):
        print(compressed_str)
    else:
        print(text)

if __name__ == "__main__":
    solve()
