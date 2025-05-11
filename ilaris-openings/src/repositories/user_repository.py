from entities.user import User
from database_connection import connect_database

def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_by_username(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )

        result = cursor.fetchone()

        return get_user_by_row(result)

    def create(self, user):
        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def create_table(self):
        cursor = self._connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            );
        """)
        self._connection.commit()


user_repository = UserRepository(connect_database())
