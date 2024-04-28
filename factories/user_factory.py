from models.user import User

class UserFactory:
    @staticmethod
    def create_user(user_type: str, username: str, password: str) -> User:
        """Factory method to create users based on type."""
        if user_type == "admin":
            return User(username=username, password=password, role="admin")
        elif user_type == "customer":
            return User(username=username, password=password, role="customer")
        else:
            raise ValueError(f"Unknown user type: {user_type}")
