"""
Exercise 3: Email Domain Extractor

Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the `@`) and print it. If the string is not a valid email (does not contain exactly one `@`), print `"Invalid Email"`.

- **Sample Input**: `"vinod@vinod.co"`
- **Sample Output**: `"vinod.co"`
- **Sample Input**: `"vinod.co"`
- **Sample Output**: `"Invalid Email"`

--------------------------------------------------

💡 Useful Functions & Methods:
1. `str.count(sub)` -> Counts how many times substring `sub` appears in the string.
   - Example: `"user@domain.com".count("@")` -> `1`
2. `str.split(sep, maxsplit)` -> Splits the string by delimiter `@`.
   - Example: `"user@domain.com".split("@")` -> `['user', 'domain.com']`
   - Access domain with index `[1]`.
3. Alternative (Slicing): `str.find(sub)` -> Finds the index of `@`, then slice `email[index+1:]`.

📋 Step-by-Step Logic:
1. Check if `email.count("@") == 1`.
2. If true, extract domain using `email.split("@")[1]` and print it.
3. If false, print `"Invalid Email"`.
"""

def solve():
   string1=str(input("Enter the email\n"))
   # string1.count("@")
   
   if '@' in string1:
      string1.split('@')
      # username=string1.rindex()
      username= string1[:1]
      domainname=string1[2:]
      # print("username",username)
      print(domainname)
      

   else:
      print("Invalid Email")
   

if __name__ == "__main__":
    solve()
