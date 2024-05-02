# global_state.py

from models.user import User


class GlobalState:
    _current_user = None

    @classmethod
    def set_current_user(cls, user: User):
        cls._current_user = user

    @classmethod
    def get_current_user(cls):
        return cls._current_user
    
    @classmethod
    def logout(cls):
        cls._current_user = None
