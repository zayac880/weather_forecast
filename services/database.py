import sqlite3


class Database:
    """A class for interacting with a SQLite database."""
    def __init__(self):
        self.create_table()
        self.add_default_users()

    def get_db(self):
        """Method for obtaining a database connection."""
        return sqlite3.connect('users.db')

    def create_table(self):
        """Method to create a user table if it does not exist."""
        db = self.get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY, username TEXT, balance INTEGER)''')
        db.commit()

    def add_default_users(self):
        """Method for adding users to the database when the application starts."""
        users_data = [
            ("user1", 5000),
            ("user2", 7000),
            ("user3", 9000),
            ("user4", 11000),
            ("user5", 13000)
        ]
        self.add_users(users_data)

    def add_users(self, users_data):
        """Method for adding users to the database."""
        db = self.get_db()
        cursor = db.cursor()
        cursor.executemany('INSERT INTO users (username, balance) VALUES (?, ?)', users_data)
        db.commit()

    def get_balance(self, user_id):
        """Method for getting user's balance from database."""
        db = self.get_db()
        cursor = db.cursor()
        cursor.execute('SELECT balance FROM users WHERE id = ?', (user_id,))
        result = cursor.fetchone()
        db.close()
        return result[0] if result else 0

    def update_balance(self, user_id, new_balance):
        """Method for updating the user's balance in the database."""
        if self.get_balance(user_id) is not None:
            db = self.get_db()
            cursor = db.cursor()
            cursor.execute('UPDATE users SET balance = ? WHERE id = ?', (new_balance, user_id))
            db.commit()
            db.close()
