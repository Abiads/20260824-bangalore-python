"""
Assignment 3: Course Feedback Compiler & Sanitizer

Scenario:
Process feedback records containing ratings from 1 to 5. Clean invalid elements and calculate averages.

Problem Description:
Write `compile_feedback(ratings_dict)`:
- Returns a dict mapping each course name to its average rating, rounded to 2 decimal places.
- For each rating: attempt `float(val)`. If ValueError/TypeError, print warning:
  "Warning: Invalid rating value '<val>' in course '<course>' skipped." and continue.
- If course has 0 valid ratings: catch `ZeroDivisionError`, print warning:
  "Warning: No valid ratings found for course '<course>'. Rating set to 0.0." and assign 0.0.
"""

def compile_feedback(ratings_dict: dict) -> dict:
    averages = {}
    #imp assignment
    for course, ratings in ratings_dict.items():
        total = 0
        count = 0
        for val in ratings:
            try:
                rating = float(val)
                total += rating
                count += 1
            except (ValueError, TypeError):
                print(
                    f"Warning: Invalid rating value '{val}' "
                    f"in course '{course}' skipped."
                )
                continue

        try:
            average = total / count
        except ZeroDivisionError:
            print(
                f"Warning: No valid ratings found for course "
                f"'{course}'. Rating set to 0.0."
            )
            average = 0.0
        averages[course] = round(average, 2)
    return averages


if __name__ == "__main__":
    feedback_data = {
        "Python Programming": [5, 4, "4", "Great", 5],
        "Machine Learning": [],
        "Deep Learning": ["Good", "Average", None]
    }
    # Test your function
    averages = compile_feedback(feedback_data)
    print("Feedback Averages:", averages)

