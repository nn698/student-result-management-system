from student import Student
from results import record_scores, calculate_result
from reports import (
    generate_report_card,
    display_all_results,
    rank_students,
    sort_students_by_name,
    class_statistics,
    save_report
)
from storage import save_students, load_students


try:
    students = load_students()

except (OSError, ValueError, TypeError, KeyError) as error:
    print(f"Unable to start application: {error}")
    raise SystemExit(1)


def register_student():
    print("\n----- REGISTER NEW STUDENT -----")

    student_id = input("Enter Student ID: ").strip().upper()

    
    if student_id in students:
        print("Error: Student ID already exists!")
        return

    full_name = input("Enter Full Name: ").strip()
    student_class = input("Enter Class/Form: ").strip()
    gender = input("Enter Gender: ").strip()
    dob = input("Enter Date of Birth (YYYY-MM-DD): ").strip()

      
    
    try:
        new_student = Student(
            student_id,
            full_name,
            student_class,
            gender,
            dob
        )

    except ValueError as error:
        print(f"Registration failed: {error}")
        return

    students[student_id] = new_student
    save_students(students)

    print("\nStudent registered successfully!")



def view_students():
    print("\n----- REGISTERED STUDENTS -----")

    if not students:
        print("No students have been registered.")
        return

    for student in students.values():
        student.display_info()



def delete_student():
    print("\n----- DELETE STUDENT -----")

    student_id = input(
        "Enter Student ID to delete: "
    ).strip().upper()

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    print("\nStudent to be deleted:")
    student.display_info()

    confirmation = input(
        "\nAre you sure you want to delete "
        "this student? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
       del students[student_id]
       save_students(students)
       print("\nStudent deleted successfully!")
    else:
        ("\n Deletion Cancelled")









def update_student():
    print("\n----- UPDATE STUDENT -----")

    student_id = input(
        "Enter Student ID to update: "
    ).strip().upper()

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]
    student.display_info()

    print("\nPress Enter to keep existing information.")

    full_name = input(
        f"Full Name [{student.full_name}]: "
    ).strip() or student.full_name

    student_class = input(
        f"Class [{student.student_class}]: "
    ).strip() or student.student_class

    gender = input(
        f"Gender [{student.gender}]: "
    ).strip() or student.gender

    dob = input(
        f"Date of Birth [{student.dob}]: "
    ).strip() or student.dob

    try:
        updated_student = Student(
            student_id,
            full_name,
            student_class,
            gender,
            dob
        )

        
        updated_student.scores = student.scores.copy()
        updated_student.result_date = student.result_date

    except ValueError as error:
        print(f"Update failed: {error}")
        return

    students[student_id] = updated_student

    save_students(students)

    print("\nStudent information updated successfully!")




def search_student():
    print("\n----- SEARCH STUDENT -----")

    search_term = input(
        "Enter Student ID or Name: "
    ).strip().lower()

    if not search_term:
        print("Please enter a search term.")
        return

    found = False

    for student in students.values():
        if (
            search_term in student.student_id.lower()
            or search_term in student.full_name.lower()
        ):
            student.display_info()
            found = True

    if not found:
        print("No student found matching your search.")


def enter_student_scores():
    print("\n----- RECORD STUDENT SCORES -----")

    student_id = input(
        "Enter Student ID: "
    ).strip().upper()

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    record_scores(student)

    save_students(students)


def view_student_result():
    print("\n----- STUDENT RESULT -----")

    student_id = input(
        "Enter Student ID: "
    ).strip().upper()

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    result = calculate_result(student)

    if result is None:
        print("Student result is incomplete.")
        return

    print(f"\nName: {student.full_name}")
    print(f"Class: {student.student_class}")

    print("\nSUBJECT SCORES")

    for subject, score in student.scores.items():
        print(f"{subject}: {score}")

    print(f"\nTotal: {result['total']:.2f}/500")
    print(f"Average: {result['average']:.2f}%")
    print(f"Grade: {result['grade']}")
    print(
        f"Date Recorded: "
        f"{getattr(student, 'result_date', 'Not recorded')}"
    )



def view_report_card():
    student_id = input(
        "Enter Student ID: "
    ).strip().upper()

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]

    generate_report_card(student)



def main():
    while True:
        print("\n========== STUDENT RESULT SYSTEM ==========")
        print("1. Register Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Record/Update Student Scores")
        print("7. View Student Result")
        print("8. View Student Report Card")
        print("9. Display All Student Results")
        print("10. Rank Students")
        print("11. Sort Students by Name")
        print("12. View Class Statistics")
        print("13. Save Results Report")
        print("0. Exit")
        print("===========================================")

        choice = input("Select an option: ").strip()

        if choice == "1":
            register_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
          enter_student_scores()

        elif choice == "7":
          view_student_result()

        
        elif choice == "8":
          view_report_card()

        elif choice == "9":
          display_all_results(students)

        elif choice == "10":
          rank_students(students)
 
        elif choice == "11":
          sort_students_by_name(students)

        elif choice == "12":
          class_statistics(students)

        elif choice == "13":
          save_report(students)


        elif choice == "0":
            print("\nExiting Student Result System...")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()



