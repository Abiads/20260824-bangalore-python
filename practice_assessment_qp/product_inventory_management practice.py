products = [
    {"id": 1, "name": "Laptop", "price": 55000, "quantity": 10},
    {"id": 2, "name": "Chair", "price": 1500, "quantity": 50},
    {"id": 3, "name": "Mouse", "price": 100, "quantity": 5},
    {"id": 4, "name": "Headphone", "price": 1500, "quantity": 5}
]
next_id = 5


def get_num(prompt, cast=float):
    while True:
        try:
            val = cast(input(prompt))
            if val > 0:
                return val
        except ValueError:
            print("Error: Please enter a valid positive number.")


def add_product():
    global next_id
    while True:
        name = input("Enter product name: ").strip()
        if not name:
            print("Name cannot be empty.")
            continue
        price = get_num("Enter price: ", float)
        qty = get_num("Enter quantity: ", int)
        products.append({"id": next_id, "name": name, "price": price, "quantity": qty})
        print(f"Product added: {name} (ID: {next_id})")
        next_id += 1

        if input("Add another? (y/n): ").strip().lower() != "y":
            break


def search_product():
    query = input("Enter product name to search: ").strip().lower()
    matches = [p for p in products if query in p["name"].lower()]
    if not matches:
        print("No products found.")
    for p in matches:
        print(f"ID: {p['id']} | {p['name']} | Price: {p['price']} | Quantity: {p['quantity']}")


def update_product():
    query = input("Enter product name to update: ").strip().lower()
    for p in products:
        if p["name"].lower() == query:
            p["price"] = get_num("Enter new price: ", float)
            p["quantity"] = get_num("Enter new quantity: ", int)
            print(f"Updated: {p['name']} | Price: {p['price']} | Quantity: {p['quantity']}")
            return
    print("Product not found.")


def view_products():
    if not products:
        print("Inventory is empty.")
    for p in products:
        print(f"ID: {p['id']} | {p['name']} | Price: {p['price']} | Quantity: {p['quantity']}")


def delete_product():
    query = input("Enter product name to delete: ").strip().lower()
    for p in products:
        if p["name"].lower() == query:
            products.remove(p)
            print(f"Deleted: {p['name']}")
            return
    print("Product not found.")


def main():
    while True:
        print("\n" + "=" * 40)
        print("     PRODUCT INVENTORY MANAGEMENT")
        print("=" * 40)
        print("1. Add Product\n2. Search Product\n3. Update Product\n4. View All Products\n5. Delete Product\n6. Exit")

        ch = input("Enter choice (1-6): ").strip()
        if ch == "1": add_product()
        elif ch == "2": search_product()
        elif ch == "3": update_product()
        elif ch == "4": view_products()
        elif ch == "5": delete_product()
        elif ch == "6":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Choose 1-6.")


if __name__ == "__main__":
    main()