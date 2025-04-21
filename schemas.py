from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    completed: bool = False

class TaskCreate(BaseModel):
    title: str
    description: str
    
class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
