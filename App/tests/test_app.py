import os
import tempfile
import pytest
import logging
import unittest
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from App.main import create_app
from App.database import db, create_db
from App.models import User, Student, Staff, Review
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    update_user,
    create_student,
    get_all_students,
    get_student,
    update_student,
    create_staff,
    get_all_staff,
    get_staff,
    update_staff,
    create_review,
    get_all_reviews,
    update_review,
    get_review,
    get_reviews_by_category
)

LOGGER = logging.getLogger(__name__)

# =========================
# User Tests
# =========================

class UserUnitTests(unittest.TestCase):
    """Unit tests for the User model."""

    def test_new_user(self):
        """Test creating a new user."""
        user = User("bob", "bobpass")
        assert user.username == "bob"

    def test_get_json(self):
        """Test the JSON representation of a user."""
        user = User("bob", "bobpass")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id": None, "username": "bob"})

    def test_hashed_password(self):
        """Test that the password is hashed."""
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password)
        assert user.password != password

    def test_check_password(self):
        """Test checking a user's password."""
        password = "mypass"
        user = User("bob", password)
        assert user.check_password(password)

# =========================
# User Integration Tests
# =========================

@pytest.fixture(autouse=True, scope="module")
def empty_db():
    """Create an empty database for tests and drop it after tests."""
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()

def test_authenticate():
    """Test user authentication."""
    user = create_user("bob", "bobpass")
    assert login("bob", "bobpass") is not None

class UsersIntegrationTests(unittest.TestCase):
    """Integration tests for user-related functionality."""

    def test_create_user(self):
        """Test creating a new user."""
        user = create_user("rick", "bobpass")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        """Test retrieving all users in JSON format."""
        users_json = get_all_users_json()
        self.assertListEqual([{"id": 1, "username": "bob"}, {"id": 2, "username": "rick"}], users_json)

    def test_update_user(self):
        """Test updating an existing user's username."""
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"

# =========================
# Student Tests
# =========================

class StudentUnitTests(unittest.TestCase):
    """Unit tests for the Student model."""

    def test_new_student(self):
        """Test creating a new student."""
        student = Student(name="John Doe", year=2, program="Computer Science")
        assert student.name == "John Doe"
        assert student.year == 2
        assert student.program == "Computer Science"

    def test_get_json(self):
        """Test the JSON representation of a student."""
        student = Student(name="John Doe", year=2, program="Computer Science")
        student_json = student.get_json()
        self.assertDictEqual(student_json, {"studentID": None, "name": "John Doe", "year": 2, "program": "Computer Science"})

# =========================
# Student Integration Tests
# =========================

class StudentsIntegrationTests(unittest.TestCase):
    """Integration tests for student-related functionality."""

    def test_create_student(self):
        """Test creating a new student."""
        student = create_student("John Doe", 2, "Computer Science")
        assert student.name == "John Doe"

    def test_get_all_students(self):
        """Test retrieving all students in JSON format."""
        students_json = get_all_students()
        self.assertListEqual([{"studentID": 1, "name": "John Doe", "year": 2, "program": "Computer Science"}], students_json)

    def test_update_student(self):
        """Test updating an existing student's name."""
        update_student(1, name="Jane Doe")
        student = get_student(1)
        assert student['name'] == "Jane Doe"  # Changed from .name to ['name']

# =========================
# Staff Tests
# =========================

class StaffUnitTests(unittest.TestCase):
    """Unit tests for the Staff model."""

    def test_new_staff(self):
        """Test creating a new staff member."""
        staff = Staff(name="Jane Doe", position="Manager", email="jane@example.com", department="HR")
        assert staff.name == "Jane Doe"
        assert staff.position == "Manager"
        assert staff.email == "jane@example.com"
        assert staff.department == "HR"

    def test_get_json(self):
        """Test the JSON representation of a staff member."""
        staff = Staff(name="Jane Doe", position="Manager", email="jane@example.com", department="HR")
        staff_json = staff.get_json()
        self.assertDictEqual(staff_json, {"id": None, "name": "Jane Doe", "position": "Manager", "email": "jane@example.com", "department": "HR"})

# =========================
# Staff Integration Tests
# =========================

class StaffIntegrationTests(unittest.TestCase):
    """Integration tests for staff-related functionality."""

    def test_create_staff(self):
        """Test creating a new staff member."""
        staff = create_staff("Jane Doe", "Manager", "jane@example.com", "HR")
        assert staff.name == "Jane Doe"

    def test_get_all_staff(self):
        """Test retrieving all staff in JSON format."""
        staff_json = get_all_staff()
        self.assertListEqual([{"id": 1, "name": "Jane Doe", "position": "Manager", "email": "jane@example.com", "department": "HR"}], staff_json)

    def test_update_staff(self):
        """Test updating an existing staff member's name."""
        update_staff(1, name="John Doe")
        staff = get_staff(1)
        assert staff['name'] == "John Doe"  # Changed from .name to ['name']

# =========================
# Review Tests
# =========================

class ReviewUnitTests(unittest.TestCase):
    """Unit tests for the Review model."""

    def test_new_review(self):
        """Test creating a new review."""
        review = Review(
            review_type="Feedback",
            category="Positive",
            comment="Great work",
            date=datetime(2023, 9, 30),  # Use a datetime object here
            review_Status="Approved",
            StudentID=1,
            StaffID=2
        )
        assert review.review_type == "Feedback"
        assert review.category == "Positive"
        assert review.comment == "Great work"
        assert review.review_Status == "Approved"

    def test_get_json(self):
        """Test the JSON representation of a review."""
        review = Review(
            review_type="Feedback",
            category="Positive",
            comment="Great work",
            date=datetime(2023, 9, 30),
            review_Status="Approved",
            StudentID=1,
            StaffID=2
        )
        review_json = review.get_json()
        self.assertDictEqual(review_json, {
            "reviewID": None,
            "review_type": "Feedback",
            "category": "Positive",
            "comment": "Great work",
            "date": datetime(2023, 9, 30),
            "review_Status": "Approved",
            "studentID": 1,
            "staffID": 2
        })

# =========================
# Review Integration Tests
# =========================

class ReviewsIntegrationTests(unittest.TestCase):
    """Integration tests for review-related functionality."""

    def test_create_review(self):
        """Test creating a new review."""
        review = create_review(
            "Feedback",
            "Great work",
            datetime(2023, 9, 30),
            "Approved",
            "Positive",
            1,
            2
        )
        # Add assertions to verify the review creation
        self.assertEqual(review.review_type, "Feedback")
        self.assertEqual(review.comment, "Great work")
        self.assertEqual(review.category, "Positive")
        self.assertEqual(review.review_Status, "Approved")
        self.assertEqual(review.StudentID, 1)
        self.assertEqual(review.StaffID, 2)

    def test_get_all_reviews(self):
        """Test retrieving all reviews."""
        reviews = get_all_reviews()
        self.assertEqual(len(reviews), 1)

    def test_get_reviews_by_category(self):
        """Test retrieving reviews filtered by category."""
        reviews = get_reviews_by_category("Positive")
        self.assertEqual(len(reviews), 1)

    def test_update_review(self):
        """Test updating an existing review's comment and category."""
        update_review(1, comment="Updated review", category="Negative")
        review = get_review(1)
        assert review["comment"] == "Updated review"
        assert review["category"] == "Negative"

