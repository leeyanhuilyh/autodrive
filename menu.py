from car import Car

class Menu:
    def __init__(self):
        self.cars = []
        self.car_print = ""

    def add_car(self, car: Car):
        self.cars.append(car)
        self.car_print += f"- {car.name}, ({car.x}, {car.y}) {car.direction}, {''.join(list(car.commands))}\n"
