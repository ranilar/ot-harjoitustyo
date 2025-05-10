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
            "SELECT * FROM Users WHERE username = ?",
            (username,)
        )
        
        result = cursor.fetchone()
        
        return get_user_by_row(result)

    def create(self, user):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            todo: Tallennettava käyttäjä User-oliona.

        Returns:
            Tallennettu käyttjä User-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into Users (username, password_hash) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

user_repository = UserRepository(connect_database())