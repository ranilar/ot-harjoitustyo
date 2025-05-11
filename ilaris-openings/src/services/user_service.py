from entities.user import User
from repositories.user_repository import user_repository

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class UserService:
    def __init__(self):
        self._user_repository = user_repository
        self._user = None

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user
        return True

    def get_current_user(self):
        return self._user

    def logout(self):
        self._user = None

    def register(self, username, password, login=True):
        user_exists = self._user_repository.find_by_username(username)
        if user_exists:
            raise UsernameExistsError("That username already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user
        return True
