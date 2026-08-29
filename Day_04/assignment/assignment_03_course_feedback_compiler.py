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
    result = {}
    for course, ratings in ratings_dict.items():
        valid_ratings = []
        for val in ratings:
            try:
                if val is None:
                    raise TypeError("None value")
                valid_ratings.append(float(val))
            except (ValueError, TypeError):
                print(f"Warning: Invalid rating value '{val}' in course '{course}' skipped.")
        
        try:
            avg = sum(valid_ratings) / len(valid_ratings)
            result[course] = round(avg, 2)
        except ZeroDivisionError:
            print(f"Warning: No valid ratings found for course '{course}'. Rating set to 0.0.")
            result[course] = 0.0
            
    return result

if __name__ == "__main__":
    feedback_data = {
        "Python Programming": [5, 4, "4", "Great", 5],
        "Machine Learning": [],
        "Deep Learning": ["Good", "Average", None]
    }
    averages = compile_feedback(feedback_data)
    print("Feedback Averages:", averages)

