from fastapi import Depends, HTTPException, APIRouter

from app.db import get_db
from app.models import Job, Application
from app.schemas import JobCreate, JobUpdate, ApplicationCreate
from app.services import create_application

jobs_router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"]
)

@jobs_router.get("/")
def get_jobs(db = Depends(get_db)):
    return db.query(Job).all()


@jobs_router.post("/")
def create_job(job_data: JobCreate, db = Depends(get_db)):
    new_job = Job(**job_data.dict())

    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


@jobs_router.patch("/{job_id}")
def update_job(job_id: int, job_data: JobUpdate, db = Depends(get_db)):
    job_query = db.query(Job).filter(Job.id == job_id)
    db_job = job_query.first()

    if db_job is None:
        return HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")

    update_data = job_data.dict(exclude_unset=True)
    job_query.update(update_data, synchronize_session=False)

    db.commit()
    db.refresh(db_job)

    return db_job


@jobs_router.delete("/{job_id}")
def delete_job(job_id: int, db=Depends(get_db)):
    job_query = db.query(Job).filter(Job.id == job_id)
    db_job = job_query.first()
    if db_job is None:
        return HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")

    job_query.delete(synchronize_session=False)
    db.commit()

    return {
        "message": f"Job with id {job_id} has been deleted successfully.",
        "status": 200
    }


@jobs_router.post("/{job_id}/applications")
def apply_to_job(job_id: int, application_data: ApplicationCreate, db = Depends(get_db)):
    return create_application(db, job_id, application_data)


@jobs_router.get("/{job_id}/applications")
def list_all_applications(job_id: int, db = Depends(get_db)):
    job_query = db.query(Job).filter(Job.id == job_id)
    db_job = job_query.first()
    if db_job is None:
        return HTTPException(status_code=404, detail=f"Job with id {job_id} does not exist")

    application_query = db.query(Application).filter(Application.job_id == job_id)
    db_applications = application_query.all()

    return db_applications

