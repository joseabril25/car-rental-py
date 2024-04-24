# user_manager.py

from database.db_manager import DBManager
from utils.helpers import hash_password, check_password

import bcrypt

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

    def login_user(self, username, password):
        try:
            query = "SELECT user_id, password, role FROM Users WHERE username = ?"
            user_data = self.db_manager.execute_query(query, (username,)).fetchone()
            if user_data and check_password(password, user_data[1]):
                return user_data  # Return a user object or data tuple
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
