import unittest
import sys
from pathlib import Path


sys.path.insert(
    0, str(Path(__file__).resolve().parents[1])
)

from student import Student
from results import (
    calculate_grade,
    calculate_result,
    validate_score,
    SUBJECTS
)


class TestStudentResultSystem(unittest.TestCase):

    def setUp(self):
        self.student = Student(
            "ST001",
            "Yusuf Abubakar",
            "SS3",
            "Male",
            "2005-06-15"
        )

    def test_student_creation(self):
        self.assertEqual(
            self.student.student_id, "ST001"
        )

        self.assertEqual(
            self.student.full_name, "Yusuf Abubakar"
        )

    def test_invalid_student_id(self):
        with self.assertRaises(ValueError):
            Student(
                "ST@001",
                "Ada Obi",
                "SS2",
                "Female",
                "2008-05-12"
            )

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            Student(
                "ST002",
                "Ada Obi",
                "SS2",
                "Female",
                "2026-02-30"
            )

    def test_grade_calculation(self):
        self.assertEqual(calculate_grade(85), "A")
        self.assertEqual(calculate_grade(65), "B")
        self.assertEqual(calculate_grade(55), "C")
        self.assertEqual(calculate_grade(45), "D")
        self.assertEqual(calculate_grade(35), "F")

    def test_score_validation(self):
        self.assertEqual(validate_score(85), 85.0)

        with self.assertRaises(ValueError):
            validate_score(120)

        with self.assertRaises(ValueError):
            validate_score("abc")

    def test_result_calculation(self):
        self.student.scores = {
            "Mathematics": 85,
            "English": 75,
            "Physics": 90,
            "Chemistry": 80,
            "Biology": 70
        }

        result = calculate_result(self.student)

        self.assertEqual(result["total"], 400)
        self.assertEqual(result["average"], 80)
        self.assertEqual(result["grade"], "A")

    def test_incomplete_result(self):
        self.student.scores = {
            "Mathematics": 85
        }

        result = calculate_result(self.student)

        self.assertIsNone(result)

    def test_student_serialization(self):
        student_data = self.student.to_dict()

        restored_student = Student.from_dict(
            student_data
        )

        self.assertEqual(
            restored_student.full_name,
            self.student.full_name
        )


if __name__ == "__main__":
    unittest.main()
