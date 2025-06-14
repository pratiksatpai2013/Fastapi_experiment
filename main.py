from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional, Any 
from pydantic import BaseModel

import Models
from database import SessionLocal, engine, Base

Models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.post("/tasks/", response_model=TaskCreate)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Models.Task(title=task.title, description=task.description, completed=task.completed)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.get("/tasks/", response_model=List[TaskCreate])
def read_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Models.Task).all()
    return tasks

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}

