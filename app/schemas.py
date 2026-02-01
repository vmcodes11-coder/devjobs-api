from pydantic import BaseModel
from typing import Optional

class JobCreate(BaseModel):
    title: str
    company: str
    description: Optional[str] = None

    salary: int
    is_remote: bool = False

class JobUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    description: Optional[str] = None

    salary: Optional[int] = None
    is_remote: Optional[bool] = None


class ApplicationCreate(BaseModel):
    applicant_name: str
    applicant_email: str
    linkedin_url: Optional[str] = None