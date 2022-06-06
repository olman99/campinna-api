import databases
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from ..config import settings

database = databases.Database(settings.POSTGRES_DATABASE_URI)

engine = sqlalchemy.create_engine(settings.POSTGRES_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
