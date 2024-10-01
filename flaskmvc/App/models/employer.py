from App.database import db

class Employer(db.Model):
    __tablename__ = 'employer'
    employerID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255), nullable=False)

    def __init__(self, name, company_name, email, phone_number, address):
        self.name = name
        self.company_name = company_name
        self.email = email
        self.phone_number = phone_number
        self.address = address
    
    def __repr__(self):
        return f"<Employer:{self.employerID} Name:{self.name}, Company:{self.company_name}>"
