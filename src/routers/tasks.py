from fastapi import APIRouter
from pydantic import BaseModel
from src.database.database import database, tasks


router = APIRouter(
    prefix='/tasks',
    tags=['tasks']
)


class Task(BaseModel):
    description: str
    is_urgent: bool
    is_done: bool = False


@router.post('/new')
async def register_tasks(task: Task):
    """
    Register a new task on database.
    """
    last_record_id = await database.execute(tasks.insert().values(**task.dict()))
    return {**task.dict(), 'id': last_record_id}


@router.get('/')
async def get_tasks():
    """
    Get all tasks from database.
    """
    return await database.fetch_all(tasks.select())
