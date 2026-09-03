"""
STUDENT GRADE & ASSESSMENT MODULE
CONTINUOUS EVALUATION & TRANSCRIPT PERSISTENCE SYSTEM
Coursework: Python Systems Programming | Duration: 2 Hours | Maximum Marks: 40 | Target Topic: JSON File Persistence & Modular Analytics
"""

import json

# Initial sample cohort dataset (for testing and initial seeding)
students = [
    {"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
    {"id": 2, "name": "Diya Patel", "course": "Data Science", "marks": 74.0, "grade": "B"},
    {"id": 3, "name": "Rohan Nair", "course": "Web Architecture", "marks": 45.0, "grade": "F"},
    {"id": 4, "name": "Sneha Kulkarni", "course": "Python Core", "marks": 92.0, "grade": "A"},
    {"id": 5, "name": "Amit Verma", "course": "Data Science", "marks": 63.5, "grade": "C"}
]

next_id = 6  # Tracks next auto-assigned student ID
DEFAULT_JSON_FILEPATH = "students.json"

#-------------------------------------------------------------------------------------

def compute_letter_grade(marks: float) -> str:
    """
    Automated Grade Evaluation Logic:
    - Marks >= 85.0 -> Grade A
    - Marks >= 70.0 and < 85.0 -> Grade B
    - Marks >= 50.0 and < 70.0 -> Grade C
    - Marks < 50.0 -> Grade F (Fail)
    """
    if marks >= 85.0:
        return "A"
    elif marks >= 70.0:
        return "B"
    elif marks >= 50.0:
        return "C"
    else:
        return "F"

#-------------------------------------------------------------------------------------

def get_non_empty_string(prompt: str) -> str:
    """Prompts until a non-empty string is provided after stripping whitespace."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Error: Input string cannot be empty. Please re-enter.")

#-------------------------------------------------------------------------------------

def get_valid_marks(prompt: str) -> float:
    """Prompts until a valid float in the range [0.0, 100.0] is entered."""
    while True:
        try:
            value = float(input(prompt))
            if 0.0 <= value <= 100.0:
                return value
            print("Error: Marks must be between 0.0 and 100.0 inclusive.")
        except ValueError:
            print("Error: Invalid numeric input. Please enter a valid decimal number.")

#-------------------------------------------------------------------------------------

def render_single_student_card(student: dict) -> None:
    """Renders a detailed inspection card for a single student."""
    print("\n" + "=" * 45)
    print("         STUDENT TRANSCRIPT CARD")
    print("=" * 45)
    print(f"  Student ID     : {student['id']}")
    print(f"  Candidate Name : {student['name']}")
    print(f"  Course / Module: {student['course']}")
    print(f"  Marks Obtained : {student['marks']:.2f} / 100.0")
    print(f"  Awarded Grade  : {student['grade']}")
    print("=" * 45)

#-------------------------------------------------------------------------------------

def render_cohort_table(cohort_list: list[dict]) -> None:
    """Displays all student records in a structured tabular grid."""
    if not cohort_list:
        print("\n[!] The student cohort registry is currently empty.")
        return

    if len(cohort_list) == 1:
        render_single_student_card(cohort_list[0])
        return

    print(f"\n{'-'*75}")
    print(f"{'ID':^5} | {'Candidate Name':<22} | {'Course / Module':<22} | {'Marks':>7} | {'Grade':^7}")
    print(f"{'-'*75}")
    for s in cohort_list:
        print(f"{s['id']:^5} | {s['name']:<22} | {s['course']:<22} | {s['marks']:>7.2f} | {s['grade']:^7}")
    print(f"{'-'*75}")

#-------------------------------------------------------------------------------------

def enroll_student(cohort: list[dict], current_next_id: int) -> int:
    """Prompts user for student info, calculates grade, and appends to cohort."""
    print("\n--- Enroll New Student ---")
    name = get_non_empty_string("Enter Candidate Name: ")
    course = get_non_empty_string("Enter Enrolled Course/Module: ")
    marks = get_valid_marks("Enter Marks Obtained (0-100): ")
    grade = compute_letter_grade(marks)

    new_student = {
        "id": current_next_id,
        "name": name,
        "course": course,
        "marks": marks,
        "grade": grade
    }
    cohort.append(new_student)
    print(f"Success: Student '{name}' enrolled with ID: {current_next_id} (Awarded Grade: {grade})")
    return current_next_id + 1

#-------------------------------------------------------------------------------------

def query_student_records(cohort: list[dict], search_term: str) -> list[dict]:
    """Returns students matching exact numeric ID or case-insensitive name/course substring."""
    search_term = search_term.strip()
    if not search_term:
        return []

    # Numeric ID match
    if search_term.isdigit():
        target_id = int(search_term)
        return [s for s in cohort if s["id"] == target_id]

    # Substring search on Name or Course
    query_lower = search_term.lower()
    return [
        s for s in cohort
        if query_lower in s["name"].lower() or query_lower in s["course"].lower()
    ]

#-------------------------------------------------------------------------------------

def revise_student_evaluation(cohort: list[dict], student_id: int) -> bool:
    """Updates candidate name, course, or marks (recalculating grade on marks change)."""
    target = next((s for s in cohort if s["id"] == student_id), None)
    if not target:
        print(f"Error: Student with ID {student_id} not found in cohort.")
        return False

    print(f"\n--- Revise Evaluation for ID {student_id}: '{target['name']}' ---")
    print("(Press Enter directly to keep existing values)")

    # Name update
    name_str = input(f"Enter new Candidate Name [{target['name']}]: ").strip()
    if name_str:
        target["name"] = name_str

    # Course update
    course_str = input(f"Enter new Course [{target['course']}]: ").strip()
    if course_str:
        target["course"] = course_str

    # Marks update
    marks_str = input(f"Enter new Marks [{target['marks']:.2f}]: ").strip()
    if marks_str:
        while True:
            try:
                val = float(marks_str)
                if 0.0 <= val <= 100.0:
                    target["marks"] = val
                    target["grade"] = compute_letter_grade(val)
                    print(f"Grade automatically re-computed to: '{target['grade']}'")
                    break
                print("Marks must be between 0.0 and 100.0.")
            except ValueError:
                print("Invalid numeric value.")
            marks_str = input("Re-enter valid Marks: ").strip()

    print(f"Success: Student ID {student_id} evaluation record updated.")
    return True

#-------------------------------------------------------------------------------------

def purge_student_record(cohort: list[dict], student_id: int) -> bool:
    """Purges student record from cohort after explicit confirmation."""
    for i, s in enumerate(cohort):
        if s["id"] == student_id:
            render_single_student_card(s)
            confirm = input(f"Are you sure you want to purge '{s['name']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                deleted = cohort.pop(i)
                print(f"Success: Student '{deleted['name']}' (ID: {student_id}) purged from memory.")
                return True
            else:
                print("Purge operation cancelled. Record retained.")
                return False

    print(f"Error: Student with ID {student_id} not found in cohort.")
    return False

#-------------------------------------------------------------------------------------

def save_cohort_to_json(filepath: str, cohort: list[dict]) -> None:
    """Serializes cohort list to JSON file with indent=4."""
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(cohort, f, indent=4)
        print(f"Success: {len(cohort)} student record(s) serialized and saved to '{filepath}'.")
    except Exception as e:
        print(f"Error: Failed to write JSON to '{filepath}': {e}")

#-------------------------------------------------------------------------------------

def load_cohort_from_json(filepath: str) -> list[dict]:
    """Deserializes student cohort records from JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            loaded_data = json.load(f)
            if isinstance(loaded_data, list):
                print(f"Success: {len(loaded_data)} student record(s) loaded from '{filepath}'.")
                return loaded_data
            else:
                print("Error: JSON root is not a list. Skipping import.")
                return []
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found. Retaining active in-memory cohort.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Malformed JSON syntax in '{filepath}'. Unable to parse records.")
        return []
    except Exception as e:
        print(f"Error: Unexpected error reading '{filepath}': {e}")
        return []

#-------------------------------------------------------------------------------------

def main():
    """Interactive, menu-driven CLI controller."""
    global students, next_id

    while True:
        print("\n" + "=" * 55)
        print("  STUDENT GRADE & ASSESSMENT MODULE (CLI CONTROLLER)")
        print("=" * 55)
        print("[1] Enroll Student")
        print("[2] Cohort Directory")
        print("[3] Query Records")
        print("[4] Revise Evaluation")
        print("[5] Purge Record")
        print("[6] Save to JSON (students.json)")
        print("[7] Load from JSON (students.json)")
        print("[8] Terminate")
        print("=" * 55)

        choice = input("Enter option [1-8]: ").strip()

        if choice == "1":
            next_id = enroll_student(students, next_id)

        elif choice == "2":
            render_cohort_table(students)

        elif choice == "3":
            query = input("\nEnter Student ID, Candidate Name, or Course Name: ").strip()
            results = query_student_records(students, query)
            if results:
                render_cohort_table(results)
            else:
                print(f"No records found matching '{query}'.")

        elif choice == "4":
            try:
                s_id = int(input("\nEnter Student ID to revise: "))
                revise_student_evaluation(students, s_id)
            except ValueError:
                print("Error: Student ID must be an integer.")

        elif choice == "5":
            try:
                s_id = int(input("\nEnter Student ID to purge: "))
                purge_student_record(students, s_id)
            except ValueError:
                print("Error: Student ID must be an integer.")

        elif choice == "6":
            filepath = input(f"Enter target JSON filepath [{DEFAULT_JSON_FILEPATH}]: ").strip() or DEFAULT_JSON_FILEPATH
            save_cohort_to_json(filepath, students)

        elif choice == "7":
            filepath = input(f"Enter source JSON filepath [{DEFAULT_JSON_FILEPATH}]: ").strip() or DEFAULT_JSON_FILEPATH
            loaded = load_cohort_from_json(filepath)
            if loaded:
                students = loaded
                max_id = max((s["id"] for s in students), default=0)
                next_id = max_id + 1
                print(f"Cohort updated in memory. Next available ID: {next_id}")

        elif choice == "8":
            print("\nTerminating Student Grade Module. Session concluded.")
            break

        else:
            print("Invalid option selected. Please choose a valid command [1-8].")

#-------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
