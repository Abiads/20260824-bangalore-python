# Initial sample data stored in a list of dictionaries
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000.0, "quantity": 10},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 20000.0, "quantity": 25},
    {"id": 3, "name": "Chair", "category": "Furniture", "price": 1500.0, "quantity": 50},
    {"id": 4, "name": "Notebook", "category": "Stationery", "price": 50.0, "quantity": 200},
    {"id": 5, "name": "Bottle", "category": "Accessories", "price": 300.0, "quantity": 80}
]

next_id = 6  # Tracks the next auto-generated product ID

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
            print("Error: Quantity must be greater than or equal to 0.")
        except ValueError:
            print("Error: Invalid integer input. Please enter a whole number.")

#-------------------------------------------------------------------------------------

def display_table(product_list):
    """Helper function to print products in a neat tabular format."""
    print(f"\n{'-'*65}")
    print(f"{'ID':<5} | {'Name':<18} | {'Category':<15} | {'Price (₹)':<10} | {'Qty':<6}")
    print(f"{'-'*65}")
    for p in product_list:
        print(f"{p['id']:<5} | {p['name']:<18} | {p['category']:<15} | {p['price']:<10.2f} | {p['quantity']:<6}")
    print(f"{'-'*65}")

#-------------------------------------------------------------------------------------

def add_product():
    """Adds a new product with auto-generated ID."""
    global next_id
    print("\n--- Add Product ---")
    name = get_non_empty_string("Enter Product Name: ")
    category = get_non_empty_string("Enter Category: ")
    price = get_positive_float("Enter Price: ")
    quantity = get_non_negative_int("Enter Quantity: ")

    new_item = {
        "id": next_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    products.append(new_item)
    print(f"Success: Product '{name}' added with ID: {next_id}")
    next_id += 1

#-------------------------------------------------------------------------------------

def view_all_products():
    """Displays all products in the inventory."""
    print("\n--- Inventory Products ---")
    if not products:
        print("No products currently available in inventory.")
        return
    display_table(products)

#-------------------------------------------------------------------------------------

def search_product():
    """Searches products by Product ID or Name."""
    print("\n--- Search Product ---")
    print("1. Search by ID")
    print("2. Search by Name")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        try:
            search_id = int(input("Enter Product ID to search: "))
            matches = [p for p in products if p["id"] == search_id]
        except ValueError:
            print("Error: ID must be an integer.")
            return
    elif choice == "2":
        search_name = input("Enter Product Name to search: ").strip().lower()
        matches = [p for p in products if search_name in p["name"].lower()]
    else:
        print("Invalid search choice.")
        return

    if matches:
        display_table(matches)
    else:
        print("No matching products found.")

#-------------------------------------------------------------------------------------

def update_product():
    """Updates product attributes using product ID."""
    print("\n--- Update Product ---")
    try:
        prod_id = int(input("Enter Product ID to update: "))
    except ValueError:
        print("Error: Product ID must be an integer.")
        return

    target = next((p for p in products if p["id"] == prod_id), None)
    if not target:
        print(f"Product with ID {prod_id} not found.")
        return

    print(f"Updating Product: {target['name']} (ID: {target['id']})")
    print("(Press Enter directly to keep the existing value)")

    # Name update
    new_name = input(f"Enter new Name [{target['name']}]: ").strip()
    if new_name:
        target["name"] = new_name

    # Category update
    new_cat = input(f"Enter new Category [{target['category']}]: ").strip()
    if new_cat:
        target["category"] = new_cat

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

    # Quantity update
    qty_input = input(f"Enter new Quantity [{target['quantity']}]: ").strip()
    if qty_input:
        while True:
            try:
                val = int(qty_input)
                if val >= 0:
                    target["quantity"] = val
                    break
                print("Quantity must be >= 0.")
            except ValueError:
                print("Invalid integer.")
            qty_input = input("Re-enter valid Quantity: ").strip()

    print(f"Success: Product ID {prod_id} updated successfully.")

#-------------------------------------------------------------------------------------

def delete_product():
    """Deletes a product by product ID."""
    print("\n--- Delete Product ---")
    try:
        prod_id = int(input("Enter Product ID to delete: "))
    except ValueError:
        print("Error: Product ID must be an integer.")
        return

    for i, p in enumerate(products):
        if p["id"] == prod_id:
            deleted_item = products.pop(i)
            print(f"Success: Product '{deleted_item['name']}' (ID: {prod_id}) removed.")
            return

    print(f"Product with ID {prod_id} not found.")

#-------------------------------------------------------------------------------------

def main():
    """Main menu loop."""
    while True:
        print("\n===================================")
        print(" PRODUCT INVENTORY MANAGEMENT")
        print("===================================")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        print("===================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            view_all_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option between 1 and 6.")

#-------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
