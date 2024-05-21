from models.user import User

class UserFactory:

    @staticmethod
    def create_user(user_type: str, username: str, password: str, fullname: str, passport: str) -> User:
        """Factory method to create users based on type."""
        if user_type == "admin":
            return User(fullname=fullname, passport=passport, username=username, password=password, role="admin")
        elif user_type == "customer":
            return User(fullname=fullname, passport=passport, username=username, password=password, role="customer")
        else:
            raise ValueError(f"Unknown user type: {user_type}")
        
    @staticmethod
    def update_user(user, **kwargs):
        """
        Updates an existing User instance with given keyword arguments.

        Args:
        user (User): The User instance to update.
        **kwargs: Arbitrary keyword arguments corresponding to User attributes.

        Returns:
        User: The updated User object.
        """
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
            else:
                raise AttributeError(f"{key} is not a valid attribute of User.")
        
        # Additional validation or processing can be added here
        
        return user
