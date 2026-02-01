from fastapi import FastAPI
from app.routers.jobs import jobs_router
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(jobs_router)

@app.get("/")
def say_hello():
    return {
        "message": "Hello, DevJobs!",
        "status": 200
    }