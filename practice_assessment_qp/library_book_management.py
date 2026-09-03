"""
DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM
Coursework: Python Systems Programming | Duration: 2 Hours | Marks: 40 | Focus: Text File Handling
"""

# Initial sample seed records stored in a list of dictionaries
catalog = [
    {"id": 1, "title": "Python Programming", "author": "John Zelle", "genre": "Technical", "price": 650.00, "copies": 15},
    {"id": 2, "title": "Clean Code", "author": "Robert Martin", "genre": "Technical", "price": 950.00, "copies": 8},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "price": 350.00, "copies": 20},
    {"id": 4, "title": "Sapiens", "author": "Yuval Noah Harari", "genre": "History", "price": 550.00, "copies": 12},
    {"id": 5, "title": "Cosmos", "author": "Carl Sagan", "genre": "Science", "price": 480.00, "copies": 6}
]

next_id = 6  # Tracks next auto-assigned book ID
DEFAULT_FILEPATH = "books.txt"

#-------------------------------------------------------------------------------------

def get_non_empty_string(prompt: str) -> str:
    """Prompts until a non-empty string is provided."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please re-enter.")

#-------------------------------------------------------------------------------------

def get_positive_float(prompt: str) -> float:
    """Prompts until a valid float greater than 0 is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Error: Price must be greater than 0.0.")
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid price.")

#-------------------------------------------------------------------------------------

def get_non_negative_int(prompt: str) -> int:
    """Prompts until a valid integer >= 0 is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Error: Copies must be an integer >= 0.")
        except ValueError:
            print("Error: Invalid integer input. Please enter a whole number.")

#-------------------------------------------------------------------------------------

def render_single_book_card(book: dict) -> None:
    """Renders a detailed key-value inspection card for a single book."""
    print("\n" + "=" * 45)
    print("           BOOK DETAILS CARD")
    print("=" * 45)
    print(f"  Accession ID : {book['id']}")
    print(f"  Book Title   : {book['title']}")
    print(f"  Author Name  : {book['author']}")
    print(f"  Genre        : {book['genre']}")
    print(f"  Unit Price   : ₹{book['price']:.2f}")
    print(f"  Stock Copies : {book['copies']}")
    print("=" * 45)

#-------------------------------------------------------------------------------------

def render_catalog(book_list: list[dict]) -> None:
    """Displays formatted tabular catalog or single-record card when count == 1."""
    if not book_list:
        print("\n[!] The library catalog is currently empty.")
        return

    if len(book_list) == 1:
        render_single_book_card(book_list[0])
        return

    print(f"\n{'-'*80}")
    print(f"{'ID':^5} | {'Book Title':<26} | {'Author Name':<22} | {'Genre':<10} | {'Price (₹)':>9} | {'Copies':>6}")
    print(f"{'-'*80}")
    for b in book_list:
        print(f"{b['id']:^5} | {b['title']:<26} | {b['author']:<22} | {b['genre']:<10} | {b['price']:>9.2f} | {b['copies']:>6}")
    print(f"{'-'*80}")

#-------------------------------------------------------------------------------------

def add_book_entry(book_catalog: list[dict], current_next_id: int) -> int:
    """Prompts user for book details, appends new dict, returns updated ID counter."""
    print("\n--- Add New Book Entry ---")
    title = get_non_empty_string("Enter Book Title: ")
    author = get_non_empty_string("Enter Author Name: ")
    genre = get_non_empty_string("Enter Genre Category: ")
    price = get_positive_float("Enter Unit Price (₹): ")
    copies = get_non_negative_int("Enter Stock Copies: ")

    new_book = {
        "id": current_next_id,
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
        "copies": copies
    }
    book_catalog.append(new_book)
    print(f"Success: '{title}' added to catalog with Accession ID: {current_next_id}")
    return current_next_id + 1

#-------------------------------------------------------------------------------------

def query_books(book_catalog: list[dict], search_term: str) -> list[dict]:
    """Returns filtered list matching numeric ID or case-insensitive title/author substring."""
    search_term = search_term.strip()
    if not search_term:
        return []

    # Check if search term is numeric ID
    if search_term.isdigit():
        target_id = int(search_term)
        return [b for b in book_catalog if b["id"] == target_id]

    # Search by Title or Author substring (case-insensitive)
    query_lower = search_term.lower()
    return [
        b for b in book_catalog
        if query_lower in b["title"].lower() or query_lower in b["author"].lower()
    ]

#-------------------------------------------------------------------------------------

def modify_book_details(book_catalog: list[dict], book_id: int) -> bool:
    """Updates price and copies for the specified book ID; returns success status."""
    target = next((b for b in book_catalog if b["id"] == book_id), None)
    if not target:
        print(f"Error: Book with ID {book_id} not found in catalog.")
        return False

    print(f"\n--- Modifying Book: '{target['title']}' (ID: {book_id}) ---")
    print("(Press Enter directly to keep the existing value)")

    # Update Price
    price_str = input(f"Enter new Price [{target['price']:.2f}]: ").strip()
    if price_str:
        while True:
            try:
                val = float(price_str)
                if val > 0:
                    target["price"] = val
                    break
                print("Price must be > 0.0.")
            except ValueError:
                print("Invalid numeric value.")
            price_str = input("Re-enter valid Price: ").strip()

    # Update Copies
    copies_str = input(f"Enter new Stock Copies [{target['copies']}]: ").strip()
    if copies_str:
        while True:
            try:
                val = int(copies_str)
                if val >= 0:
                    target["copies"] = val
                    break
                print("Copies must be an integer >= 0.")
            except ValueError:
                print("Invalid integer value.")
            copies_str = input("Re-enter valid Stock Copies: ").strip()

    print(f"Success: Book ID {book_id} details updated.")
    return True

#-------------------------------------------------------------------------------------

def delete_book_entry(book_catalog: list[dict], book_id: int) -> bool:
    """Prompts for confirmation before removing the record dictionary; returns success status."""
    for i, b in enumerate(book_catalog):
        if b["id"] == book_id:
            render_single_book_card(b)
            confirm = input(f"Are you sure you want to delete '{b['title']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                deleted = book_catalog.pop(i)
                print(f"Success: Book '{deleted['title']}' (ID: {book_id}) removed from catalog.")
                return True
            else:
                print("Operation cancelled. Record retained.")
                return False

    print(f"Error: Book with ID {book_id} not found in catalog.")
    return False

#-------------------------------------------------------------------------------------

def sync_catalog_to_file(filepath: str, book_catalog: list[dict]) -> None:
    """Serializes each book dictionary into pipe-delimited strings in write mode ('w')."""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            for b in book_catalog:
                line = f"{b['id']}|{b['title']}|{b['author']}|{b['genre']}|{b['price']:.2f}|{b['copies']}\n"
                file.write(line)
        print(f"Success: {len(book_catalog)} book record(s) saved to '{filepath}'.")
    except Exception as e:
        print(f"Error: Failed to save catalog to '{filepath}': {e}")

#-------------------------------------------------------------------------------------

def load_catalog_from_file(filepath: str) -> list[dict]:
    """Parses books.txt line-by-line using split('|') and reconstructs dictionary list."""
    loaded_books = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line_no, line in enumerate(file, 1):
                clean_line = line.strip()
                if not clean_line:
                    continue
                parts = clean_line.split("|")
                if len(parts) != 6:
                    print(f"Warning: Skipping malformed line {line_no}: '{clean_line}'")
                    continue
                
                try:
                    book_id = int(parts[0])
                    title = parts[1].strip()
                    author = parts[2].strip()
                    genre = parts[3].strip()
                    price = float(parts[4])
                    copies = int(parts[5])
                    
                    loaded_books.append({
                        "id": book_id,
                        "title": title,
                        "author": author,
                        "genre": genre,
                        "price": price,
                        "copies": copies
                    })
                except ValueError as ve:
                    print(f"Warning: Skipping line {line_no} due to numeric casting error: {ve}")
                    continue

        print(f"Success: {len(loaded_books)} book record(s) loaded from '{filepath}'.")
        return loaded_books
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found. Initializing with existing in-memory catalog.")
        return []
    except Exception as e:
        print(f"Error: Failed to read from '{filepath}': {e}")
        return []

#-------------------------------------------------------------------------------------

def main():
    """Interactive CLI menu controller."""
    global catalog, next_id

    while True:
        print("\n" + "=" * 50)
        print("  DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM")
        print("=" * 50)
        print("1. Add Book")
        print("2. View Catalog")
        print("3. Search Books")
        print("4. Update Details")
        print("5. Delete Book")
        print("6. Save to File (books.txt)")
        print("7. Load from File (books.txt)")
        print("8. Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            next_id = add_book_entry(catalog, next_id)

        elif choice == "2":
            render_catalog(catalog)

        elif choice == "3":
            query = input("\nEnter search term (Book ID, Title, or Author): ").strip()
            results = query_books(catalog, query)
            if results:
                render_catalog(results)
            else:
                print(f"No records found matching '{query}'.")

        elif choice == "4":
            try:
                b_id = int(input("\nEnter Book ID to update: "))
                modify_book_details(catalog, b_id)
            except ValueError:
                print("Error: Book ID must be an integer.")

        elif choice == "5":
            try:
                b_id = int(input("\nEnter Book ID to delete: "))
                delete_book_entry(catalog, b_id)
            except ValueError:
                print("Error: Book ID must be an integer.")

        elif choice == "6":
            filepath = input(f"Enter destination filepath [{DEFAULT_FILEPATH}]: ").strip() or DEFAULT_FILEPATH
            sync_catalog_to_file(filepath, catalog)

        elif choice == "7":
            filepath = input(f"Enter source filepath [{DEFAULT_FILEPATH}]: ").strip() or DEFAULT_FILEPATH
            loaded = load_catalog_from_file(filepath)
            if loaded:
                catalog = loaded
                max_id = max((b["id"] for b in catalog), default=0)
                next_id = max_id + 1
                print(f"Catalog updated in memory. Next available ID: {next_id}")

        elif choice == "8":
            print("\nExiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please choose a valid numbered option (1-8).")

#-------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
