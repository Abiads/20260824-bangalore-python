import json

# Initial sample data stored in a list of dictionaries
students = [
    {"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
    {"id": 2, "name": "Diya Patel", "course": "Data Science", "marks": 74.0, "grade": "B"},
    {"id": 3, "name": "Rohan Nair", "course": "Web Architecture", "marks": 45.0, "grade": "F"},
    {"id": 4, "name": "Sneha Kulkarni", "course": "Python Core", "marks": 92.0, "grade": "A"},
    {"id": 5, "name": "Amit Verma", "course": "Data Science", "marks": 63.5, "grade": "C"}
]

next_id = 6  # Tracks the next auto-generated student ID
FILE_NAME = "students.json"

#-------------------------------------------------------------------------------------

def compute_letter_grade(marks):
    """Calculates letter grade based on marks obtained."""
    if marks >= 85.0:
        return "A"
    elif marks >= 70.0:
        return "B"
    elif marks >= 50.0:
        return "C"
    else:
        return "F"

#-------------------------------------------------------------------------------------

def get_non_empty_string(prompt):
    """Prompts until a non-empty string is provided."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input cannot be empty. Please re-enter.")

#-------------------------------------------------------------------------------------

def get_valid_marks(prompt):
    """Prompts until a valid float between 0.0 and 100.0 is entered."""
    while True:
        try:
            value = float(input(prompt))
            if 0.0 <= value <= 100.0:
                return value
            print("Error: Marks must be between 0.0 and 100.0 inclusive.")
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid number.")

#-------------------------------------------------------------------------------------

def display_table(student_list):
    """Helper function to print students in a neat tabular format."""
    print(f"\n{'-'*70}")
    print(f"{'ID':<5} | {'Name':<20} | {'Course':<20} | {'Marks':<10} | {'Grade':<6}")
    print(f"{'-'*70}")
    for s in student_list:
        print(f"{s['id']:<5} | {s['name']:<20} | {s['course']:<20} | {s['marks']:<10.2f} | {s['grade']:<6}")
    print(f"{'-'*70}")

#-------------------------------------------------------------------------------------

def add_student():
    """Adds a new student with auto-generated ID and calculated grade."""
    global next_id
    print("\n--- Add Student ---")
    name = get_non_empty_string("Enter Candidate Name: ")
    course = get_non_empty_string("Enter Course Name: ")
    marks = get_valid_marks("Enter Marks (0-100): ")
    grade = compute_letter_grade(marks)

    new_student = {
        "id": next_id,
        "name": name,
        "course": course,
        "marks": marks,
        "grade": grade
    }
    students.append(new_student)
    print(f"Success: Student '{name}' enrolled with ID: {next_id} (Grade: {grade})")
    next_id += 1

#-------------------------------------------------------------------------------------

def view_all_students():
    """Displays all students in the cohort."""
    print("\n--- Student Cohort Directory ---")
    if not students:
        print("No student records currently available.")
        return
    display_table(students)

#-------------------------------------------------------------------------------------

def search_student():
    """Searches students by ID, Name, or Course."""
    print("\n--- Search Student ---")
    print("1. Search by ID")
    print("2. Search by Name or Course")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        try:
            search_id = int(input("Enter Student ID to search: "))
            matches = [s for s in students if s["id"] == search_id]
        except ValueError:
            print("Error: ID must be an integer.")
            return
    elif choice == "2":
        query = input("Enter Name or Course to search: ").strip().lower()
        matches = [s for s in students if query in s["name"].lower() or query in s["course"].lower()]
    else:
        print("Invalid search choice.")
        return

    if matches:
        display_table(matches)
    else:
        print("No matching students found.")

#-------------------------------------------------------------------------------------

def update_student():
    """Updates student details and recalculates grade if marks change."""
    print("\n--- Update Student Record ---")
    try:
        student_id = int(input("Enter Student ID to update: "))
    except ValueError:
        print("Error: Student ID must be an integer.")
        return

    target = next((s for s in students if s["id"] == student_id), None)
    if not target:
        print(f"Student with ID {student_id} not found.")
        return

    print(f"Updating Student: '{target['name']}' (ID: {target['id']})")
    print("(Press Enter directly to keep the existing value)")

    # Name update
    new_name = input(f"Enter new Name [{target['name']}]: ").strip()
    if new_name:
        target["name"] = new_name

    # Course update
    new_course = input(f"Enter new Course [{target['course']}]: ").strip()
    if new_course:
        target["course"] = new_course

    # Marks update
    marks_input = input(f"Enter new Marks [{target['marks']}]: ").strip()
    if marks_input:
        while True:
            try:
                val = float(marks_input)
                if 0.0 <= val <= 100.0:
                    target["marks"] = val
                    target["grade"] = compute_letter_grade(val)
                    print(f"Grade automatically updated to: '{target['grade']}'")
                    break
                print("Marks must be between 0.0 and 100.0.")
            except ValueError:
                print("Invalid number.")
            marks_input = input("Re-enter valid Marks: ").strip()

    print(f"Success: Student ID {student_id} updated successfully.")

#-------------------------------------------------------------------------------------

def delete_student():
    """Deletes a student record by ID."""
    print("\n--- Delete Student ---")
    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Error: Student ID must be an integer.")
        return

    for i, s in enumerate(students):
        if s["id"] == student_id:
            deleted_item = students.pop(i)
            print(f"Success: Student '{deleted_item['name']}' (ID: {student_id}) removed.")
            return

    print(f"Student with ID {student_id} not found.")

#-------------------------------------------------------------------------------------

def save_to_file():
    """Saves all student records to students.json."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            json.dump(students, f, indent=4)
        print(f"Success: {len(students)} record(s) saved to '{FILE_NAME}'.")
    except Exception as e:
        print(f"Error saving to JSON file: {e}")

#-------------------------------------------------------------------------------------

def load_from_file():
    """Loads student records from students.json."""
    global students, next_id
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            loaded = json.load(f)
            if isinstance(loaded, list) and loaded:
                students = loaded
                next_id = max(s["id"] for s in students) + 1
                print(f"Success: {len(students)} record(s) loaded from '{FILE_NAME}'.")
            else:
                print("JSON file was empty or invalid.")
    except FileNotFoundError:
        print(f"File '{FILE_NAME}' not found.")
    except Exception as e:
        print(f"Error loading from JSON file: {e}")

#-------------------------------------------------------------------------------------

def main():
    """Main menu loop."""
    while True:
        print("\n===================================")
        print("    STUDENT GRADE MANAGEMENT")
        print("===================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save to File (students.json)")
        print("7. Load from File (students.json)")
        print("8. Exit")
        print("===================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
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
