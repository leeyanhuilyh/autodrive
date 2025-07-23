from collections import deque

class Car:

    def __init__(self, name: str, x: int, y: int, direction: str):
        assert direction.lower() in ["n", "e", "s", "w"], "Invalid direction"
        assert x >= 0, "x must be positive"
        assert y >= 0, "y must be positive"
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = None

    def add_command(self, commands_str: str):
        self.commands = deque(commands_str)
