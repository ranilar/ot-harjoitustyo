import unittest
import sqlite3
import uuid

from services.user_service import UserService, InvalidCredentialsError, UsernameExistsError
from repositories.user_repository import UserRepository

def unique_username():
    return uuid.uuid4().hex[:6]

class TestUserService(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect("test-database.sqlite")
        self.connection.row_factory = sqlite3.Row

        self.user_repository = UserRepository(self.connection)
        self.user_repository.create_table()

        self.user_service = UserService()
        self.user_service._user_repository = self.user_repository

    def tearDown(self):
        self.connection.close()

    def test_register_creates_user(self):
        username = unique_username()
        self.assertTrue(self.user_service.register(username, "testi123"))

        user = self.user_repository.find_by_username(username)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)

    def test_register_duplicate_raises_error(self):
        username = unique_username()
        self.user_service.register(username, "testi123")
        with self.assertRaises(UsernameExistsError):
            self.user_service.register(username, "joku123")

    def test_login_success(self):
        username = unique_username()
        self.user_service.register(username, "testi123")
        result = self.user_service.login(username, "testi123")
        self.assertTrue(result)

    def test_login_wrong_password_raises_error(self):
        username = unique_username()
        self.user_service.register(username, "oikea")
        with self.assertRaises(InvalidCredentialsError):
            self.user_service.login(username, "väärä")

    def test_login_nonexistent_user_raises_error(self):
        with self.assertRaises(InvalidCredentialsError):
            self.user_service.login("joku123", "joku123")

    def test_get_current_user_returns_logged_in_user(self):
        username = unique_username()
        self.user_service.register(username, "testi123")
        self.user_service.login(username, "testi123")
        current_user = self.user_service.get_current_user()
        self.assertEqual(current_user.username, username)

    def test_logout_clears_current_user(self):
        username = unique_username()
        self.user_service.register(username, "testi123")
        self.user_service.login(username, "testi123")
        self.user_service.logout()
        self.assertIsNone(self.user_service.get_current_user())
