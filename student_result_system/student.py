from datetime import date
import re
class Student:
    def __init__(self, student_id, full_name, student_class, gender, dob):
        self.student_id = student_id
        self.full_name = full_name
        self.student_class = student_class
        self.gender = gender
        self.dob = dob
        self.scores = {}

        self.validate()

    def display_info(self):
        print("\n----- STUDENT INFORMATION -----")
        print(f"Student ID: {self.student_id}")
        print(f"Full Name: {self.full_name}")
        print(f"Class: {self.student_class}")
        print(f"Gender: {self.gender}")
        print(f"Date of Birth: {self.dob}")
        print(f"Scores: {self.scores}")

    
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "student_class": self.student_class,
            "gender": self.gender,
            "dob": self.dob,
            "scores": self.scores,
            "result_date": getattr(
                self, "result_date", None
            )
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(
            data["student_id"],
            data["full_name"],
            data["student_class"],
            data["gender"],
            data["dob"]
        )

        student.scores = data.get("scores", {})
        student.result_date = data.get("result_date")

        return student

    
    def validate(self):
        # Student ID must contain 2-20 permitted characters.
        if not re.fullmatch(
            r"[A-Z0-9_-]{2,20}",
            self.student_id
        ):
            raise ValueError(
                "Student ID must contain 2-20 letters, "
                "numbers, underscores or hyphens."
            )

        if len(self.full_name.strip()) < 2:
            raise ValueError(
                "Full name must contain at least 2 characters."
            )

        if not self.student_class.strip():
            raise ValueError("Student class cannot be empty.")

        if self.gender.lower() not in (
            "male", "female", "other"
        ):
            raise ValueError(
                "Gender must be Male, Female or Other."
            )

        try:
            birth_date = date.fromisoformat(self.dob)
        except ValueError:
            raise ValueError(
                "Date of birth must be a valid date in YYYY-MM-DD format."
            )

        if birth_date > date.today():
            raise ValueError(
                "Date of birth cannot be in the future."
            )


