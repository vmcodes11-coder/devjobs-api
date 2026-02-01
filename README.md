
# DevJobs API

A professional REST API for a job platform, built with Python using FastAPI. It allows users to view, post, update and delete jobs, and to apply to listing.


## Tech Stack
- **Language**: Python 3.11
- **Framework**: FastAPI
- **Database**: SQLite (SQLAlchemy ORM)
- **Validation**: Pydantic
- **Tools**: Uvicorn

## How to run
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements
```
3. Run the server:
```bash
uvicorn app.main:app --reload --port 8001 
```
4. Open Swagger UI (docs)
```
http://127.0.0.1:8001
```

## Features
- CRUD operations for Jobs
- Data validation & Serialization
- Application system (Relationships)
- Modular Architecture (Router/Controller/Service)



Created by: Nume Prenume
