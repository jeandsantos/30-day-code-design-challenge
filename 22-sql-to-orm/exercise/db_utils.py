import sqlite3


# Initialize database connection
def get_db() -> sqlite3.Connection:
    connection = sqlite3.connect("events.db")
    connection.row_factory = sqlite3.Row
    return connection


# Initialize database table
def init_db():
    connection = get_db()
    with open("schema.sql") as f:
        connection.executescript(f.read())
