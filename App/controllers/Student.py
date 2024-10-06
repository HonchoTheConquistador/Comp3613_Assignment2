from App.models import Student, Review
from App.database import db

# Create a new student
def create_student(name, year, program):
    new_student = Student(name=name, year=year, program=program)
    db.session.add(new_student)
    db.session.commit()
    return new_student

# Get a student by studentID
def get_student(studentID):
    student = Student.query.get(studentID)
    if student:
        return student.get_json()
    return None

# Get all students
def get_all_students():
    students = Student.query.all()
    return [student.get_json() for student in students]

# Update a student by studentID
def update_student(studentID, name=None, year=None, program=None):
    student = Student.query.get(studentID)
    if student:
        if name:
            student.name = name
        if year:
            student.year = year
        if program:
            student.program = program
        db.session.commit()
        return student.get_json()
    return None

# Delete a student by studentID
def delete_student(studentID):
    student = Student.query.get(studentID)
    if student:
        db.session.delete(student)
        db.session.commit()
        return True
    return False


