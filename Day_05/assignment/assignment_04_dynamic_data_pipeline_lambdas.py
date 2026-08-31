"""
Assignment 4: Dynamic Data Pipeline with Lambdas & Custom Sorting

Scenario:
Clean, filter, and sort raw product dataset tuples using map(), filter(), and sorted() with lambdas.

Problem Description:
Write `process_dataset(dataset)`:
1. Parsing: Extract product name (str), numeric price (float), rating (float) from raw tuples.
2. Filtering: Use `filter()` with lambda to keep items with price <= 1000.0.
3. Mapping: Use `map()` with lambda to transform to `{"product": name, "price": price, "score": rating}`.
4. Sorting: Sort list of dicts in descending order of score using `sorted()` with lambda key.
Returns sorted list of dicts.
"""

def process_dataset(dataset: list[tuple]) -> list[dict]:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    data_input = [
        ("Laptop", "Price: 1200", "Rating: 4.8"),
        ("Phone", "Price: 800", "Rating: 4.5"),
        ("Mouse", "Price: 25", "Rating: 4.7"),
        ("Charger", "Price: 15", "Rating: 4.2")
    ]
    processed = process_dataset(data_input)
    print("Processed Dataset:", processed)

