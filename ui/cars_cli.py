from managers.cars_manager import CarManager

class CarsCLI():
    def __init__(self, current_user=None):
        self.car_manager = CarManager()
        self.current_user = current_user

    def view_available_cars(self):
        try:
            cars = self.car_manager.get_available_cars(self.current_user.is_admin())
            if len(cars) < 1:
                print("No cars available.")
            
            self.car_manager.display_cars(cars)
        except Exception as e:
            print(f"Failed to retrieve available cars: {e}")