from car import Car
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