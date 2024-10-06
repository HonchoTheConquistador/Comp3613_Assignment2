from App.models import Review
from App.database import db

# Create a new review with category (positive/negative)
def create_review(review_type, comment, date, review_status, category, studentID, staffID):
    new_review = Review(
        review_type=review_type,
        comment=comment,
        date=date,
        review_Status=review_status,
        category=category,  # New category field
        StudentID=studentID,
        StaffID=staffID
    )
    db.session.add(new_review)
    db.session.commit()
    return new_review

# Get a review by reviewID
def get_review(reviewID):
    review = Review.query.get(reviewID)
    if review:
        return review.get_json()
    return None

# Get all reviews
def get_all_reviews():
    reviews = Review.query.all()
    return [review.get_json() for review in reviews]

# Get reviews by category (positive/negative or all)
def get_reviews_by_category(category):
    if category.lower() in ["positive", "negative"]:
        reviews = Review.query.filter_by(category=category.capitalize()).all()
    else:
        reviews = Review.query.all()
    return [review.get_json() for review in reviews]

# Get reviews for a specific student
def get_reviews_for_student(studentID):
    reviews = Review.query.filter_by(StudentID=studentID).all()
    return [review.get_json() for review in reviews]

# Get reviews authored by a specific staff member
def get_reviews_by_staff(staffID):
    reviews = Review.query.filter_by(StaffID=staffID).all()
    return [review.get_json() for review in reviews]

# Update a review by reviewID, including category update
def update_review(reviewID, review_type=None, comment=None, review_status=None, category=None):
    review = Review.query.get(reviewID)
    if review:
        if review_type:
            review.review_type = review_type
        if comment:
            review.comment = comment
        if review_status:
            review.review_Status = review_status
        if category:  # Allow category update
            review.category = category
        db.session.commit()
        return review.get_json()
    return None

# Delete a review by reviewID
def delete_review(reviewID):
    review = Review.query.get(reviewID)
    if review:
        db.session.delete(review)
        db.session.commit()
        return True
    return False


