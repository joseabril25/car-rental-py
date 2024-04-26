from sqlalchemy import Column, ForeignKey, Integer, String, Date
from .base import Base

class Rental(Base):
    __tablename__ = 'rentals'

    rental_id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.car_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)  # 'pending', 'approved', 'rejected'

    def extend_rental(self, new_end_date):
        self.end_date = new_end_date

    def calculate_cost(self):
        days = (self.end_date - self.start_date).days
        return self.car.calculate_rental_cost(days)
