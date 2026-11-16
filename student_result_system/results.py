from datetime import datetime
import math

SUBJECTS = [
    "Mathematics",
    "English",
    "Physics",
    "Chemistry",
    "Biology"
]


def calculate_grade(average):
    if average >= 70:
        return "A"

    elif average >= 60:
        return "B"

    elif average >= 50:
        return "C"

    elif average >= 40:
        return "D"

    else:
        return "F"



def validate_score(score):
    try:
        score = float(score)
    except (ValueError, TypeError):
        raise ValueError("Score must be a valid number.")

    if not math.isfinite(score) or not 0 <= score <= 100:
        raise ValueError(
            "Score must be between 0 and 100."
        )

    return score



def calculate_result(student):
    scores = student.scores

    
    if not all(subject in scores for subject in SUBJECTS):
        return None

    total = sum(scores[subject] for subject in SUBJECTS)

    average = total / len(SUBJECTS)

    grade = calculate_grade(average)

    return {
        "total": total,
        "average": average,
        "grade": grade
    }



def record_scores(student):
    print(f"\nRecording scores for {student.full_name}")

    # Work on a temporary copy first.
    new_scores = student.scores.copy()

    for subject in SUBJECTS:
        while True:
            existing = new_scores.get(subject)

            if existing is None:
                prompt = f"Enter {subject} score: "
            else:
                prompt = (
                    f"Enter {subject} score "
                    f"[current: {existing}]: "
                )

            value = input(prompt).strip()

            
            if value == "" and existing is not None:
                break

            try:
                score = validate_score(value)
                new_scores[subject] = score
                break

            except ValueError as error:
                print(f"Error: {error}")

    
    student.scores = new_scores

    student.result_date = datetime.now().isoformat(
        timespec="seconds"
    )

    print("\nStudent scores recorded successfully!")
