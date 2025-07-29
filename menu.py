from car import Car
from simulator import Simulator
from field import Field
from typing import Tuple


class Menu:
    def __init__(self) -> None:
        self.simulator = Simulator()
        self.mode = -1

    def set_field(self, field_input: str) -> None:
        field_size = field_input.split()
        assert len(field_size) == 2, "Field size must be in x y format"
        assert field_size[0].isdigit() and field_size[1].isdigit(), "Height and width must be a positive integer"
        width, height = int(field_size[0]), int(field_size[1])
        assert width > 0, "Width must be positive"
        assert height > 0, "Height must be positive"
        field = Field(width, height)
        self.simulator.set_field(field)
        print(f"You have created a field of {width} x {height}.")
        print()

    def set_mode(self, mode: str) -> None:
        assert mode in ["1", "2"], "Invalid mode"
        self.mode = mode

    def add_car(self, car_name: str, car_position: tuple, car_commands: str) -> None:
        car = Car(car_name, car_position[0], car_position[1], car_position[2])
        car.add_command(car_commands)
        self.simulator.add_car(car)
        print(self.simulator.car_print)

    def get_car_name(self, car_name: str) -> str:
        assert 0 < len(car_name) < 64, "Car name must be non-empty and less than 64 characters"
        return car_name

    def get_car_position_direction(self, car_position: str) -> Tuple[int, int, str]:
        assert len(car_position.split()) == 3, "Car position must be in x y Direction format"
        car_position = car_position.split()
        assert car_position[0].isdigit() and car_position[1].isdigit(), \
            "Car position must be a positive integer"
        assert int(car_position[0]) >= 0 and int(car_position[0]) < self.simulator.field.width, \
            "Car position must be within the field"
        assert int(car_position[1]) >= 0 and int(car_position[1]) < self.simulator.field.height, \
            "Car position must be within the field"
        assert car_position[2].upper() in ["N", "E", "S", "W"], \
            "Invalid direction. Must be N, E, S, or W (case insensitive)."
        direction = self.get_car_direction(car_position[2])
        return (int(car_position[0]), int(car_position[1]), direction)

    def get_car_direction(self, car_direction: str) -> str:
        assert car_direction.upper() in ["N", "E", "S", "W"], \
            "Invalid direction. Must be N, E, S, or W (case insensitive)."
        return car_direction.upper()

    def get_car_commands(self, car_commands: str) -> str:
        assert 0 < len(car_commands) < 128, "Car commands must be less than 128 characters"
        car_commands = car_commands.upper()
        assert all(command in ["F", "L", "R"] for command in car_commands), \
            "Invalid command. Must be f, b, l, or r (case insensitive)."
        return car_commands
