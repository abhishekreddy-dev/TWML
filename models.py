import sqlite3
from datetime import datetime

def init_db():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Create table if it doesn't exist, with an additional email and timestamp column
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                semester TEXT,
                major TEXT,
                netid TEXT,
                email TEXT,          -- Added email column
                purpose TEXT,
                timestamp TEXT NOT NULL  -- To store submission date and time
            )
        ''')
        
        conn.commit()  # Commit the transaction
    except sqlite3.Error as e:
        print(f"Error while initializing the database: {e}")
    finally:
        conn.close()  # Ensure the connection is closed

if __name__ == '__main__':
    init_db()
