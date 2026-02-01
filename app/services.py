from fastapi import HTTPException

from app.models import Job, Application
from app.schemas import ApplicationCreate


def create_application(db, job_id, application_data: ApplicationCreate):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        return HTTPException(status_code=404, detail="Job not found")

    new_application = Application(
        **application_data.dict(),
        job_id=job.id
    )

    db.add(new_application)
    db.commit()
    db.refresh(new_application)

    return new_application
