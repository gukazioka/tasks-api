from fastapi import FastAPI
from pydantic import BaseModel
from src.database.database import database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


class Task(BaseModel):
    description: str
    is_urgent: bool 
    is_done: bool = False


@app.get('/ping')
async def ping():
    return {'message': 'pong'}


@app.post('/tasks/new')
async def register_tasks():
    pass


@app.get('/tasks')
async def get_tasks():
    return Task(description='Foo', is_urgent=True, is_done=False)
