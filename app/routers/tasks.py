from fastapi import APIRouter, Depends
from typing import Annotated, Optional
from app.database import SessionLocal

from sqlalchemy.orm import Session

from app.models.task import Tasks

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@router.get("/")
async def read_tasks(db: db_dependency):
    tasks = db.query(Tasks).all()
    return tasks

@router.post("/")
async def create_task(db: db_dependency, title: str, description: Optional[str] = None):
    task = Tasks(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task