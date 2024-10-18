from student_tracker import StudentTracker


tracker = StudentTracker()


def add_student_ui():
    name = input("Enter student's name: ")
    roll_number = input("Enter roll number: ")
    tracker.add_student(name, roll_number)


def add_grades_ui():
    roll_number = input("Enter roll number: ")
    subject = input("Enter subject: ")
    grade = int(input(f"Enter grade for {subject}: "))
    tracker.add_grades(roll_number, subject, grade)


def view_student_ui():
    roll_number = input("Enter roll number: ")
    tracker.view_student_details(roll_number)


def menu():
    while True:
        print("\n1. Add Student\n2. Add Grades\n3. View Student\n4. Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            add_student_ui()
        elif choice == 2:
            add_grades_ui()
        elif choice == 3:
            view_student_ui()
        elif choice == 4:
            break
        else:
            print("Invalid option.")
            if __name__ == "_main_":
                menu()