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

    def run_simulation(self) -> None:
        step = 1
        while len(self.cars):
            curr_positions = {}
            to_remove = []
            print(f"Step {step}")
            for i, car in enumerate(self.cars):

                # Car successfully reached destination
                if not len(car.commands): 
                    self.end_print += f"{car.name}, ({car.x}, {car.y}) {car.direction}\n"
                    to_remove.append(i)
                    continue

                self.forward(car)
                
                # Handle car crash
                if (car.x, car.y) in curr_positions: 
                    self.end_print += f"{self.cars[curr_positions[car.x, car.y]].name}, collides with {car.name} at ({car.x}, {car.y}) at step {step}\n"
                    self.end_print += f"{car.name}, collides with {self.cars[curr_positions[car.x, car.y]].name} at ({car.x}, {car.y}) at step {step}\n"
                    to_remove.append(i)
                    to_remove.append(curr_positions[car.x, car.y])
                else:
                    # Update current positions
                    curr_positions[(car.x, car.y)] = i
            
            # remove cars in to_remove
            for i in reversed(to_remove):
                self.cars.pop(i)            
            step += 1

        print(self.end_print)