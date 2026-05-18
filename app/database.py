import sqlite3
from pathlib import Path

DB_PATH = Path("/data/secrets.db")
SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        with open(SCHEMA_PATH, "r") as file:
            conn.executescript(file.read())