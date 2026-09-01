"""
Exercise 5: Custom Title Case Formatter

Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters).
- **Sample Input**: `"WELCOME TO BANGALORE CITY"`
- **Sample Output**: `"Welcome To Bangalore City"`

--------------------------------------------------

"""

# def solve():
#     text = input("Enter a string: ")
#     words = text.split()
#     title_case_words = []
    
#     for word in words:
#         if len(word) > 0:
#             # Capitalize first letter and lowercase the rest
#             title_case_word = word[0].upper() + word[1:].lower()
#             title_case_words.append(title_case_word)
    
#     result = ' '.join(title_case_words)
#     print(result)

# if __name__ == "__main__":
#     solve()


def solve():
    text = input("Enter a string:")
    words = text.lower().split()
    number_of_words = len(words)

    # print(type(number_of_words))
    
    for i in range(number_of_words):
        words[i] = words[i].capitalize()

    result = ' '.join(words)
    print(result)


if __name__ == "__main__":
    solve()