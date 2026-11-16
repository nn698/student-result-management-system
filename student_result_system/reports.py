from results import calculate_result, SUBJECTS
from datetime import datetime
from pathlib import Path

def generate_report_card(student):
    result = calculate_result(student)

    print("\n" + "=" * 50)
    print("           STUDENT REPORT CARD")
    print("=" * 50)

    print(f"Student ID: {student.student_id}")
    print(f"Full Name: {student.full_name}")
    print(f"Class: {student.student_class}")
    print(f"Gender: {student.gender}")
    print(f"Date of Birth: {student.dob}")

    print("-" * 50)
    print(f"{'SUBJECT':<20}{'SCORE':>10}")
    print("-" * 50)

    for subject in SUBJECTS:
        score = student.scores.get(subject)

        if score is None:
            print(f"{subject:<20}{'Not entered':>10}")
        else:
            print(f"{subject:<20}{score:>10.2f}")

    print("-" * 50)

    if result is None:
        print("Result Status: INCOMPLETE")
    else:
        print(f"Total Score: {result['total']:.2f}/500")
        print(f"Average Score: {result['average']:.2f}%")
        print(f"Final Grade: {result['grade']}")

    print(
        f"Date Recorded: "
        f"{getattr(student, 'result_date', 'Not recorded')}"
    )

    print("=" * 50)



def display_all_results(students):
    print("\n" + "=" * 85)
    print("                    ALL STUDENTS' RESULTS")
    print("=" * 85)

    if not students:
        print("No students registered.")
        return

    print(
        f"{'ID':<12}"
        f"{'NAME':<25}"
        f"{'CLASS':<10}"
        f"{'TOTAL':<12}"
        f"{'AVERAGE':<12}"
        f"{'GRADE':<8}"
    )

    print("-" * 85)

    for student in students.values():
        result = calculate_result(student)

        if result is None:
            total = "-"
            average = "-"
            grade = "Pending"
        else:
            total = f"{result['total']:.2f}"
            average = f"{result['average']:.2f}%"
            grade = result["grade"]

        print(
            f"{student.student_id:<12}"
            f"{student.full_name[:24]:<25}"
            f"{student.student_class:<10}"
            f"{total:<12}"
            f"{average:<12}"
            f"{grade:<8}"
        )



def rank_students(students):
    ranked_students = []

    for student in students.values():
        result = calculate_result(student)

        if result is not None:
            ranked_students.append(
                (student, result)
            )

    ranked_students.sort(
        key=lambda item: item[1]["average"],
        reverse=True
    )

    print("\n----- STUDENT RANKING -----")

    if not ranked_students:
        print("No completed results available.")
        return

    print(
        f"{'POSITION':<12}"
        f"{'NAME':<25}"
        f"{'AVERAGE':<12}"
        f"{'GRADE':<8}"
    )

    print("-" * 60)

    for position, (student, result) in enumerate(
        ranked_students, start=1
    ):
        print(
            f"{position:<12}"
            f"{student.full_name[:24]:<25}"
            f"{result['average']:<12.2f}"
            f"{result['grade']:<8}"
        )



def sort_students_by_name(students):
    sorted_students = sorted(
        students.values(),
        key=lambda student: student.full_name.lower()
    )

    print("\n----- STUDENTS SORTED BY NAME -----")

    if not sorted_students:
        print("No students registered.")
        return

    for student in sorted_students:
        print(
            f"{student.student_id} - "
            f"{student.full_name} - "
            f"{student.student_class}"
        )



def class_statistics(students):
    class_name = input(
        "Enter Class/Form: "
    ).strip().lower()

    class_results = []

    for student in students.values():
        if student.student_class.lower() == class_name:
            result = calculate_result(student)

            if result is not None:
                class_results.append(result["average"])

    if not class_results:
        print("No completed results found for this class.")
        return

    highest = max(class_results)
    lowest = min(class_results)

    class_average = sum(class_results) / len(class_results)

    print("\n----- CLASS STATISTICS -----")
    print(f"Class: {class_name.upper()}")
    print(f"Completed Results: {len(class_results)}")
    print(f"Highest Average: {highest:.2f}%")
    print(f"Lowest Average: {lowest:.2f}%")
    print(f"Class Average: {class_average:.2f}%")



def save_report(students):
    report_folder = Path("reports")
    report_folder.mkdir(exist_ok=True)

    filename = report_folder / "student_results.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("STUDENT RESULT REPORT\n")
        file.write("=" * 60 + "\n")

        file.write(
            f"Generated: {datetime.now():%Y-%m-%d %H:%M:%S}\n\n"
        )

        for student in students.values():
            result = calculate_result(student)

            file.write(f"ID: {student.student_id}\n")
            file.write(f"Name: {student.full_name}\n")
            file.write(f"Class: {student.student_class}\n")

            if result is None:
                file.write("Result: Pending\n")
            else:
                file.write(
                    f"Total: {result['total']:.2f}/500\n"
                )
                file.write(
                    f"Average: {result['average']:.2f}%\n"
                )
                file.write(
                    f"Grade: {result['grade']}\n"
                )

            file.write("-" * 60 + "\n")

    print(f"\nReport saved successfully to {filename}")
