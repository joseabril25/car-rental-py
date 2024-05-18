import enum
from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship

from .base import Base

class RentalStatus(enum.Enum):
    Pending = 0
    Approved = 1
    Rejected = 2
    Done = 3

    @classmethod
    def get_status_name(cls, value):
        """Return the name of the status for a given value."""
        for status in cls:
            if status.value == value:
                return status.name
        return None  # Optional: raise an exception or handle undefined cases

    @classmethod
    def get_rental_type_by_number(cls, number):
        """Retrieve a rental status type based on its integer representation."""
        mapping = {
            0: RentalStatus.Pending,
            1: RentalStatus.Approved,
            2: RentalStatus.Rejected,
            3: RentalStatus.Done
        }
        return mapping.get(number, None)
    
class Rental(Base):
    __tablename__ = 'rentals'

    rental_id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.car_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    start_date = Column(Date)
    end_date = Column(Date)
    cost = Column(Float)
    status = Column(Enum(RentalStatus))  # 0 ='pending', 1='approved', 2='rejected', 3='done'
    car = relationship("Car", backref="rentals")
    user = relationship("User", backref="rentals")
    
    def get_status_description(self):
        """Return the string description of the current status."""
        return self.status.name.replace('.', ' ').capitalize()
    
    def __str__(self):
        return (f"Rental ID: {self.rental_id}, Car ID: {self.car_id}, User ID: {self.user_id}, "
                f"Start Date: {self.start_date}, End Date: {self.end_date}, "
                f"Status: {self.status}")
    

