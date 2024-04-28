from models.car import Car, CarType

class CarFactory:
    @staticmethod
    def create_car(car_type: str, **kwargs):
        # check if the car type is valid
        if car_type not in CarType:
            raise ValueError(f"Unknown car type: {type}")
            
        if type == "Luxury":
            kwargs['min_rent_period'] = 3
            kwargs['max_rent_period'] = 30
        elif type == "Economy":
            kwargs['min_rent_period'] = 1
            kwargs['max_rent_period'] = 30
        elif type == "SUV":
            kwargs['min_rent_period'] = 2
            kwargs['max_rent_period'] = 45

        return Car(car_type=car_type, **kwargs)

        