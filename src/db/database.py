import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER', 'sergey')}" \
                          f":{os.getenv('POSTGRES_PASSWORD', 2709)}" \
                          f"@{os.getenv('POSTGRES_HOST', 'localhost')}" \
                          f":{os.getenv('POSTGRES_PORT', 5432)}/" \
                          f"{os.getenv('POSTGRES_DB', 'test_menu')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
