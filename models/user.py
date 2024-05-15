from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)  # 'customer' or 'admin'

    def is_admin(self):
        return self.role == 'admin'

    def __str__(self):
        return f"User({self.username}, {self.password} ,{self.role})"
