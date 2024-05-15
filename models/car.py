# car.py

import enum
from sqlalchemy import Column, Float, Integer, String, Boolean, Enum
from models.base import Base

class CarType(enum.Enum):
    Luxury = 'Luxury'
    Economy = 'Economy'
    SUV = 'SUV'

    @classmethod
    def get_car_type_by_number(cls, number):
        mapping = {
            1: CarType.Luxury,
            2: CarType.Economy,
            3: CarType.SUV
        }

        return mapping.get(number, None)
    
class Car(Base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    mileage = Column(Integer)
    plate_number = Column(String, unique=True)
    available_now = Column(Boolean)  # Using Boolean type
    min_rent_period = Column(Integer)
    max_rent_period = Column(Integer)
    car_type = Column(Enum(CarType))
    price_per_day = Column(Float)

    def get_details(self):
        details = f"{self.year} {self.make} {self.model}, Mileage: {self.mileage}km"
        availability = "Available" if self.available_now else "Not Available"
        return f"{details}, {availability}"
    
    def get_car_type(self):
        return self.car_type.name
    
    def __str__(self):
        availability = "Available" if self.available_now else "Not Available"
        return (f"Car ID: {self.car_id}, Make: {self.make}, Model: {self.model}, "
                f"Year: {self.year}, Mileage: {f'{self.mileage:,d}'}km, "
                f"Plate Number: {self.plate_number}, "
                f"Status: {availability}, Min Rent: {self.min_rent_period} days, "
                f"Max Rent: {self.max_rent_period} days"
                f"Car Type: {self.car_type}"
                f"Daily Rate: ${self.price_per_day:.2f}")
    
