import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize,
    create_job_posting, update_job_posting, delete_job_posting, 
    get_all_job_postings, get_job_postings_by_employer, get_job_postings_by_category,
    create_employer, update_employer, delete_employer, get_all_employers,
    create_applicant, update_applicant, delete_applicant, get_all_applicants,
    apply_to_job, get_applicants_by_job_id, get_job_postings_with_status
 )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

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
    

app.cli.add_command(test)


# Employer Commands Group
employer_cli = AppGroup('employer', help='Employer-related commands')

@employer_cli.command("create", help="Creates a new employer")
@click.argument("name")
@click.argument("company_name")
@click.argument("email")
@click.argument("phone_number")
@click.argument("address")
@with_appcontext
def create_employer_command(name, company_name, email, phone_number, address):
    create_employer(name, company_name, email, phone_number, address)
    print(f"Employer {name} created successfully.")

@employer_cli.command("update", help="Updates an employer's details")
@click.argument("employer_id")
@click.argument("name")
@click.argument("company_name")
@click.argument("email")
@click.argument("phone_number")
@click.argument("address")
@with_appcontext
def update_employer_command(employer_id, name, company_name, email, phone_number, address):
    update_employer(employer_id, name, company_name, email, phone_number, address)
    print(f"Employer {name} updated successfully.")

@employer_cli.command("delete", help="Deletes an employer")
@click.argument("employer_id")
@with_appcontext
def delete_employer_command(employer_id):
    delete_employer(employer_id)
    print(f"Employer {employer_id} deleted successfully.")

@employer_cli.command("list", help="Lists all employers")
@with_appcontext
def list_employers_command():
    employers = get_all_employers()
    for employer in employers:
        print(employer)

app.cli.add_command(employer_cli)

# Job Posting Commands Group
job_cli = AppGroup('job', help='Job-related commands')

@job_cli.command("create", help="Creates a new job posting")
@click.argument("title")
@click.argument("description")
@click.argument("location")
@click.argument("category")
@click.argument("employer_id")
@with_appcontext
def create_job_command(title, description, location, category, employer_id):
    create_job_posting(title, description, location, category, employer_id)
    print(f"Job '{title}' created successfully.")

@job_cli.command("update", help="Updates a job posting")
@click.argument("job_id")
@click.argument("title")
@click.argument("description")
@click.argument("location")
@click.argument("category")
@click.argument("employer_id")
@with_appcontext
def update_job_command(job_id, title, description, location, category, employer_id):
    update_job_posting(job_id, title, description, location, category, employer_id)
    print(f"Job {job_id} updated successfully.")

@job_cli.command("delete", help="Deletes a job posting")
@click.argument("job_id")
@with_appcontext
def delete_job_command(job_id):
    delete_job_posting(job_id)
    print(f"Job {job_id} deleted successfully.")

@job_cli.command("list", help="Lists all job postings")
@with_appcontext
def list_jobs_command():
    jobs = get_all_job_postings()
    for job in jobs:
        print(job)

@job_cli.command("list-category", help="Lists jobs by category")
@click.argument("category")
@with_appcontext
def list_jobs_by_category_command(category):
    jobs = get_job_postings_by_category(category)
    for job in jobs:
        print(job)

@job_cli.command("list-employer", help="Lists jobs by employer")
@click.argument("employer_id")
@with_appcontext
def list_jobs_by_employer_command(employer_id):
    jobs = get_job_postings_by_employer(employer_id)
    for job in jobs:
        print(job)

app.cli.add_command(job_cli)

# Applicant Commands Group
applicant_cli = AppGroup('applicant', help='Applicant-related commands')

@applicant_cli.command("create", help="Creates a new applicant")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("email")
@click.argument("skills")
@with_appcontext
def create_applicant_command(first_name, last_name, email, skills):
    create_applicant(first_name, last_name, email, skills)
    print(f"Applicant {first_name} {last_name} created successfully.")

@applicant_cli.command("update", help="Updates an applicant's details")
@click.argument("applicant_id")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("email")
@click.argument("skills")
@with_appcontext
def update_applicant_command(applicant_id, first_name, last_name, email, skills):
    update_applicant(applicant_id, first_name, last_name, email, skills)
    print(f"Applicant {applicant_id} updated successfully.")

@applicant_cli.command("delete", help="Deletes an applicant")
@click.argument("applicant_id")
@with_appcontext
def delete_applicant_command(applicant_id):
    delete_applicant(applicant_id)
    print(f"Applicant {applicant_id} deleted successfully.")

@applicant_cli.command("list", help="Lists all applicants")
@with_appcontext
def list_applicants_command():
    applicants = get_all_applicants()
    for applicant in applicants:
        print(applicant)

app.cli.add_command(applicant_cli)

# Application (Applied) Commands Group
application_cli = AppGroup('application', help='Job application-related commands')

@application_cli.command("apply", help="Apply for a job")
@click.argument("applicant_id")
@click.argument("job_id")
@with_appcontext
def apply_to_job_command(applicant_id, job_id):
    apply_to_job(applicant_id, job_id)
    print(f"Applicant {applicant_id} applied to job {job_id} successfully.")

@application_cli.command("view-applicants", help="View applicants by job ID")
@click.argument("job_id")
@with_appcontext
def view_applicants_by_job_command(job_id):
    applicants = get_applicants_by_job_id(job_id)
    for applicant in applicants:
        print(applicant)

app.cli.add_command(application_cli)