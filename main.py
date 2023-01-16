import uvicorn
from fastapi import FastAPI

from src.db.database import engine, Base
from src.core import config

Base.metadata.create_all(bind=engine)
app = FastAPI(
    title=config.PROJECT_NAME,
    version=config.VERSION,
    docs_url="/api/openapi",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json"
)


@app.get("/")
def root():
    return {"service": config.PROJECT_NAME, "version": config.VERSION}


if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
