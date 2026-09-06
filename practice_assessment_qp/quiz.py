def get_low_stock_products(products_list, threshold):
    return [p for p in products_list if p["quantity"] < threshold]
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000.0, "quantity": 10},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 20000.0, "quantity": 25},
    {"id": 3, "name": "Chair", "category": "Furniture", "price": 1500.0, "quantity": 50},
]
print(get_low_stock_products(products, 28))
    # ...
print("\nAnother Function Starts\n")

def find_expensive_product_in_category(products_list, min_price, category):
    filtered = [p for p in products_list if p["category"] == category and p["price"] > min_price]
    return max(filtered, key=lambda x: x["price"]) if filtered else None
print(find_expensive_product_in_category(products, 1500.0, "Electronics"))

    # ...
def calculate_total_stock_value(products_list):
    return sum(p["price"] * p["quantity"] for p in products_list)
print(calculate_total_stock_value(products))
    # ...
def group_products_by_category(products_list):
    groups = {}
    for p in products_list:
        cat = p["category"]
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(p["name"])
    return groups
print(group_products_by_category(products))
    # ...
def validate_product_data(products_list):
    errors = []
    for p in products_list:
        if p["quantity"] < 0:
            errors.append(p["name"])
    return errors
print(validate_product_data(products))
    # ...
def get_inventory_summary(products_list):
    count = len(products_list)
    total_val = sum(p["price"] * p["quantity"] for p in products_list)
    return f"Total items: {count}, Total Value: {total_val}"
print(get_inventory_summary(products))
