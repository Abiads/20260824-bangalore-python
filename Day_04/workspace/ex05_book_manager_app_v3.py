from pprint import pprint

def menu():
    """
    Display a set of options to the user,
    accept the user's choice,
    do a basic validation
    if correct value, return the same
    else return -1
    """
    print("*** MAIN MENU ***")
    print("=================")
    print("0. Exit")
    print("1. Add a book record")
    print("2. View all books")
    print("3. Edit a book record")
    print("4. Delete a book")

    choice = int(input('Enter your choice: '))

    if choice < 0 or choice > 4:
        choice = -1

    return choice

books = [
    {"id" :819, "title" :"Let us C", "author": "Y Kanitkar", "price": 499.0},
    {'id': 33, 'title': 'Python Unleashed', 'author': 'John MIller', 'price': 999.0},
    {'id': 298, 'title': 'Java made easy', 'author': 'Rajesh Rao', 'price': 1499.0},
]

def add_book():
    b = {}
    print("Enter book details: ")
    b["id"] = int(input("ID: "))
    b['title'] = input("Title: ")
    b['author'] = input("Author: ")
    b['price'] = float(input("Price: "))

    books.append(b)


def view_books():
    print("-"*98)
    print(f"{"ID":^10} {"Title":<35} {"Author":<35} {"Price":>15}")
    print("-"*98)
    for b in books:
        print(f"{b['id']:^10} {b['title']:<35} {b['author']:<35} {b['price']:>15.2f}")
    print("="*98)


def edit_book():
    book_id = int(input("Enter id of the book to edit: "))

    book_ids = [b[0] for b in books] # list of books transformed into a list of ids
    if book_id not in book_ids:
        print("No such book. Try again.")
        return

    the_book = [b for b in books if b[0]==book_id][0]
    _, title, author, price = the_book

    _title = input(f'Title: ({title}) ')
    if _title == "":
        _title = title

    _author = input(f'Author: ({author}) ')
    if _author == "":
        _author = author

    _price = input(f'Price: ({price}) ')
    if _price == "":
        _price = price
    else:
        _price = float(_price)

    the_book[1] = _title
    the_book[2] = _author
    the_book[3] = _price

    print("The book is updated successfully!")


def delete_book():
    book_id = int(input("Enter id of the book to delete: "))

    book_ids = [b[0] for b in books] # list of books transformed into a list of ids
    if book_id not in book_ids:
        print("No such book. Try again.")
        return

    the_book = [b for b in books if b[0]==book_id][0]
    print("Book found!")
    print(f"ID          : {the_book[0]}")
    print(f"Title       : {the_book[1]}")
    print(f"Author      : {the_book[2]}")
    print(f"Price       : {the_book[3]}")

    print()
    ans = input("Are you sure you want to delete this book? (yes/no): ")

    if ans.strip().lower() == "yes":
        books.remove(the_book)
        print("Book deleted successfully!")
    else:
        print("Book was not deleted!")


def main():
    while True:
        user_choice = menu()

        if user_choice == 0:
            break

        if user_choice == 1:
            add_book()
        elif user_choice == 2:
            view_books()
        elif user_choice == 3:
            edit_book()
        elif user_choice == 4:
            delete_book()
        else:
            print("Invalid choice! Please retry with valid value.")

        print()
    print("Bye!")


print("-" * 80)
main()