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
  str1=str(input("Enter a string: "))

  lower1=str1.lower()
  n=len(lower1)
  print(n)
  
  
  acount=0
  ecount=0
  icount=0
  ocount=0
  ucount=0
  for i in range (n):
    
    if 'a' in lower1[i]:
      acount+=1
    if 'e' in lower1[i]:
      ecount+=1
    if 'i' in lower1[i]:
      icount+=1
    if 'o' in lower1[i]:
      ocount+=1
    if 'u' in lower1[i]:
      ucount+=1
                           
    

  print("a:",acount)
  print("e:",ecount)
  print("i:",icount)
  print("o",ocount)
  print("u:",ucount)
  vowelcount=  acount+ecount+icount+ocount+ucount
  print("TotalConsonant",n-vowelcount)     


if __name__ == "__main__":
    solve()
