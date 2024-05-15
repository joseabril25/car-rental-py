import enum
from sqlalchemy import Column, Enum, ForeignKey, Integer, Date
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
class Rental(Base):
    __tablename__ = 'rentals'

    rental_id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.car_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    start_date = Column(Date)
    end_date = Column(Date)
    cost = Column(Integer)
    status = Column(Enum(RentalStatus))  # 0 ='pending', 1='approved', 2='rejected', 3='done'
    car = relationship("Car", backref="rentals")
    user = relationship("User", backref="rentals")

    def extend_rental(self, new_end_date):
        self.end_date = new_end_date

    def calculate_cost(self):
        days = (self.end_date - self.start_date).days
        return self.car.calculate_rental_cost(days)
    
    def get_status_description(self):
        """Return the string description of the current status."""
        return self.status.name.replace('.', ' ').capitalize()
    
    def __str__(self):
        return (f"Rental ID: {self.rental_id}, Car ID: {self.car_id}, User ID: {self.user_id}, "
                f"Start Date: {self.start_date}, End Date: {self.end_date}, "
                f"Status: {RentalStatus.get_status_name(self.status)}")
    

