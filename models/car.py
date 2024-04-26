# car.py

from sqlalchemy import Column, Integer, String, Boolean
from .base import Base

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

    def get_details(self):
        details = f"{self.year} {self.make} {self.model}, Mileage: {self.mileage}km"
        availability = "Available" if self.available_now else "Not Available"
        return f"{details}, {availability}"
    
    def __str__(self):
        availability = "Available" if self.available_now else "Not Available"
        return (f"Car ID: {self.car_id}, Make: {self.make}, Model: {self.model}, "
                f"Year: {self.year}, Mileage: {f'{self.mileage:,d}'}km, "
                f"Status: {availability}, Min Rent: {self.min_rent_period} days, "
                f"Max Rent: {self.max_rent_period} days")
