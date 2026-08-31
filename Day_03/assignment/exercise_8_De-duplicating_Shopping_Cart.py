"""
Exercise 8: De-duplicating Shopping Cart

An online shopping cart has duplicate items due to double-clicks.
Remove all duplicates BUT keep the first occurrence of each item in original order.

HINTS:
- cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
- Iterate through each item in cart
- Keep track of items already seen (use a new list)
- Only add item if it hasn't been added before
- Check if item is NOT in cleaned list: if item not in cleaned_cart

Expected output: ['apple', 'banana', 'orange']
"""

# TODO: Initialize cart with duplicates (hardcoded)
# TODO: Create an empty cleaned_cart list
# TODO: Loop through each item in cart
# TODO: Check if item is not already in cleaned_cart
# TODO: If not present, append it
# TODO: Print cleaned cart
def main():

    # shopping_cart = list(map(str, input().split()))

    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
    cleaned_cart=[]
    for i in range(len(cart)):

        if cart[i] not in cleaned_cart:
            cleaned_cart.append(cart)
    print(cleaned_cart)

    




if __name__== "__main__":
    main()