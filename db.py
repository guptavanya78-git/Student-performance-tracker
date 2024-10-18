import sqlite3

conn = sqlite3.connect('students.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE students
             (name text, roll_number text, grades text)''')

conn.commit()
conn.close()
