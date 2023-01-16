from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from src.core import config
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.DATABASE_URL, echo=True)
Base = declarative_base()
sessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
metadata = MetaData()


def get_db():
    db_local = sessionLocal()
    try:
        yield db_local
    finally:
        db_local.close()
