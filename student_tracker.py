class Student:
    def _init_(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:  # Ensuring valid grade
            self.grades[subject] = grade
        else:
            print(f"Invalid grade for {subject}. Must be between 0 and 100.")

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def display_details(self):
        print(f"Student Name: {self.name}, Roll Number: {self.roll_number}")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")
        print(f"Average Grade: {self.calculate_average():.2f}")


class StudentTracker:
    def _init_(self):
        self.students = {}

    def add_student(self, name, roll_number):
        if roll_number in self.students:
            print(f"Student with roll number {roll_number} already exists.")
        else:
            self.students[roll_number] = Student(name, roll_number)

    def add_grades(self, roll_number, subject, grade):
        if roll_number in self.students:
            self.students[roll_number].add_grade(subject, grade)
        else:
            print(f"Student with roll number {roll_number} not found.")

    def view_student_details(self, roll_number):
        if roll_number in self.students:
            self.students[roll_number].display_details()
        else:
            print(f"Student with roll number {roll_number} not found.")

    def calculate_average(self, roll_number):
        if roll_number in self.students:
            return self.students[roll_number].calculate_average()
        else:
            print(f"Student with roll number {roll_number} not found.")
            return None