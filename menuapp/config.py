import os
from pathlib import Path

import dotenv

#ENVIROMENT VARIABLES SETTINGS
APP_ROOT = os.path.join(os.path.dirname(__file__), "")
dotenv_path = os.path.join(APP_ROOT, "../.env")
dotenv.load_dotenv(dotenv_path)

BASE_DIR = Path(__file__).resolve().parent.parent

# NAME & VERSION
PROJECT_NAME = os.getenv("PROJECT_NAME")
VERSION = os.getenv("VERSION")
# POSTGRES SETTINGS
POSTGRES_HOST: str = os.getenv("POSTGRES_HOST")
POSTGRES_PORT: int = os.getenv("POSTGRES_PORT")
POSTGRES_DB: str = os.getenv("POSTGRES_DB")
POSTGRES_USER: str = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
DATABASE_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                    f"@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
