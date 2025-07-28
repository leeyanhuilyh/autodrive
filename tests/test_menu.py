import pytest
from menu import Menu
from car import Car


@pytest.mark.parametrize("field_input, expected_width, expected_height", [
    ("10 10", 10, 10),
    ("5 3", 5, 3),
    ("1 1", 1, 1),
    ("100 50", 100, 50),
])
def test_set_field_valid(field_input, expected_width, expected_height):
    menu = Menu()
    menu.set_field(field_input)
    assert menu.simulator.field.width == expected_width
    assert menu.simulator.field.height == expected_height


@pytest.mark.parametrize("field_input", [
    "10",           # Missing height
    "10 10 10",     # Too many values
    "0 10",         # Zero width
    "10 0",         # Zero height
    "-1 10",        # Negative width
    "10 -1",        # Negative height
    "abc def",      # Non-numeric values
    "",             # Empty string
])
def test_set_field_invalid(field_input):
    menu = Menu()
    with pytest.raises(AssertionError):
        menu.set_field(field_input)


@pytest.mark.parametrize("mode", ["1", "2"])
def test_set_mode_valid(mode):
    menu = Menu()
    menu.set_mode(mode)
    assert menu.mode == mode


@pytest.mark.parametrize("mode", ["0", "3", "a", "12", ""])
def test_set_mode_invalid(mode):
    menu = Menu()
    with pytest.raises(AssertionError):
        menu.set_mode(mode)


# TODO: Test not proper
def test_add_car():
    menu = Menu()
    menu.set_field("10 10")
    car_name = "TestCar"
    car_position = (5, 5, "N")
    car_commands = "FFR"
    
    menu.add_car(car_name, car_position, car_commands)
    
    assert len(menu.simulator.cars) == 1
    car = menu.simulator.cars[0]
    assert car.name == car_name
    assert car.x == car_position[0]
    assert car.y == car_position[1]
    assert car.direction == car_position[2]
    assert ''.join(list(car.commands)) == car_commands


@pytest.mark.parametrize("car_name", [
    "A", "TestCar", "Car123", "a" * 63  # Valid names
])
def test_get_car_name_valid(car_name):
    menu = Menu()
    result = menu.get_car_name(car_name)
    assert result == car_name


@pytest.mark.parametrize("car_name", [
    "", "a" * 64, "a" * 100  # Invalid names
])
def test_get_car_name_invalid(car_name):
    menu = Menu()
    with pytest.raises(AssertionError):
        menu.get_car_name(car_name)


@pytest.mark.parametrize("car_position_input, expected_position", [
    ("0 0 N", (0, 0, "N")),
    ("5 3 E", (5, 3, "E")),
    ("9 9 S", (9, 9, "S")),
    ("1 2 W", (1, 2, "W")),
    ("0 0 n", (0, 0, "N")),  # Case insensitive
    ("5 3 e", (5, 3, "E")),
    ("9 9 s", (9, 9, "S")),
    ("1 2 w", (1, 2, "W")),
])
def test_get_car_position_direction_valid(car_position_input, expected_position):
    menu = Menu()
    menu.set_field("10 10")
    result = menu.get_car_position_direction(car_position_input)
    assert result == expected_position


@pytest.mark.parametrize("car_position_input", [
    "0 0",          # Missing direction
    "0 0 N E",      # Too many values
    "-1 0 N",       # Negative x
    "0 -1 N",       # Negative y
    "10 0 N",       # x out of bounds
    "0 10 N",       # y out of bounds
    "0 0 X",        # Invalid direction
    "abc def N",    # Non-numeric coordinates
    "",             # Empty string
])
def test_get_car_position_direction_invalid(car_position_input):
    menu = Menu()
    menu.set_field("10 10")
    with pytest.raises(AssertionError):
        menu.get_car_position_direction(car_position_input)


@pytest.mark.parametrize("direction, expected", [
    ("N", "N"), ("E", "E"), ("S", "S"), ("W", "W"),
    ("n", "N"), ("e", "E"), ("s", "S"), ("w", "W"),  # Case insensitive
])
def test_get_car_direction_valid(direction, expected):
    menu = Menu()
    result = menu.get_car_direction(direction)
    assert result == expected


@pytest.mark.parametrize("direction", [
    "X", "North", "East", "South", "West", "1", "2", ""
])
def test_get_car_direction_invalid(direction):
    menu = Menu()
    with pytest.raises(AssertionError):
        menu.get_car_direction(direction)


@pytest.mark.parametrize("car_commands, expected", [
    ("F", "F"),
    ("LR", "LR"),
    ("FFRFFL", "FFRFFL"),
    ("f", "F"),     # Case insensitive
    ("lr", "LR"),
    ("FfRfFl", "FFRFFL"),
    ("F" * 127, "F" * 127),  # Maximum length
])
def test_get_car_commands_valid(car_commands, expected):
    menu = Menu()
    result = menu.get_car_commands(car_commands)
    assert result == expected


@pytest.mark.parametrize("car_commands", [
    "F" * 128,      # Too long
    "F" * 200,      # Way too long
    "B",            # Invalid command
    "FB",           # Invalid command
    "FLRB",         # Invalid command
    "",             # Empty string
])
def test_get_car_commands_invalid(car_commands):
    menu = Menu()
    with pytest.raises(AssertionError):
        menu.get_car_commands(car_commands)


def test_menu_initialization():
    menu = Menu()
    assert menu.simulator is not None
    assert menu.mode == -1
    assert len(menu.simulator.cars) == 0
    assert menu.simulator.field is None 