# user_manager.py

from database.db_manager import DBManager
from models.user import User
from utils.helpers import hash_password, check_password

class UserManager:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def register_user(self, username, password, role):
        try:
            hashed_password = hash_password(password)
            query = "INSERT INTO Users (username, password, role) VALUES (?, ?, ?)"
            self.db_manager.execute_query(query, (username, hashed_password, role))
        except Exception as e:
            print(f"Failed to register user: {e}")
            raise

    def login_user(self, username, password) -> User:
        try:
            query = "SELECT * FROM Users WHERE username = ?"
            user_data = self.db_manager.execute_query(query, (username,)).fetchone()
            print(f'user:: {user_data}')
            if user_data and check_password(password, user_data[2]):
                return User(user_id=user_data[0], username=user_data[1], hashed_password=user_data[2], role=user_data[3])  # Return a user object or data tuple
            return None
        except Exception as e:
            print(f"Login failed: {e}")
            raise

    def check_user_role(self, username):
        try:
            query = "SELECT role FROM Users WHERE username = ?"
            role = self.db_manager.execute_query(query, (username,)).fetchone()
            return role[0] if role else None
        except Exception as e:
            print(f"Failed to check user role: {e}")
            raise
