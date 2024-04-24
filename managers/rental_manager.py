# rental_manager.py

from database.db_manager import DBManager
from utils.helpers import validate_date

class RentalManager:
    def __init__(self, db_manager: DBManager):
        self.db_manager = db_manager

    def create_rental(self, car_id, customer_id, start_date, end_date):
        try:
            validate_date(start_date)
            validate_date(end_date)
            query = "INSERT INTO Rentals (car_id, customer_id, start_date, end_date, status) VALUES (?, ?, ?, ?, 'pending')"
            self.db_manager.execute_query(query, (car_id, customer_id, start_date, end_date))
        except Exception as e:
            print(f"Error creating rental: {e}")
            raise

    def update_rental_status(self, rental_id, status):
        try:
            query = "UPDATE Rentals SET status = ? WHERE rental_id = ?"
            self.db_manager.execute_query(query, (status, rental_id))
        except Exception as e:
            print(f"Error updating rental status: {e}")
            raise
