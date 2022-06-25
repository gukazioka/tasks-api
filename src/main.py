from fastapi import FastAPI
from src.constants.universal import TAGS_METADATA
from src.database.database import database
from src.routers import tasks

app = FastAPI(
    title='TasksAPI',
    description='An API to perform database operations related to tasks',
    openapi_tags=TAGS_METADATA
)
app.include_router(tasks.router)


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/ping')
async def ping():
    return {'message': 'pong'}
