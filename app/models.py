from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    description = Column(String)
    salary = Column(Integer)

    is_remote = Column(Boolean, default=False)

    applications = relationship("Application", back_populates="job")

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    applicant_name = Column(String)
    applicant_email = Column(String)
    linkedin_url = Column(String)

    job_id = Column(Integer, ForeignKey("jobs.id"))

    job = relationship("Job", back_populates="applications")