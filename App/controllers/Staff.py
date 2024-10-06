from App.models import Staff, Review
from App.database import db

# Create a new staff member
def create_staff(name, position, email, department):
    new_staff = Staff(name=name, position=position, email=email, department=department)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff

# Get a staff member by staffID
def get_staff(staffID):
    staff = Staff.query.get(staffID)
    if staff:
        return staff.get_json()
    return None

# Get all staff members
def get_all_staff():
    staff = Staff.query.all()
    return [staff.get_json() for staff in staff]

# Update a staff member by staffID
def update_staff(staffID, name=None, position=None, email=None, department=None):
    staff = Staff.query.get(staffID)
    if staff:
        if name:
            staff.name = name
        if position:
            staff.position = position
        if email:
            staff.email = email
        if department:
            staff.department = department
        db.session.commit()
        return staff.get_json()
    return None

# Delete a staff member by staffID
def delete_staff(staffID):
    staff = Staff.query.get(staffID)
    if staff:
        db.session.delete(staff)
        db.session.commit()
        return True
    return False


