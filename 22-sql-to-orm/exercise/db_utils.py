import sqlite3


# Initialize database connection
def get_db(file_path: str) -> sqlite3.Connection:
    connection = sqlite3.connect(file_path)
    connection.row_factory = sqlite3.Row
    return connection


# Initialize database table
def init_db(file_path: str):
    connection = get_db(file_path)
    with open("schema.sql") as f:
        connection.executescript(f.read())
