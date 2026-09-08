"""
### Assignment 1: Structured CSV & JSON Data Processor
#### Scenario
An academic registrar stores student course registrations in a CSV file. You need to read this file, compute overall statistics, and export a summarized JSON report.

#### Problem Description
1. Create a function `process_student_records(input_csv_path, output_json_path)`:
   - Reads an `input_csv_path` containing columns: `student_id`, `name`, `course`, `score`.
   - Uses `csv.DictReader` inside a context manager to parse all rows.
   - Computes:
     - `total_students`: Total number of students processed.
     - `average_score`: Arithmetic mean of all student scores (rounded to 2 decimal places).
     - `top_scorer`: The dictionary `{"name": <name>, "score": <score>}` of the highest scoring student.
     - `course_counts`: A dictionary mapping each course name to the count of enrolled students.
   - Writes the summary dictionary into `output_json_path` formatted with an indentation of 4 spaces using `json.dump()`.

#### Example Walkthrough
```python
# Given input CSV:
# student_id,name,course,score
# 101,Arham,AI,88.5
# 102,Lisa,BDA,94.0
# 103,Vinod,AI,96.5

process_student_records("students.csv", "summary.json")

# Expected summary.json output:
# {
#     "total_students": 3,
#     "average_score": 93.0,
#     "top_scorer": {
#         "name": "Vinod",
#         "score": 96.5
#     },
#     "course_counts": {
#         "AI": 2,
#         "BDA": 1
#     }
# }
```
"""
import csv
import json


def process_student_records(input_csv_path, output_json_path):
    with open(input_csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        summary = {
            "total_students": 0,
            "average_score": 0.0,
            "top_scorer": None,
            "course_counts": {},
        }
    else:
        total_students = len(rows)
        scores = []
        top_scorer = None
        highest_score = float("-inf")
        course_counts = {}

        for row in rows:
            name = row["name"]
            course = row["course"]
            score = float(row["score"])
            scores.append(score)

            if score > highest_score:
                highest_score = score
                top_scorer = {"name": name, "score": score}

            course_counts[course] = course_counts.get(course, 0) + 1

        avg_score = round(sum(scores) / total_students, 2)
        summary = {
            "total_students": total_students,
            "average_score": avg_score,
            "top_scorer": top_scorer,
            "course_counts": course_counts,
        }

    with open(output_json_path, mode="w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    return summary


if __name__ == "__main__":
    pass
