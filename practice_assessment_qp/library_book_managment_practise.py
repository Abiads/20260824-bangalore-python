books = [
    {"id": 1, "title": "Python Programming", "author": "John Zelle", "genre": "Technical", "price": 650.0, "copies": 15},
    {"id": 2, "title": "Clean Code", "author": "Robert Martin", "genre": "Technical", "price": 950.0, "copies": 8},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "price": 350.0, "copies": 20},
    {"id": 4, "title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History", "price": 550.0, "copies": 12},
    {"id": 5, "title": "Cosmos", "author": "Carl Sagan", "genre": "Science", "price": 480.0, "copies": 6}
]
next_id=6

def get_num(prompt, cast = float):
    while True:
        try:        
            val = cast(input(prompt))
            if val > 0:
                return val
        except:
            pass
        print("Enter valid number")
        

def get_str(prompt):
    while True:
        try:
            val = input(prompt).strip()
            if val:
                return val
        except:    
            pass
        print("Enter valid string")

def add_book():
    global next_id
    
    while True:
        title = get_str("Enter the name of the Book: ")
        author = get_str("Enter the name of the Author: ")
        genre = get_str("Whast the Genre?: ")
        price = get_num("Price: ", float)
        copies = get_num("Number of copies: ", int)
        book_list={
            "id": next_id,
            "title": title,
            "author": author,
            "genre": genre,
            "price": price,
            "copies": copies

        }
        books.append(book_list)
        print(f"Success: Book '{title}' added with ID: {next_id}")
        next_id+=1
        next=input("Do you want to enter new book y/n")

        try:
            if next == 'y':
                continue
            else:
                break
        except:
            break



def view_all(books):
    if not books:
        return ("The book list is empty")
    for b in books:
        print(f"{b['id']} || {b['title']} || {b['author']} || {b['genre']} || {b['price']} || {b['copies']}")

def search_book():
    pass

def update():
    pass

def delete():
    pass

def save_txt():
    pass

def load_txt():
    pass





def main():
    """Main menu loop."""

    while True:
        print("\n===================================")
        print("    LIBRARY BOOK MANAGEMENT")
        print("===================================")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Save to File (books.txt)")
        print("7. Load from File (books.txt)")
        print("8. Exit")
        print("===================================")


        try:    
            choice = int(input("Enter your choice (1-8): "))

            if choice == 1:
                add_book()
            elif choice == 2:
                view_all(books)
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                pass
            elif choice == 7:
                pass
            elif choice == 8:
                pass
            else:
                print("Enter a valid choice number")
                main()
        except:
            print("Enter a valid choice number")        



if __name__ == "__main__":
    main()
