from App.database import db

class JobPostings(db.Model):  
    __tablename__ = 'job_postings'
    jobID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    employerID = db.Column(db.Integer, db.ForeignKey('employer.employerID'), nullable=False)

    # Relationship back to Employer
    employer = db.relationship('Employer', backref='job_postings', lazy=True)

    # Relationship back to Applied
    applications = db.relationship('Applied', backref='job_posting', lazy=True)

    def __init__(self, title, description, location, category, employerID):
        self.title = title
        self.description = description
        self.location = location
        self.category = category
        self.employerID = employerID
    
    def __repr__(self):
        return f"<JobPosting:{self.jobID}, {self.title}, Category: {self.category}, Location: {self.location}>"
