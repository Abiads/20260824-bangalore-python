"""
Assignment 2: Robust Phonebook Contact Registry

Scenario:
Command-Line Interface contact registry mapping contact names to phone numbers.
Validates user inputs to prevent corrupted entries.

Problem Description:
1. Define custom exception `InvalidPhoneNumberError(Exception)`.
2. Write function `register_contact(phonebook, name, phone_input)`:
   - Validate `name`: non-empty string consisting only of alphabetic characters and spaces. If invalid, raise `ValueError("Contact name must be a non-empty alphabetic string.")`.
   - Validate `phone_input`: digits only. Attempt `int(phone_input)`. If ValueError occurs, catch it and raise `InvalidPhoneNumberError("Phone number must contain digits only.")`.
   - If valid, store `phone_input` as string in `phonebook[name]`.
   - Return updated `phonebook`.
"""

class InvalidPhoneNumberError(Exception):
    pass

def register_contact(phonebook: dict, name: str, phone_input: str) -> dict:
    if not name or not all(c.isalpha() or c.isspace() for c in name):
        raise ValueError("Contact name must be a non-empty alphabetic string.")
    
    try:
        int(phone_input)
    except ValueError:
        raise InvalidPhoneNumberError("Phone number must contain digits only.")
        
    phonebook[name] = str(phone_input)
    return phonebook

if __name__ == "__main__":
    contacts = {}
    contacts = register_contact(contacts, "Alice", "0987654321")
    print("Registered Alice:", contacts)
    
    try:
        register_contact(contacts, "Bob", "123-456-789")
    except InvalidPhoneNumberError as e:
        print("Caught expected error:", e)
        
    try:
        register_contact(contacts, "Bob123", "9876543210")
    except ValueError as e:
        print("Caught expected error:", e)

