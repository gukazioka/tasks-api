import sqlalchemy
import databases
from src.constants.universal import DATABASE_URL

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    'tasks',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('description', sqlalchemy.String),
    sqlalchemy.Column('is_urgent', sqlalchemy.Boolean),
    sqlalchemy.Column('is_done', sqlalchemy.Boolean)
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)