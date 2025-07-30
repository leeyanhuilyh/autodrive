from src.car import Car
import pytest


@pytest.mark.parametrize("name, x, y, direction", [
    ("A", 1, 2, "N"),
    ("Bbb", 3, 4, "e"),
    ("cC", 5, 6, "S"),
])
def test_car_creation(name, x, y, direction):
    car = Car(name, x, y, direction)
    assert car.name == name
    assert car.x == x
    assert car.y == y
    assert car.direction == direction
    assert car.commands is None


@pytest.mark.parametrize("name, x, y, direction", [
    ("A", -1, 0, "n"),
    ("B", 3, 4, "North"),
])
def test_invalid_car_creation(name, x, y, direction):
    with pytest.raises(AssertionError):
        Car(name, x, y, direction)


@pytest.mark.parametrize(
    "start_direction, turns, expected_directions",
    [
        ("N", ["L"], ["W"]),
        ("E", ["L", "L"], ["N", "W"]),
        ("S", ["R", "R"], ["W", "N"]),
        ("W", ["L", "R", "R"], ["S", "W", "N"]),
    ]
)
def test_car_turn(start_direction, turns, expected_directions):
    car = Car("A", 0, 0, start_direction)
    for turn, expected in zip(turns, expected_directions):
        car.turn(turn)
        assert car.direction == expected
