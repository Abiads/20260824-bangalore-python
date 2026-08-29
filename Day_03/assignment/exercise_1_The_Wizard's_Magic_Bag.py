"""
Exercise 1: The Wizard's Magic Bag

A wizard has a magic bag containing a sequence of items: ["staff", "potion", "spellbook"]
When the wizard steps through a magic portal:
1. A new item enters the bag (append to the end)
2. The oldest item in the bag (at index 0) is dissolved and ejected (remove from start)

HINTS:
- Use input() to get the new item name
- Use list.pop(0) to remove and get the first item
- Use list.append() to add the new item to the end
- Print the ejected item and updated bag contents
"""

# TODO: Initialize the magic bag
# TODO: Prompt user for new item
# TODO: Remove the first item from the bag
# TODO: Add the new item to the bag
# TODO: Print results

def solve():
    list1=['staff', 'potion', 'spellbook']
    str1=str(input("Enter the String to be inserted in the last(e.g. amulet)\n"))
    list1.pop(0)
    list1.append(str1)
    print(list1)


if __name__ == "__main__":
    solve()

