from models.car import Car, CarType
from services.pricing_service import PricingService

class CarFactory:
    @staticmethod
    def create_or_update_car(car=None, car_type: str = None, **kwargs):
        print('car: ', car)
        print('car_type: ', car_type)
        # Determine if creating or updating
        if car is None and car_type is not None:
            # Creating a new car
            if car_type not in CarType:
                raise ValueError(f"Unknown car type: {car_type}")
            car = Car(car_type=car_type)  # Assuming Car requires car_type at instantiation
        elif car is not None and car_type is not None:
            # Updating existing car, assume car_type is set
            car_type = car.car_type
        else:
            raise ValueError("Invalid operation. Must specify either an existing car (update) or a car type (create).")

        # Apply type-specific attributes
        if car_type == CarType.Luxury:
            print('does it select the corret car type?')
            car.min_rent_period = 3
            car.max_rent_period = 30
        elif car_type == CarType.Economy:
            car.min_rent_period = 1
            car.max_rent_period = 30
        elif car_type == CarType.SUV:
            car.min_rent_period = 2
            car.max_rent_period = 45

        car.price_per_day = PricingService.get_daily_rate(car_type)

        # Apply other attributes
        for key, value in kwargs.items():
            if hasattr(car, key):
                setattr(car, key, value)

        return car

        