import unittest
import sqlite3
from entities.user import User
from repositories.user_repository import UserRepository, get_user_by_row

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repo = UserRepository(self.connection)
        self.repo.create_table()

    def tearDown(self):
        self.connection.close()

    def test_create_user_and_find_by_username(self):
        user = User("testi123", "joku123")
        self.repo.create(user)

        retrieved_user = self.repo.find_by_username("testi123")

        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.username, "testi123")
        self.assertEqual(retrieved_user.password, "joku123")

    def test_find_by_username_returns_none_for_unknown_user(self):
        retrieved_user = self.repo.find_by_username("joku")
        self.assertIsNone(retrieved_user)

    def test_create_multiple_users(self):
        user1 = User("eka", "eka123")
        user2 = User("toka", "toka123")

        self.repo.create(user1)
        self.repo.create(user2)

        found1 = self.repo.find_by_username("eka")
        found2 = self.repo.find_by_username("toka")

        self.assertEqual(found1.username, "eka")
        self.assertEqual(found2.username, "toka")

    def test_create_duplicate_username_raises_error(self):
        user = User("duplikaatti", "salis1")
        self.repo.create(user)

        with self.assertRaises(sqlite3.IntegrityError):
            self.repo.create(User("duplikaatti", "salis2"))

    def test_get_user_by_row_none(self):
        self.assertIsNone(get_user_by_row(None))

