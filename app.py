from flask import Flask, render_template, request, redirect, url_for
from student_tracker import StudentTracker

app = Flask(__name__)
tracker = StudentTracker()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add_student', methods=['POST'])
def add_student():
    name = request.form['name']
    roll_number = request.form['roll_number']
    tracker.add_student(name, roll_number)
    return redirect(url_for('home'))


@app.route('/add_grade', methods=['POST'])
def add_grade():
    roll_number = request.form['roll_number']
    subject = request.form['subject']
    grade = int(request.form['grade'])
    tracker.add_grades(roll_number, subject, grade)
    return redirect(url_for('home'))


@app.route('/view_student', methods=['GET', 'POST'])
def view_student():
    if request.method == 'POST':
        roll_number = request.form['roll_number']
        student = tracker.students.get(roll_number)
        if student:
            return render_template('view_student.html', student=student)
        else:
            return "Student not found", 404
    return render_template('view_form.html')


if __name__ == "_main_":
    app.run(debug=True)
    