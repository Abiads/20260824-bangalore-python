def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please re-enter.")


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Error: Please enter a valid positive number.")
        except ValueError:
            print("Error: Please enter a valid positive number.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Error: Please enter a valid positive integer.")
        except ValueError:
            print("Error: Please enter a valid positive integer.")


def add_products(products):
    while True:
        product_name = get_non_empty_string("Enter product name: ")
        product_price = get_positive_float("Enter product price: ")
        product_quantity = get_positive_integer("Enter product quantity: ")

        products.append((product_name, product_price, product_quantity))
        print(f"Product added: {product_name}, Price: {product_price}, Quantity: {product_quantity}")

        add_another = input("Do you want to add another product? (y/n): ").strip().lower()
        if add_another != 'y':
            break


def search_products(products):
    search_name = get_non_empty_string("Enter product name to search: ")
    found_products = [product for product in products if product[0].lower() == search_name.lower()]

    if found_products:
        for product in found_products:
            print(f"Found Product: {product[0]}, Price: {product[1]}, Quantity: {product[2]}")
    else:
        print("No products found with that name.")


def update_products(products):
    search_name = get_non_empty_string("Enter product name to update: ")

    for i, product in enumerate(products):
        if product[0].lower() == search_name.lower():
            new_price = get_positive_float("Enter new product price: ")
            new_quantity = get_positive_integer("Enter new product quantity: ")
            products[i] = (product[0], new_price, new_quantity)
            print(f"Product updated: {product[0]}, New Price: {new_price}, New Quantity: {new_quantity}")
            return

    print("No products found with that name.")


def view_all_products(products):
    if not products:
        print("No products in the inventory.")
    else:
        for product in products:
            print(f"Product: {product[0]}, Price: {product[1]}, Quantity: {product[2]}")


def delete_products(products):
    search_name = get_non_empty_string("Enter product name to delete: ")

    for i, product in enumerate(products):
        if product[0].lower() == search_name.lower():
            deleted_product = products.pop(i)
            print(f"Product deleted: {deleted_product[0]}")
            return

    print("No products found with that name.")


def main():
    products = []

    while True:
        print("\n" + "=" * 80)
        print("PRODUCT INVENTORY MANAGEMENT")
        print("=" * 80)
        print("Menu")
        print("1. Add Product")
        print("2. Search Product")
        print("3. Update Product")
        print("4. View All Products")
        print("5. Delete Product")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid selection. Please choose a number between 1 and 6.")
            continue

        if choice == 1:
            add_products(products)
        elif choice == 2:
            search_products(products)
        elif choice == 3:
            update_products(products)
        elif choice == 4:
            view_all_products(products)
        elif choice == 5:
            delete_products(products)
        elif choice == 6:
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose an option between 1 and 6.")


if __name__ == "__main__":
    main()