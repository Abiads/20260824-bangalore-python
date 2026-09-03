# 🏆 The Ultimate Master Guide: 3 Practice Assessment Systems

This master document breaks down the **Similarities**, **Differences**, **Core Mechanics**, and a **Rapid Memorization System** for the three Python Practical Assessment applications:

1. 📦 **Product Inventory Management System** (`product_inventory_management.py`)
2. 📚 **Library Book Management System** (`library_book_management.py`)
3. 🎓 **Student Grade & Assessment Module** (`student_grade_management.py`)

---

## 📊 1. Master Comparison Matrix

| Dimension | 📦 Product Inventory System | 📚 Library Book Management | 🎓 Student Grade System |
| :--- | :--- | :--- | :--- |
| **Focus Topic** | In-Memory CRUD & Search Filters | Delimited Flat-File I/O (`open`, `split('|')`) | JSON Persistence (`json.dump` / `json.load`) |
| **Data Schema** | `id, name, category, price, quantity` | `id, title, author, genre, price, copies` | `id, name, course, marks, grade` |
| **Persistence Target** | In-Memory (No File) | `books.txt` (Pipe Delimited: `id\|title\|author...`) | `students.json` (`json.dump(..., indent=4)`) |
| **Special Rule** | Category string tracking & stock validation | Single-Item Card when `count == 1` | Automated Grade Engine (`A`, `B`, `C`, `F`) |
| **Search Method** | Sub-menu: `1. By ID`, `2. By Name` | Unified query (auto-detects `isdigit()` vs substring) | Unified query (ID, Name, or Course substring) |
| **Update Nuance** | Name, Category, Price, Quantity | Price and Copies only | Name, Course, Marks $\to$ **Auto-recalculates Grade** |

---

## 🧩 2. Universal Similarities (The Shared Skeleton)

All 3 systems share the exact same **7 foundational building blocks**. Memorizing these 7 patterns gives you 80% of the code for any assessment.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        THE 7 SHARED BUILDING BLOCKS                    │
│                                                                        │
│ 1. State:          list[dict] + next_id counter                        │
│ 2. Guard Triad:    Safe String, Safe Float, Safe Integer               │
│ 3. Display:        Formatted Grid with f"{val:<width}" and borders     │
│ 4. Search Filter:  List comprehension [x for x in list if condition]   │
│ 5. Update:         Target lookup + Enter-to-skip value preservation    │
│ 6. Delete:         enumerate() + pop(i) with (y/n) confirmation        │
│ 7. Menu Controller:while True + match/if-elif choices + Exit           │
└────────────────────────────────────────────────────────────────────────┘
```

---

### Shared Building Block 1: The Input Guard Triad
Always place these 3 validator functions at the top of your script:

```python
#-------------------------------------------------------------------------------------
# 1. NON-EMPTY STRING GUARD
def get_non_empty_string(prompt: str) -> str:
    while True:
        val = input(prompt).strip()
        if val: return val
        print("Error: Input cannot be empty.")

#-------------------------------------------------------------------------------------
# 2. POSITIVE FLOAT GUARD (Price / Marks)
def get_positive_float(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt))
            if val > 0: return val
            print("Error: Must be greater than 0.")
        except ValueError:
            print("Error: Enter a valid decimal number.")

#-------------------------------------------------------------------------------------
# 3. NON-NEGATIVE INTEGER GUARD (Qty / Copies)
def get_non_negative_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(prompt))
            if val >= 0: return val
            print("Error: Must be >= 0.")
        except ValueError:
            print("Error: Enter a whole integer.")
```

---

### Shared Building Block 2: Table Formatting (<, >, ^)
Align strings left (`<`), numeric amounts right (`>`), and IDs center (`^`):

```python
def render_table(items):
    if not items:
        print("No records available.")
        return
    print(f"\n{'-'*65}")
    print(f"{'ID':^5} | {'Name / Title':<25} | {'Price / Marks':>10} | {'Qty / Grade':^8}")
    print(f"{'-'*65}")
    for item in items:
        print(f"{item['id']:^5} | {item['name']:<25} | {item['price']:>10.2f} | {item['quantity']:^8}")
    print(f"{'-'*65}")
```

---

### Shared Building Block 3: The Unified Search Strategy
One search bar that intelligently handles both numeric IDs and string substrings:

```python
def query_records(dataset, search_term):
    search_term = search_term.strip()
    if not search_term: return []
    
    # Check if user entered numeric ID
    if search_term.isdigit():
        target_id = int(search_term)
        return [item for item in dataset if item["id"] == target_id]
    
    # Otherwise search by name or secondary field (case-insensitive)
    q = search_term.lower()
    return [item for item in dataset if q in item["name"].lower() or q in item["category"].lower()]
```

---

### Shared Building Block 4: The Enter-to-Skip Update Pattern
Prompt the user; if they press **Enter** (empty string), keep the existing value:

```python
def update_item(dataset, item_id):
    target = next((x for x in dataset if x["id"] == item_id), None)
    if not target:
        print(f"ID {item_id} not found.")
        return

    # If user types something, update; if empty, retain old value
    new_name = input(f"Enter Name [{target['name']}]: ").strip()
    if new_name:
        target["name"] = new_name
```

---

### Shared Building Block 5: Safe Deletion with Confirmation
```python
def delete_item(dataset, item_id):
    for i, item in enumerate(dataset):
        if item["id"] == item_id:
            confirm = input(f"Are you sure you want to delete '{item['name']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                deleted = dataset.pop(i)
                print(f"Success: '{deleted['name']}' removed.")
                return
            else:
                print("Cancelled.")
                return
    print("Record not found.")
```

---

## ⚡ 3. Key Differences & Unique Requirements

```
                                SYSTEM DIFFERENCES
                                
   📦 Product Inventory            📚 Library Books             🎓 Student Grades
   ────────────────────           ──────────────────           ──────────────────
   • 100% In-Memory               • Flat Pipe Delimited        • JSON Persistence
   • Sub-menu Search Options      • books.txt serialization    • students.json sync
   • Stock check bounds           • Single item detail card    • Auto-Computed Grade
```

---

### Unique to 📚 Library Book Management: Flat Pipe-Delimited File (`books.txt`)

* **Save to File (`"w"` mode)**:
  ```python
  def sync_catalog_to_file(filepath, catalog):
      with open(filepath, "w", encoding="utf-8") as f:
          for b in catalog:
              f.write(f"{b['id']}|{b['title']}|{b['author']}|{b['genre']}|{b['price']:.2f}|{b['copies']}\n")
  ```

* **Load from File (`"r"` mode with `split('|')`)**:
  ```python
  def load_catalog_from_file(filepath):
      loaded = []
      try:
          with open(filepath, "r", encoding="utf-8") as f:
              for line in f:
                  parts = line.strip().split("|")
                  if len(parts) == 6:
                      loaded.append({
                          "id": int(parts[0]),
                          "title": parts[1],
                          "author": parts[2],
                          "genre": parts[3],
                          "price": float(parts[4]),
                          "copies": int(parts[5])
                      })
          return loaded
      except FileNotFoundError:
          return []
  ```

* **Single-Record Card Inspection**:
  ```python
  if len(book_list) == 1:
      print("\n" + "="*40 + "\n       BOOK DETAILS CARD\n" + "="*40)
      print(f" Title: {book_list[0]['title']}\n Author: {book_list[0]['author']}")
  ```

---

### Unique to 🎓 Student Grade System: Automated Grade Logic & JSON Persistence

* **Automated Grade Evaluation Rule**:
  ```python
  def compute_letter_grade(marks: float) -> str:
      if marks >= 85.0: return "A"
      elif marks >= 70.0: return "B"
      elif marks >= 50.0: return "C"
      else: return "F"
  ```

* **Auto-Recalculate on Update**:
  ```python
  # If marks are updated, immediately recompute letter grade!
  if new_marks_str:
      target["marks"] = float(new_marks_str)
      target["grade"] = compute_letter_grade(target["marks"])
  ```

* **JSON Serialization & Deserialization**:
  ```python
  # Save JSON
  with open("students.json", "w", encoding="utf-8") as f:
      json.dump(students, f, indent=4)

  # Load JSON
  try:
      with open("students.json", "r", encoding="utf-8") as f:
          students = json.load(f)
  except (FileNotFoundError, json.JSONDecodeError):
      pass
  ```

---

## 🧠 4. Rapid Memorization Technique (The 5-Minute Exam Hack)

When you sit for an exam or assessment, follow this **Mental Sequence**:

### Step 1: Write the Skeleton (3 mins)
1. Initialize your list: `items = [...]` and `next_id = len(items) + 1`.
2. Write `main()` with `while True:` and the menu choices `1-8`.
3. Put `pass` in all function headers so the program runs immediately.

### Step 2: Write the 3 Input Guards (2 mins)
1. `get_non_empty_string(prompt)`
2. `get_positive_float(prompt)`
3. `get_non_negative_int(prompt)`

### Step 3: Fill in CRUD (5 mins)
* **Add**: Call the guards $\to$ build dictionary $\to$ `.append()` $\to$ `next_id += 1`.
* **View**: Print table header $\to$ iterate and format $\to$ print border.
* **Search**: `[x for x in items if ...]` using `.isdigit()` or `.lower() in ...`.
* **Update**: Find with `next(...)` $\to$ prompt with `[current_val]` $\to$ if input is non-empty, update.
* **Delete**: Find with `enumerate()` $\to$ prompt `(y/n)` $\to$ `.pop(i)`.

### Step 4: Add the Question-Specific Feature (3 mins)
* If **Products**: Add stock checks.
* If **Library Books**: Add file `split('|')` load and `write()` loop.
* If **Student Grades**: Add `compute_letter_grade()` and `json.dump()` / `json.load()`.

---

## 📁 Source Files Reference

All three fully functioning, tested implementations are located in:
* [`practice_assessment_qp/product_inventory_management.py`](file:///c:/Users/conne/Downloads/CDAC_Python_Vinodco/practice_assessment_qp/product_inventory_management.py)
* [`practice_assessment_qp/library_book_management.py`](file:///c:/Users/conne/Downloads/CDAC_Python_Vinodco/practice_assessment_qp/library_book_management.py)
* [`practice_assessment_qp/student_grade_management.py`](file:///c:/Users/conne/Downloads/CDAC_Python_Vinodco/practice_assessment_qp/student_grade_management.py)
