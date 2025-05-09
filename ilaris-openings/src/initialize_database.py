from database_connection import connect_database

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    );
    ''')
    
    connection.commit()

def drop_tables(connection):
    cursor = connection.cursor()
    
    cursor.execute('''DROP TABLE IF EXISTS users''')
    
    connection.commit()



def initialize_database():
    connection = connect_database()
    drop_tables(connection)
    create_tables(connection)



if __name__ == "__main__":
    initialize_database()