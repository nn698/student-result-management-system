import json
from pathlib import Path

from student import Student


# Create a path relative to the project folder.
BASE_DIR = Path(__file__).resolve().parent

DATA_FILE = BASE_DIR / "data" / "students.json"


def save_students(students):
    DATA_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    student_records = []

    for student in students.values():
        student_records.append(
            student.to_dict()
        )

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(
            student_records,
            file,
            indent=4
        )

    print("Student records saved successfully!")


def load_students():
    if not DATA_FILE.exists():
        print("No saved student records found.")
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            student_records = json.load(file)

        students = {}

        for record in student_records:
            student = Student.from_dict(record)

            students[student.student_id] = student

        print("Student records loaded successfully!")

        return students

    except (json.JSONDecodeError, OSError, KeyError,
            TypeError, ValueError) as error:
        print(f"Error loading student records: {error}")
        raise
