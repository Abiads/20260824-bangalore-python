products = [ 
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10}, 
    {"id": 3, "name": "Smartphone", "category": "Electronics", "price": 20000, "quantity": 25} ,
    {"id": 4, "name": "Smartphone", "category": "Electronics", "price": 17800, "quantity": 12} ,
    {"id": 5, "name": "Smartphone", "category": "Electronics", "price": 31000, "quantity": 3} ,
    {"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50} ,
    {"id": 6, "name": "Smartphone", "category": "Electronics", "price": 200000, "quantity": 2} ,
] 

id_counter = len(products)

#-------------------------------------------------------------------------------------

def menu():
    menu_text = '''1. Add Product 
2. View All Products 
3. Search Product 
4. Update Product 
5. Delete Product 
6. Exit '''

    print('**** Product Inventory Management System ****')
    print(menu_text)
    try:
        choice = int(input('Enter your choice: '))
    except:
        choice = -1

    return choice

#-------------------------------------------------------------------------------------


def add_product():
    global id_counter
    try:
        print('**** Add new product details ****')
        name = input('Name: ').strip()
        if name == '':
            print('Name cannot be empty!')
            return
        
        category = input('Category: ').strip()
        if category == '':
            print('Category cannot be empty!')
            return
        
        price = float(input('Price: '))
        if price <= 0:
            print('Price must be > 0')
            return

        quantity = int(input('Quantity: '))
        if quantity < 0:
            print('Quantity must be >= 0')
            return

        products.append(dict(id=id_counter+1, name=name, category=category, price=price, quantity=quantity))
        id_counter += 1

    except ValueError:
        print('Please retry with a numerical value')

#-------------------------------------------------------------------------------------

def print_one_product(p):
    pid, name, category, price, quantity = p.values()
    print('---- Product Details ----')
    print(f'ID          : {pid}')
    print(f'Name        : {name}')
    print(f'Category    : {category}')
    print(f'Price       : {price}')
    print(f'Quantity    : {quantity}')
    print('-'*50)    

#-------------------------------------------------------------------------------------

def print_many_products(product_list):
    print('-'*60)
    print(f'{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}')
    print('-'*60)
    for p in product_list:
        pid, name, category, price, quantity = p.values()
        print(f'{pid:^5}{name:<20}{category:<20}{price:>10.2f}{quantity:>5}')
    print('-'*60)

#-------------------------------------------------------------------------------------

def view_products():
    if len(products) == 0:
        print("No products in the inventory. Please add first.")
    elif len(products) == 1:
        print_one_product(products[0])
    else:
        print_many_products(products)

#-------------------------------------------------------------------------------------

def search_product():
    try:
        print('1. Search by id')
        print('2. Search by name')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            pid = int(input('Enter the id of the product to search: '))
            search_product_by_id(pid)
        elif choice == 2:
            search_product_by_name()
        else:
            print('Invalid choice. Please try again.')
    except:
        print('Please try again with an integer input.')

#-------------------------------------------------------------------------------------
def search_product_by_id(pid):
    result = [p for p in products if p['id']==pid]
    if not result:
        print(f'No product found for id {pid}')
        return None

    print_one_product(result[0])
    return result[0]
#-------------------------------------------------------------------------------------
def search_product_by_name():
    name = input('Enter the name of the product to search: ')
    result = [p for p in products if p['name']==name]
    if not result:
        print(f'No product found for name "{name}"')
        return

    if len(result) == 1:
        print_one_product(result[0])
    else:
        print_many_products(result)
#-------------------------------------------------------------------------------------
def delete_product():
    try:
        pid = int(input('Enter id of the product to delete: '))
        p = search_product_by_id(pid)
        if p is None:
            return

        ans = input('Are you sure to delete this product? (y/n): ').lower()

        if ans == 'y':
            products.remove(p)
            print('Product deleted successfully!')
        
    except:
        print('Invalid type of value for product id. Try again with an integer.')
#-------------------------------------------------------------------------------------
def main():
    while True:
        choice = menu()

        match choice:
            case 1:
                add_product()
            case 2:
                view_products()
            case 3:
                search_product()
            case 4:
                ...
            case 5:
                delete_product()
            case 6:
                break
            case _:
                print('Invalid choice. Please retry.')


if __name__ == '__main__':
    main()
