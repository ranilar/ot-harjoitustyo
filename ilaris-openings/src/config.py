import os

DIRNAME = os.path.dirname(__file__)
DATA_DIR = os.path.join(DIRNAME, "..", "data")

os.makedirs(DATA_DIR, exist_ok=True)

DATABASE_FILENAME = "database.sqlite"
DATABASE_FILEPATH = os.path.join(DATA_DIR, DATABASE_FILENAME)

TEST_DATABASE_FILENAME = "test-database.sqlite"
TEST_DATABASE_FILEPATH = os.path.join(DATA_DIR, TEST_DATABASE_FILENAME)
