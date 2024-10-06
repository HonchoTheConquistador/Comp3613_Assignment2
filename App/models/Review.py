from App.database import db

class Review(db.Model):
    reviewID = db.Column(db.Integer, primary_key=True)
    review_type = db.Column(db.String(50), nullable=False)  # Could be 'Feedback', 'Complaint', 'Praise', etc.
    category = db.Column(db.String(50), nullable=False)  # 'Positive' or 'Negative'
    comment = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    review_Status = db.Column(db.String(50), nullable=False)  # 'Pending', 'Approved', 'Rejected', etc.
    # Foreign keys for relationships
    StudentID = db.Column(db.Integer, db.ForeignKey('student.studentID'), nullable=False)
    StaffID = db.Column(db.Integer, db.ForeignKey('staff.staffID'), nullable=False)

    def get_json(self):
        return {
            'reviewID': self.reviewID,
            'review_type': self.review_type,
            'category': self.category,
            'comment': self.comment,
            'date': self.date,
            'review_Status': self.review_Status,
            'studentID': self.StudentID,
            'staffID': self.StaffID
        }

