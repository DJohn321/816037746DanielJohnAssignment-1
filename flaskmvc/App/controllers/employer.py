from App.models import Employer
from App.database import db

def create_employer(name, company_name, email, phone_number, address):
    """Creates a new employer."""
    new_employer = Employer(
        name=name, 
        company_name=company_name, 
        email=email, 
        phone_number=phone_number, 
        address=address
    )
    db.session.add(new_employer)
    db.session.commit()
    return new_employer

def get_employer_by_email(email):
    """Retrieves an employer by their email."""
    return Employer.query.filter_by(email=email).first()

def get_employer(id):
    """Retrieves an employer by their ID."""
    return Employer.query.get(id)

def get_all_employers():
    """Returns all employers."""
    return Employer.query.all()

def update_employer(id, name=None, company_name=None, email=None, phone_number=None, address=None):
    """Updates an existing employer's information."""
    employer = get_employer(id)
    if employer:
        if name:
            employer.name = name
        if company_name:
            employer.company_name = company_name
        if email:
            employer.email = email
        if phone_number:
            employer.phone_number = phone_number
        if address:
            employer.address = address
        db.session.add(employer)
        return db.session.commit()
    return None

def delete_employer(id):
    """Deletes an employer by their ID."""
    employer = get_employer(id)
    if employer:
        db.session.delete(employer)
        return db.session.commit()
    return None
