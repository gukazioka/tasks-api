from email.policy import HTTP
from fastapi import APIRouter, HTTPException
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


@router.put('/tasks/done/{boolean}/{task_id}')
async def update_tasks(boolean: bool, task_id: int):
    """
    Receive a task id and boolean status, then update a task
    """
    response = await database.execute(tasks.update().where(tasks.c.id == task_id).values(is_done = boolean))

    if not response:
        raise HTTPException(status_code=404)


@router.delete('/tasks/del/{task_id}')
async def delete_tasks(task_id: int):
    """
    Receive an id and delete a task corresponding to it.
    """
    response = await database.execute(tasks.delete().where(tasks.c.id == task_id))

    if not response:
        raise HTTPException(status_code=404)
