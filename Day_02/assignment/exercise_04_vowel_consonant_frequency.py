"""
Exercise 4: Vowel & Consonant Frequency

Write a program that prompts the user to enter a string and counts:

1. The individual frequency of each vowel (`a`, `e`, `i`, `o`, `u`), case-insensitively.
2. The total count of all consonants.

- **Sample Input**: `"VinodKumarKayartaya"`
- **Sample Output**:
  ```text key val 
  Vowel Frequencies:
  a: 4
  e: 0
  i: 1
  o: 1
  u: 1
  Total Consonants: 12
  ```

--------------------------------------------------

💡 Useful Functions & Methods:
1. `str.lower()` -> Converts the string to lowercase so counting is case-insensitive.
2. `str.isalpha()` -> Returns `True` if a character is an alphabetical letter (ignores spaces/symbols).
3. Dictionary / `str.count(vowel)` -> Can count occurrences of each vowel.
   - Example: `text.count('a')`
4. Membership operator `in` -> Check if `char in "aeiou"`.

📋 Step-by-Step Logic:
1. Convert input string to lowercase: `text = text.lower()`.
2. For vowels: loop over `'aeiou'` and get frequency using `text.count(v)`.

3. For consonants: loop through each character in `text`. If `char.isalpha()` and `char not in 'aeiou'`, increment consonant counter.
4. Display the formatted vowel frequencies and total consonants count.
"""

def solve():
    text = input("Enter a string: ")
    text_lower = text.lower()
    
    vowels = 'aeiou'
    vowel_freq = {}
    consonant_count = 0
    
    # Count vowel frequencies
    for vowel in vowels:
        vowel_freq[vowel] = text_lower.count(vowel)
    
    # Count consonants
    for char in text_lower:
        if char.isalpha() and char not in vowels:
            consonant_count += 1
    
    print("Vowel Frequencies:")
    for vowel in vowels:
        print(f"{vowel}: {vowel_freq[vowel]}")
    print(f"Total Consonants: {consonant_count}")

        if lower1[i] == 'a':
            acount += 1
        if lower1[i] == 'e':
            ecount += 1
        if lower1[i] == 'i':
            icount += 1
        if lower1[i] == 'o':
            ocount += 1
        if lower1[i] == 'u':
            ucount += 1

    print("a:", acount)
    print("e:", ecount)
    print("i:", icount)
    print("o:", ocount)
    print("u:", ucount)

    vowelcount = acount + ecount + icount + ocount + ucount
    print("TotalConsonant:", n - vowelcount)



if __name__ == "__main__":
    solve()
