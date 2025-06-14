from sqlalchemy import Column, Integer, String, create_engine
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Integer, default=0)  # 0 for False, 1 for True




