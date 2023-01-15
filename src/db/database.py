from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from core import config

engine = create_engine(config.DATABASE_URL, echo=True)
db = declarative_base()
