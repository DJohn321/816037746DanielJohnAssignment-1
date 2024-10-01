from App.models import Applied, Applicant, JobPostings
from App.database import db
from datetime import datetime

def apply_to_job(applicantID, jobID):
    """Applies applicant for a job posting."""
    applicant = Applicant.query.get(applicantID)
    job = JobPostings.query.get(jobID)
    
    if not applicant or not job:
        return None  # Applicant or Job doesn't exist
    
    new_application = Applied(
        applicantID=applicantID, 
        jobID=jobID, 
        date=datetime.utcnow(), 
        status="Applied"
    )
    db.session.add(new_application)
    db.session.commit()
    return new_application

def get_jobs_applied_by_applicant(applicantID):
    """Returns all jobs an applicant has applied to."""
    applicant = Applicant.query.get(applicantID)
    if not applicant:
        return None  # Applicant doesn't exist
    
    return applicant.applied  # Uses relationship between Applicant and Applied

def get_applicants_for_job(jobID):
    """Returns all applicants for a given job posting."""
    job = JobPostings.query.get(jobID)
    if not job:
        return None  # Job doesn't exist
    
    return job.applicants  # Uses relationship between JobPostings and Applied

def applicant_to_dict(applicant):
    return {
        'id': applicant.applicantID,
        'first_name': applicant.first_name,
        'last_name': applicant.last_name,
        'email': applicant.email,
        'skills': applicant.skills
    }

# Get applicants by job ID (requires 'Applied' as a bridge table)
def get_applicants_by_job_id(job_id):
    applied_records = Applied.query.filter_by(jobID=job_id).all()
    if applied_records:
        applicants = [applicant_to_dict(Applicant.query.get(app.applicantID)) for app in applied_records]
        return applicants
    return []

