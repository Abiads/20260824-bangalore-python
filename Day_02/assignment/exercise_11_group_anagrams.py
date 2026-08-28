"""
Exercise 11: Group Anagrams

Write a program that starts with a list of strings defined at the top of your script (e.g., `words = ["eat", "tea", "tan", "ate", "nat", "bat"]`) and groups the anagrams (words formed by rearranging letters) together. Print the final grouped list of lists.

- **Hardcoded Input**: `words = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- **Sample Output**: `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`

--------------------------------------------------

💡 Useful Functions & Methods:
1. `sorted(iterable)` -> Sorts characters in a word.
   - Example: `sorted("eat")` -> `['a', 'e', 't']`
2. `''.join(sorted(word))` -> Creates a canonical sorted key for anagrams.
   - Example: `''.join(sorted("tea"))` -> `"aet"`
3. Dictionary grouping / `collections.defaultdict(list)`:
   - Store words under their sorted key: `groups[key].append(word)`
4. `list(groups.values())` -> Extracts list of grouped lists.

📋 Step-by-Step Logic:
1. Initialize an empty dictionary `anagram_groups = {}`.
2. Iterate through each word in `words`:
   a. Compute key `key = "".join(sorted(word))`.
   b. If `key` not in `anagram_groups`, add `anagram_groups[key] = []`.
   c. Append `word` to `anagram_groups[key]`.
3. Convert `anagram_groups.values()` into a list and print.
"""

def solve():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    anagram_groups = {}
    
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_groups:
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word)
    
    result = list(anagram_groups.values())
    print(result)

if __name__ == "__main__":
    solve()
