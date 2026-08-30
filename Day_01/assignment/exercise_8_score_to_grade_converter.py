"""
Exercise 8: Score to Grade Converter

Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:
* 90-100: A
* 80-89: B
* 70-79: C
* 60-69: D
* Below 60: F
"""

def solve():
    num = int(input("Please enter your score: "))
    gpa = {

        10: 'A',
        9: 'A',
        8: 'B',
        7: 'C',
        6: 'D'

    }

    if num > 100:
        print("Invalid score! Score cannot be more than 100.")
        return solve()   #Added a condition to handle errors

    if num >= 60:
        print(gpa.get(num//10))
    else:
        print("F")


if __name__ == "__main__":
    solve()
