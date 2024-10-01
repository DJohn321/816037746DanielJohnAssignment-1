from App.models import JobPostings, Applied
from App.database import db

def create_job_posting(title, description, location, category, employerID):
    """Creates a new job posting."""
    new_job_posting = JobPostings(
        title=title, 
        description=description, 
        location=location, 
        category=category, 
        employerID=employerID
    )
    db.session.add(new_job_posting)
    db.session.commit()
    return new_job_posting

def get_job_posting_by_title(title):
    """Retrieves a job posting by its title."""
    return JobPostings.query.filter_by(title=title).first()

def get_job_posting(id):
    """Retrieves a job posting by its ID."""
    return JobPostings.query.get(id)

def get_all_job_postings():
    """Returns all job postings."""
    return JobPostings.query.all()

def update_job_posting(id, title=None, description=None, location=None, category=None):
    """Updates an existing job posting."""
    job_posting = get_job_posting(id)
    if job_posting:
        if title:
            job_posting.title = title
        if description:
            job_posting.description = description
        if location:
            job_posting.location = location
        if category:
            job_posting.category = category
        db.session.add(job_posting)
        return db.session.commit()
    return None

def delete_job_posting(id):
    """Deletes a job posting by its ID."""
    job_posting = get_job_posting(id)
    if job_posting:
        db.session.delete(job_posting)
        return db.session.commit()
    return None

def job_posting_to_dict(job_posting):
    return {
        'id': job_posting.jobID,
        'title': job_posting.title,
        'description': job_posting.description,
        'location': job_posting.location,
        'category': job_posting.category,
        'employer_id': job_posting.employerID
    }

# Get job postings by employer ID
def get_job_postings_by_employer(employer_id):
    jobs = JobPostings.query.filter_by(employerID=employer_id).all()
    if jobs:
        return [job_posting_to_dict(job) for job in jobs]
    return []

# Get job postings by category
def get_job_postings_by_category(category):
    jobs = JobPostings.query.filter_by(category=category).all()
    if jobs:
        return [job_posting_to_dict(job) for job in jobs]
    return []

def get_job_postings_with_status(applicant_id):
    """Retrieve all job postings with application status for the given applicant."""
    job_postings = JobPostings.query.all()
    jobs_with_status = []
    
    for job in job_postings:
        # Check if the applicant has applied for this job
        application = Applied.query.filter_by(applicantID=applicant_id, jobID=job.id).first()
        
        if application:
            status = application.status
        else:
            status = "Not Applied"
        
        # Collect job info with status
        jobs_with_status.append({
            "job_id": job.id,
            "job_title": job.title,
            "status": status
        })
    
    return jobs_with_status

