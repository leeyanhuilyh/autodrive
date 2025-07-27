from field import Field
from car import Car
from typing import List

class Simulator:

    def __init__(self, field: Field = None, cars: List[Car] = None):
        self.field = field
        self.cars = cars if cars is not None else []
        self.car_print = ""
        self.direction_map = {
            "N": (0, 1),
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0)
        }
        self.end_state = {} # (x, y) -> (car1, car2, 1 or 0, direction, step), where 1 means collision, 0 means complete  
        self.end_print = ""

    def add_car(self, car: Car) -> None:
        self.cars.append(car)
        self.car_print += f"- {car.name}, ({car.x}, {car.y}) {car.direction}, {''.join(list(car.commands))}\n"

    def set_field(self, field: Field) -> None:
        self.field = field

    def forward(self, car: Car) -> None:
        command = car.commands.popleft()
        if command == "F":
            x, y = car.x, car.y
            dx, dy = self.direction_map[car.direction]
            x += dx
            y += dy
            if not (x < 0 or x >= self.field.width \
                or y < 0 or y >= self.field.height):
                car.x, car.y = x, y
            else:
                print(f"Car {car.name} hit the wall")
        else:
            car.turn(command)