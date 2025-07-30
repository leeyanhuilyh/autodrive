from collections import deque
from .direction import DIRECTIONS


class Car:

    def __init__(self, name: str, x: int, y: int, direction: str) -> None:
        assert direction.upper() in ["N", "E", "S", "W"], "Invalid direction"
        assert x >= 0, "x must be positive"
        assert y >= 0, "y must be positive"
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = None
        self.turn_map = {
            "L": 0,
            "R": 1
        }

    def add_command(self, commands_str: str) -> None:
        self.commands = deque(commands_str)

    def turn(self, command: str) -> None:
        self.direction = DIRECTIONS[self.direction][self.turn_map[command]]
