# engine.py

from models.base import Base
from models.car import Car, CarType
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL, adjust the path as necessary
DATABASE_URL = 'sqlite:///car_rental_system.db'

INITIAL_CARS = [
    Car(make="Toyota", model="Corolla", year=2020, mileage=15000, available_now=True, min_rent_period=1, max_rent_period=30, car_type=CarType.Economy),
    Car(make="Honda", model="Civic", year=2019, mileage=20000, available_now=True, min_rent_period=1, max_rent_period=30, car_type=CarType.Economy),
    Car(make="Ford", model="Focus", year=2018, mileage=22000, available_now=True, min_rent_period=3, max_rent_period=45, car_type=CarType.Economy),
    Car(make="Chevrolet", model="Malibu", year=2021, mileage=5000, available_now=True, min_rent_period=1, max_rent_period=30, car_type=CarType.SUV),
    Car(make="Tesla", model="Model 3", year=2022, mileage=10000, available_now=True, min_rent_period=1, max_rent_period=30, car_type=CarType.Luxury),
]

class DatabaseEngine:
    _instance = None
    _engine = None
    _Session = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseEngine, cls).__new__(cls)
            cls.initialize_engine()
        return cls._instance

    @classmethod
    def initialize_engine(cls):
        if cls._engine is None:
            cls._engine = create_engine(DATABASE_URL, echo=False)
            cls._Session = sessionmaker(bind=cls._engine)
            cls.init_db()  # Ensure tables are created

    @classmethod
    def get_session(cls):
        if cls._Session is None:
            cls.initialize_engine()  # Ensure engine and session are initialized
        return cls._Session()

    
    @classmethod
    def init_db(cls):
        """Create all tables in the database (this should be called only once)."""
        Base.metadata.create_all(cls._engine)
        session = cls.get_session()

        if session.query(Car).count() == 0:
        # The Car table is empty, add initial cars
            session.add_all(INITIAL_CARS)
            session.commit()
        session.close()

    @classmethod
    def close_session(cls):
        if cls.Session is not None:
            cls._Session.remove()

    
