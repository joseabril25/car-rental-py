# car.py

import enum
from sqlalchemy import Column, Integer, String, Boolean, Enum
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
    
class PricingService:
    _pricing_per_day = {
        CarType.Luxury: 150,   # $150 per day for luxury cars
        CarType.Economy: 75,   # $75 per day for economy cars
        CarType.SUV: 100       # $100 per day for SUVs
    }

    @staticmethod
    def get_daily_rate(car_type):
        return PricingService._pricing_per_day.get(car_type, 0) # Return 0 if car type not found
class Car(Base):
    __tablename__ = 'cars'

    car_id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    mileage = Column(Integer)
    available_now = Column(Boolean)  # Using Boolean type
    min_rent_period = Column(Integer)
    max_rent_period = Column(Integer)
    car_type = Column(Enum(CarType))

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
                f"Status: {availability}, Min Rent: {self.min_rent_period} days, "
                f"Max Rent: {self.max_rent_period} days"
                f"Car Type: {self.car_type}"
                f"Daily Rate: {self.daily_rate}")
    
