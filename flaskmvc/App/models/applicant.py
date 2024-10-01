from App.database import db

class Applicant(db.Model):
    __tablename__ = 'applicant'
    applicantID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    skills = db.Column(db.String(255), nullable=True)

    # Relationship to Applied
    applications = db.relationship('Applied', backref='applicant', lazy=True)

    def __init__(self, first_name, last_name, email, skills):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.skills = skills
    
    def __repr__(self):
        return f"<Applicant:{self.applicantID} FirstName:{self.first_name} LastName:{self.last_name}, Email:{self.email}>"
