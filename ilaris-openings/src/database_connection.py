import sqlite3
from config import DATABASE_FILEPATH

connection = sqlite3.connect(DATABASE_FILEPATH)
connection.row_factory = sqlite3.Row

def connect_database():
    """Makes connection to database"""
    return connection

def close_connection(connection):
        """Closes the database connection if it exists"""
        if connection:
            connection.close()
            connection = None