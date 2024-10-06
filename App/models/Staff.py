from App.database import db

class Staff(db.Model):
    staffID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    department = db.Column(db.String(100), nullable=False)
    # One-to-many relationship with Review
    reviews = db.relationship('Review', backref='staff', lazy=True, cascade="all, delete-orphan")

    def get_json(self):
        return {
            'id': self.staffID,
            'name': self.name,
            'position': self.position,
            'email': self.email,
            'department': self.department
        }
