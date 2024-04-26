# engine.py

from models.base import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL, adjust the path as necessary
DATABASE_URL = 'sqlite:///car_rental_system.db'

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

def init_db():
    """Create all tables in the database (this should be called only once)."""
    Base.metadata.create_all(engine)
