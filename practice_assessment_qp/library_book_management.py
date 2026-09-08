# Initial sample data stored in a list of dictionaries
books = [
    {"id": 1, "title": "Python Programming", "author": "John Zelle", "genre": "Technical", "price": 650.0, "copies": 15},
    {"id": 2, "title": "Clean Code", "author": "Robert Martin", "genre": "Technical", "price": 950.0, "copies": 8},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "price": 350.0, "copies": 20},
    {"id": 4, "title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History", "price": 550.0, "copies": 12},
    {"id": 5, "title": "Cosmos", "author": "Carl Sagan", "genre": "Science", "price": 480.0, "copies": 6}
]

next_id = 6  # Tracks the next auto-generated book ID
FILE_NAME = "books.txt"

#-------------------------------------------------------------------------------------

def get_non_empty_string(prompt):
    """Prompts until a non-empty string is provided."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please re-enter.")

#-------------------------------------------------------------------------------------

def get_positive_float(prompt):
    """Prompts until a valid float greater than 0 is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Error: Price must be greater than 0.")
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid price.")

#-------------------------------------------------------------------------------------

def get_non_negative_int(prompt):
    """Prompts until a valid integer >= 0 is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Error: Copies must be greater than or equal to 0.")
        except ValueError:
            print("Error: Invalid integer input. Please enter a whole number.")

#-------------------------------------------------------------------------------------

def display_table(book_list):
    """Helper function to print books in a neat tabular format."""
    print(f"\n{'-'*75}")
    if not book_list:
        print("Library is empty.")
    for b in book_list:
        print(f"{b['id']} | {b['title']} | {b['author']} | {b['genre']} | {b['price']} | {b['copies']}")
    print(f"{'-'*75}")
   

#-------------------------------------------------------------------------------------

def add_book():
    """Adds a new book with auto-generated ID."""
    global next_id
    print("\n--- Add Book ---")
    title = get_non_empty_string("Enter Book Title: ")
    author = get_non_empty_string("Enter Author Name: ")
    genre = get_non_empty_string("Enter Genre: ")
    price = get_positive_float("Enter Price: ")
    copies = get_non_negative_int("Enter Number of Copies: ")

    new_book = {
        "id": next_id,
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
        "copies": copies
    }
    books.append(new_book)
    print(f"Success: Book '{title}' added with ID: {next_id}")
    next_id += 1

#-------------------------------------------------------------------------------------

def view_all_books():
    """Displays all books in the library catalog."""
    print("\n--- Library Books ---")
    if not books:
        print("No books currently available in catalog.")
        return
    display_table(books)

#-------------------------------------------------------------------------------------

def search_book():
    """Searches books by Book ID, Title, or Author."""
    print("\n--- Search Book ---")
    print("1. Search by ID")
    print("2. Search by Title or Author")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        try:
            search_id = int(input("Enter Book ID to search: "))
            matches = [b for b in books if b["id"] == search_id]
        except ValueError:
            print("Error: ID must be an integer.")
            return
    elif choice == "2":
        query = input("Enter Title or Author to search: ").strip().lower()
        matches = [b for b in books if query in b["title"].lower() or query in b["author"].lower()]
    else:
        print("Invalid search choice.")
        return

    if matches:
        display_table(matches)
    else:
        print("No matching books found.")

#-------------------------------------------------------------------------------------

def update_book():
    """Updates book details using Book ID."""
    print("\n--- Update Book ---")
    try:
        book_id = int(input("Enter Book ID to update: "))
    except ValueError:
        print("Error: Book ID must be an integer.")
        return

    target = next((b for b in books if b["id"] == book_id), None)
    if not target:
        print(f"Book with ID {book_id} not found.")
        return

    print(f"Updating Book: '{target['title']}' (ID: {target['id']})")
    print("(Press Enter directly to keep the existing value)")

    # Title update
    new_title = input(f"Enter new Title [{target['title']}]: ").strip()
    if new_title:
        target["title"] = new_title

    # Author update
    new_author = input(f"Enter new Author [{target['author']}]: ").strip()
    if new_author:
        target["author"] = new_author

    # Genre update
    new_genre = input(f"Enter new Genre [{target['genre']}]: ").strip()
    if new_genre:
        target["genre"] = new_genre

    # Price update
    price_input = input(f"Enter new Price [{target['price']}]: ").strip()
    if price_input:
        while True:
            try:
                val = float(price_input)
                if val > 0:
                    target["price"] = val
                    break
                print("Price must be > 0.")
            except ValueError:
                print("Invalid number.")
            price_input = input("Re-enter valid Price: ").strip()

    # Copies update
    copies_input = input(f"Enter new Copies [{target['copies']}]: ").strip()
    if copies_input:
        while True:
            try:
                val = int(copies_input)
                if val >= 0:
                    target["copies"] = val
                    break
                print("Copies must be >= 0.")
            except ValueError:
                print("Invalid integer.")
            copies_input = input("Re-enter valid Copies: ").strip()

    print(f"Success: Book ID {book_id} updated successfully.")

#-------------------------------------------------------------------------------------

def delete_book():
    """Deletes a book by Book ID."""
    print("\n--- Delete Book ---")
    try:
        book_id = int(input("Enter Book ID to delete: "))
    except ValueError:
        print("Error: Book ID must be an integer.")
        return

    for i, b in enumerate(books):
        if b["id"] == book_id:
            deleted_item = books.pop(i)
            print(f"Success: Book '{deleted_item['title']}' (ID: {book_id}) removed.")
            return

    print(f"Book with ID {book_id} not found.")

#-------------------------------------------------------------------------------------

def save_to_file():
    """Saves all books to books.txt as pipe-delimited text."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for b in books:
                line = f"{b['id']}|{b['title']}|{b['author']}|{b['genre']}|{b['price']:.2f}|{b['copies']}\n"
                f.write(line)
        print(f"Success: {len(books)} book(s) saved to '{FILE_NAME}'.")
    except Exception as e:
        print(f"Error saving to file: {e}")

#-------------------------------------------------------------------------------------

def load_from_file():
    """Loads books from books.txt."""
    global books, next_id
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            loaded = []
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) == 6:
                    loaded.append({
                        "id": int(parts[0]),
                        "title": parts[1].strip(),
                        "author": parts[2].strip(),
                        "genre": parts[3].strip(),
                        "price": float(parts[4]),
                        "copies": int(parts[5])
                    })
            if loaded:
                books = loaded
                next_id = max(b["id"] for b in books) + 1
                print(f"Success: {len(books)} book(s) loaded from '{FILE_NAME}'.")
            else:
                print("File was empty. No records loaded.")
    except FileNotFoundError:
        print(f"File '{FILE_NAME}' not found.")
    except Exception as e:
        print(f"Error loading from file: {e}")

#-------------------------------------------------------------------------------------

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

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            view_all_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            load_from_file()
        elif choice == "8":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option between 1 and 8.")

#-------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
