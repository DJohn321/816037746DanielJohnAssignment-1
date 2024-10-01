from App.models import Applicant
from App.database import db

def create_applicant(first_name, last_name, email, skills):
    """Creates a new applicant."""
    new_applicant = Applicant(
        first_name=first_name, 
        last_name=last_name, 
        email=email, 
        skills=skills
    )
    db.session.add(new_applicant)
    db.session.commit()
    return new_applicant

def get_applicant_by_email(email):
    """Retrieves an applicant by their email."""
    return Applicant.query.filter_by(email=email).first()

def get_applicant(id):
    """Retrieves an applicant by their ID."""
    return Applicant.query.get(id)

def get_all_applicants():
    """Returns all applicants."""
    return Applicant.query.all()

def update_applicant(id, first_name=None, last_name=None, email=None, skills=None):
    """Updates an existing applicant's information."""
    applicant = get_applicant(id)
    if applicant:
        if first_name:
            applicant.first_name = first_name
        if last_name:
            applicant.last_name = last_name
        if email:
            applicant.email = email
        if skills:
            applicant.skills = skills
        db.session.add(applicant)
        return db.session.commit()
    return None

def delete_applicant(id):
    """Deletes an applicant by their ID."""
    applicant = get_applicant(id)
    if applicant:
        db.session.delete(applicant)
        return db.session.commit()
    return None



