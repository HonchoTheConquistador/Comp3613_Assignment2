
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/uwidcit/flaskmvc)
<a href="https://render.com/deploy?repo=https://github.com/uwidcit/flaskmvc">
  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
</a>

# Flask Commands

# The `wsgi.py` file is a utility script for performing various tasks related to the project. You can use it to import and test any code in the project. To create a manager command function, follow the example below:

```python
# inside wsgi.py

app = create_app()
migrate = get_migrate(app)

# Command to initialize the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('Database initialized')

'''
User Commands
'''
user_cli = AppGroup('user', help='User object commands')

@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# Example execution:
# $ flask user create myuser mypassword

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

# Example execution:
# $ flask user list string

app.cli.add_command(user_cli)  # Add the group to the CLI

'''
Student Commands
'''
student_cli = AppGroup('student', help='Student object commands')

# Create a new student
@student_cli.command("create", help="Creates a student")
@click.argument("name")
@click.argument("year", type=int)
@click.argument("program")
def create_student_command(name, year, program):
    create_student(name, year, program)
    print(f'Student {name} created!')

# Example execution:
# $ flask student create JohnDoe 2023 ComputerScience

# List all students
@student_cli.command("list", help="Lists all students")
def list_students_command():
    print(get_all_students())

# Example execution:
# $ flask student list

# Update a student by studentID
@student_cli.command("update", help="Updates a student")
@click.argument("student_id", type=int)
@click.argument("name", required=True)
@click.argument("year", type=int, required=True)
@click.argument("program", required=True)
def update_student_command(student_id, name, year, program):
    updated_student = update_student(student_id, name=name, year=year, program=program)
    if updated_student:
        print(f'Student {student_id} updated: {updated_student}')
    else:
        print(f'Student {student_id} not found.')
        
# Example execution:
# $ flask student update 1 JaneDoe 2024 InformationTechnology

# Delete a student by studentID
@student_cli.command("delete", help="Deletes a student")
@click.argument("student_id", type=int)
def delete_student_command(student_id):
    success = delete_student(student_id)
    if success:
        print(f'Student {student_id} deleted!')
    else:
        print(f'Student {student_id} not found.')

# Example execution:
# $ flask student delete 1

app.cli.add_command(student_cli)  # Add the group to the CLI

'''
Staff Commands
'''
staff_cli = AppGroup('staff', help='Staff object commands')

# Create a new staff member
@staff_cli.command("create", help="Creates a staff member")
@click.argument("name")
@click.argument("position")
@click.argument("email")
@click.argument("department")
def create_staff_command(name, position, email, department):
    create_staff(name, position, email, department)
    print(f'Staff member {name} created!')

# Example execution:
# $ flask staff create AliceManager Manager alice@example.com HR

# List all staff members
@staff_cli.command("list", help="Lists all staff members")
def list_staff_command():
    print(get_all_staff())

# Example execution:
# $ flask staff list

# Update a staff member by staffID
@staff_cli.command("update", help="Updates a staff member")
@click.argument("staff_id", type=int)
@click.argument("name")
@click.argument("position")
@click.argument("email")
@click.argument("department")
def update_staff_command(staff_id, name, position, email, department):
    updated_staff = update_staff(staff_id, name=name, position=position, email=email, department=department)
    if updated_staff:
        print(f'Staff {staff_id} updated: {updated_staff}')
    else:
        print(f'Staff {staff_id} not found.')
        
# Example execution:
# $ flask staff update 1 BobSupervisor Supervisor bob@example.com Marketing

# Delete a staff member by staffID
@staff_cli.command("delete", help="Deletes a staff member")
@click.argument("staff_id", type=int)
def delete_staff_command(staff_id):
    success = delete_staff(staff_id)
    if success:
        print(f'Staff {staff_id} deleted!')
    else:
        print(f'Staff {staff_id} not found.')

# Example execution:
# $ flask staff delete 1

app.cli.add_command(staff_cli)  # Add the group to the CLI

'''
Review Commands
'''
review_cli = AppGroup('review', help='Review object commands')

# Create a review
@review_cli.command("create", help="Creates a review")
@click.argument("review_type")
@click.argument("comment")
@click.argument("date")  # Pass as string; convert to date later
@click.argument("review_status")
@click.argument("category")
@click.argument("student_id", type=int)
@click.argument("staff_id", type=int)
def create_review_command(review_type, comment, date, review_status, category, student_id, staff_id):
    date = datetime.strptime(date, "%Y-%m-%d")  # Convert date to datetime
    create_review(review_type, comment, date, review_status, category, student_id, staff_id)
    print('Review created!')

# Example execution:
# $ flask review create positive "Great work!" 2024-09-30 approved feedback 1 1

# List all reviews
@review_cli.command("list", help="Lists all reviews")
def list_reviews_command():
    reviews = get_all_reviews()
    print(reviews)

# Example execution:
# $ flask review list

# List reviews by category (e.g., "positive" or "negative")
@review_cli.command("list-category", help="Lists reviews by category")
@click.argument("category")
def list_reviews_by_category_command(category):
    reviews = get_reviews_by_category(category)
    print(reviews)

# Example execution:
# $ flask review list-category positive

# List reviews for a specific student
@review_cli.command("student", help="Lists reviews for a specific student")
@click.argument("student_id", type=int)
def list_reviews_for_student_command(student_id):
    reviews = get_reviews_for_student(student_id)
    print(reviews)

# Example execution:
# $ flask review student 1

# List reviews authored by a specific staff member
@review_cli.command("staff", help="Lists reviews authored by a specific staff member")
@click.argument("staff_id", type=int)
def list_reviews_for_staff_command(staff_id):
    reviews = get_reviews_by_staff(staff_id)
    print(reviews)

# Example execution:
# $ flask review staff 1

@review_cli.command("update", help="Updates a review")
@click.argument("review_id", type=int)
@click.argument("review_type")
@click.argument("comment")
@click.argument("review_status")
@click.argument("category")
def update_review_command(review_id, review_type, comment, review_status, category):
    updated_review = update_review(review_id, review_type, comment, review_status, category)
    if updated_review:
        print(f"Review {review_id} updated: {updated_review}")
    else:
        print(f"Review {review_id} not found.")

# Example execution:
# $ flask review update 1 positive "Excellent work!" approved feedback

# Delete a review by reviewID
@review_cli.command("delete", help="Deletes a review")
@click.argument("review_id", type=int)
def delete_review_command(review_id):
    success = delete_review(review_id)
    if success:
        print(f"Review {review_id} deleted!")
    else:
        print(f"Review {review_id} not found.")

# Example execution:
# $ flask review delete 1

app.cli.add_command(review_cli)  # Add the group to the CLI

'''
Test Commands
'''
test = AppGroup('test', help='Testing commands')

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))

# Example execution:
# $ flask test user unit

@test.command("student", help="Run Student tests")
@click.argument("type", default="all")
def student_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "StudentUnitTests", "App/tests/test_app.py"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "StudentIntegrationTests", "App/tests/test_app.py"]))
    else:
        sys.exit(pytest.main(["-k", "Student", "App/tests/test_app.py"]))

# Example execution:
# $ flask test student unit/init

@test.command("staff", help="Run Staff tests")
@click.argument("type", default="all")
def staff_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "StaffUnitTests", "App/tests/test_app.py"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "StaffIntegrationTests", "App/tests/test_app.py"]))
    else:
        sys.exit(pytest.main(["-k", "Staff", "App/tests/test_app.py"]))

# Example execution:
# $ flask test staff unit/init

@test.command("review", help="Run Review tests")
@click.argument("type", default="all")
def review_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "ReviewUnitTests", "App/tests/test_app.py"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "ReviewIntegrationTests", "App/tests/test_app.py"]))
    else:
        sys.exit(pytest.main(["-k", "Review", "App/tests/test_app.py"]))

# Example execution:
# $ flask test review unit/init


#app.cli.add_command(test)  # Add the test group to the CLI
# To Test all

#Example :
#flask test user
#flask test student
#flask test staff
#flask test review



# Running the Project

#For development, run the serve command:

#bash
#$ flask run

