from datetime import datetime

from managers.cars_manager import CarManager

from models.car import Car
from models.rental import Rental, RentalStatus
from services.pricing_service import PricingService
from utils.helpers import convert_string_to_date, validate_date

class RentalFactory:
    @staticmethod
    def create_rental(car, car_id, user_id, start_date, end_date):
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

        if not RentalFactory.validate_dates(start_date, end_date, car):
            raise ValueError("Invalid rental period")
        
        # Validate the rental dates
        if start_date >= end_date:
            raise ValueError("End date must be after start date.")
        
        rate = PricingService.get_daily_rate(car.car_type)
        cost = RentalFactory.calculate_cost(start_date, end_date, rate)

        # Create and return the new Rental instance
        return Rental(
            car_id=car_id, 
            user_id=user_id, 
            start_date=convert_string_to_date(start_date), 
            end_date=convert_string_to_date(end_date), 
            status=RentalStatus.Pending, 
            cost=cost)

    @staticmethod
    def update_rental(rental, **kwargs):
        print('update rental at rental_factory')
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
    
    @staticmethod
    def validate_dates(start_date, end_date, car: Car):
        """Check if the rental period is within allowed limits."""
        verified_start_date = validate_date(start_date)
        verified_end_date = validate_date(end_date)

        rental_duration = (verified_end_date - verified_start_date).days
        return car.min_rent_period <= rental_duration <= car.max_rent_period
    
    @staticmethod
    def calculate_cost(start_date, end_date, rate: float):
        verified_start_date = validate_date(start_date)
        verified_end_date = validate_date(end_date)
        """Calculate the total cost of the rental."""
        days = (verified_end_date - verified_start_date).days
        return days * rate
