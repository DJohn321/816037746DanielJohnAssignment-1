from App.database import db
from datetime import datetime

class Applied(db.Model):
    __tablename__ = 'applied'
    ID = db.Column(db.Integer, primary_key=True)
    jobID = db.Column(db.Integer, db.ForeignKey('job_postings.jobID'), nullable=False)
    applicantID = db.Column(db.Integer, db.ForeignKey('applicant.applicantID'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # Set default to current time
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, jobID, date, applicantID, status):
        self.jobID = jobID
        self.applicantID = applicantID
        self.date = date
        self.status = status
    
    def __repr__(self):
        return f"<Applied JobID:{self.jobID}, ApplicantID:{self.applicantID}, Status:{self.status}, Date:{self.date}>"


