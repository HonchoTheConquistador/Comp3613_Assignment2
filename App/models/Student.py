from App.database import db

class Student(db.Model):
    studentID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    program = db.Column(db.String(100), nullable=False)
    # One-to-many relationship with Review
    reviews = db.relationship('Review', backref='student', lazy=True, cascade="all, delete-orphan")

    def get_json(self):
        return {
            'studentID': self.studentID,
            'name': self.name,
            'year': self.year,
            'program': self.program
        }
