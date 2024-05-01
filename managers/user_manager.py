# user_manager.py
from prettytable import PrettyTable
from models.user import User
from states.global_state import GlobalState
from utils.helpers import hash_password, check_password
from database.engine import DatabaseEngine
from factories.user_factory import UserFactory

class UserManager:
    def __init__(self, current_user=None):
        self.session = DatabaseEngine.get_session()
        self.current_user = current_user

    def register_user(self, username, password, role):
        try:
            # new_user = User(username=username, password=hash_password(password), role=role)
            new_user = UserFactory.create_user(role, username, hash_password(password))
            self.session.add(new_user)
            self.session.commit()
        except Exception as e:
            print(f"Failed to register user: {e}")
            self.session.rollback()
            raise

    def login_user(self, username, password) -> User:
        try:
            user = self.session.query(User).filter(User.username == username).one_or_none()
            if user and check_password(password, user.password):
                return user
            return None
        except Exception as e:
            print(f"Login failed: {e}")
            self.session.rollback()
            raise

    def get_all_users(self):
        try:
                user = self.session.query(User).all()
                user_table = self.display_users(user)
                return user_table
        except Exception as e:
            print(f"Error retrieving available cars: {e}")
            self.session.rollback()
            raise

    def display_users(self, users):
        table = PrettyTable()
        table.field_names = ["User ID", "Username", "User Role"]

        for user in users:
            table.add_row([user.user_id, user.username, user.role])

        print(table)
