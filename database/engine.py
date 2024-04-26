# engine.py

from models.base import Base
from models.car import Car
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL, adjust the path as necessary
DATABASE_URL = 'sqlite:///car_rental_system.db'

engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)


initial_cars = [
    Car(make="Toyota", model="Corolla", year=2020, mileage=15000, available_now=True, min_rent_period=1, max_rent_period=30),
    Car(make="Honda", model="Civic", year=2019, mileage=20000, available_now=True, min_rent_period=1, max_rent_period=30),
    Car(make="Ford", model="Focus", year=2018, mileage=22000, available_now=True, min_rent_period=3, max_rent_period=45),
    Car(make="Chevrolet", model="Malibu", year=2021, mileage=5000, available_now=True, min_rent_period=1, max_rent_period=30),
    Car(make="Tesla", model="Model 3", year=2022, mileage=10000, available_now=True, min_rent_period=1, max_rent_period=30),
]


def init_db():
    """Create all tables in the database (this should be called only once)."""
    Base.metadata.create_all(engine)
    session = Session()

    if session.query(Car).count() == 0:
        # The Car table is empty, add initial cars
        session.add_all(initial_cars)
        session.commit()
    session.close()
