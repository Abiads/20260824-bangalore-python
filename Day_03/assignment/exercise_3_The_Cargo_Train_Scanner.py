"""
Exercise 3: The Cargo Train Scanner

A train has wagons: ["coal", "iron", "gold", "coal", "timber", "coal"]
- Prompt user to enter a resource type
- Print the total number of wagons carrying that resource using .count()
- Print the index of the first wagon carrying it using .index()
- If not found, print "Resource not found on train!"

HINTS:
- Use 'if resource in train' to check existence
- Use list.count(resource) to count occurrences
- Use list.index(resource) to find first position
- Handle the case when resource is not found
"""

# TODO: Initialize the train with resources
# TODO: Get resource name from user
# TODO: Check if resource exists in train
# TODO: If exists, count occurrences and find first index
# TODO: If not exists, print not found message
def main():
    train = ["coal", "iron", "gold", "coal", "timber", "coal"]
    resource = input("Enter the resource to scan: ").strip().lower()

    if resource in train:
        count = train.count(resource)
        index = train.index(resource)
        print(f"Resource '{resource}' found {count} time(s) on the train.")
        print(f"First index: {index}")
    else:
        print("Resource not found on train!")

if __name__ == "__main__":
    main()