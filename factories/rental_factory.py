from datetime import datetime

from models.rental import Rental

class RentalFactory:
    @staticmethod
    def create_rental(car_id, user_id, start_date, end_date, status='pending'):
        """
        Creates a new Rental instance with the given parameters.

        Args:
        car_id (int): The ID of the car being rented.
        user_id (int): The ID of the user renting the car.
        start_date (str or datetime): The start date of the rental period.
        end_date (str or datetime): The end date of the rental period.
        status (str): The initial status of the rental, defaulting to 'pending'.

        Returns:
        Rental: The newly created Rental object.
        """
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        
        # Validate the rental dates
        if start_date >= end_date:
            raise ValueError("End date must be after start date.")
        
        # Create and return the new Rental instance
        return Rental(car_id=car_id, user_id=user_id, start_date=start_date, end_date=end_date, status=status)

    @staticmethod
    def update_rental(rental, **kwargs):
        """
        Updates an existing Rental instance with given keyword arguments.

        Args:
        rental (Rental): The Rental instance to update.
        **kwargs: Arbitrary keyword arguments corresponding to Rental attributes.

        Returns:
        Rental: The updated Rental object.
        """
        for key, value in kwargs.items():
            if hasattr(rental, key):
                setattr(rental, key, value)
            else:
                raise AttributeError(f"{key} is not a valid attribute of Rental.")
        
        # Additional validation or processing can be added here
        
        return rental
