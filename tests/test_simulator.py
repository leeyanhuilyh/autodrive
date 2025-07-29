import pytest
from simulator import Simulator
from car import Car
from field import Field


def test_simulator_initialization():
    simulator = Simulator()
    assert simulator.field is None
    assert simulator.cars == []
    assert simulator.car_print == ""
    assert simulator.end_print == ""
    assert simulator.end_state == {}
    assert simulator.direction_map == {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0)
    }


def test_simulator_initialization_with_parameters():
    field = Field(10, 10)
    car = Car("A", 1, 2, "N")
    cars = [car]

    simulator = Simulator(field, cars)
    assert simulator.field == field
    assert simulator.cars == cars
    assert len(simulator.cars) == 1


def test_set_field():
    simulator = Simulator()
    field = Field(5, 3)
    simulator.set_field(field)
    assert simulator.field == field
    assert simulator.field.width == 5
    assert simulator.field.height == 3


@pytest.mark.parametrize(
    "cars_to_add, expected_car_prints",
    [
        (
            [("A", 1, 2, "N", "FFR")],
            ["- A, (1, 2) N, FFR\n"]
        ),
        (
            [("A", 1, 2, "N", "FFR"), ("B", 3, 4, "E", "LFF")],
            ["- A, (1, 2) N, FFR\n", "- B, (3, 4) E, LFF\n"]
        ),
    ]
)
def test_add_cars(cars_to_add, expected_car_prints):
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    cars = []
    for name, x, y, direction, commands in cars_to_add:
        car = Car(name, x, y, direction)
        car.add_command(commands)
        simulator.add_car(car)
        cars.append(car)

    assert len(simulator.cars) == len(cars)
    for i, car in enumerate(cars):
        assert simulator.cars[i] == car
    for expected_print in expected_car_prints:
        assert expected_print in simulator.car_print


@pytest.mark.parametrize("direction, expected_dx, expected_dy", [
    ("N", 0, 1),
    ("E", 1, 0),
    ("S", 0, -1),
    ("W", -1, 0),
])
def test_direction_map(direction, expected_dx, expected_dy):
    simulator = Simulator()
    dx, dy = simulator.direction_map[direction]
    assert dx == expected_dx
    assert dy == expected_dy


@pytest.mark.parametrize("start_x, start_y, direction, command, expected_x, expected_y", [
    (5, 5, "N", "F", 5, 6),  # Move North
    (5, 5, "E", "F", 6, 5),  # Move East
    (5, 5, "S", "F", 5, 4),  # Move South
    (5, 5, "W", "F", 4, 5),  # Move West
    (0, 0, "N", "F", 0, 1),  # From edge
    (9, 9, "S", "F", 9, 8),  # From edge
])
def test_forward_movement_valid(start_x, start_y, direction, command, expected_x, expected_y):
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    car = Car("A", start_x, start_y, direction)
    car.add_command(command)

    simulator.forward(car)
    assert car.x == expected_x
    assert car.y == expected_y
    assert len(car.commands) == 0


@pytest.mark.parametrize("start_x, start_y, direction", [
    (0, 0, "W"),   # Try to move West from left edge
    (0, 0, "S"),   # Try to move South from bottom edge
    (9, 9, "E"),   # Try to move East from right edge
    (9, 9, "N"),   # Try to move North from top edge
])
def test_forward_movement_wall_collision(start_x, start_y, direction):
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    car = Car("A", start_x, start_y, direction)
    car.add_command("F")

    simulator.forward(car)
    assert car.x == start_x  # Position unchanged
    assert car.y == start_y
    assert len(car.commands) == 0


@pytest.mark.parametrize("start_direction, turn_command, expected_direction", [
    ("N", "L", "W"),
    ("N", "R", "E"),
    ("E", "L", "N"),
    ("E", "R", "S"),
    ("S", "L", "E"),
    ("S", "R", "W"),
    ("W", "L", "S"),
    ("W", "R", "N"),
])
def test_turn_commands(start_direction, turn_command, expected_direction):
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    car = Car("A", 5, 5, start_direction)
    car.add_command(turn_command)

    simulator.forward(car)
    assert car.direction == expected_direction
    assert car.x == 5  # Position unchanged
    assert car.y == 5
    assert len(car.commands) == 0


def test_run_simulation_single_car():
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    car = Car("A", 1, 2, "N")
    car.add_command("FFR")
    simulator.add_car(car)

    simulator.run_simulation()

    assert len(simulator.cars) == 0  # All cars finished
    assert "A, (1, 4) E" in simulator.end_print


def test_run_simulation_car_collision():
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    # Car A moves East to (2, 1)
    car_a = Car("A", 1, 1, "E")
    car_a.add_command("F")
    simulator.add_car(car_a)

    # Car B moves South to (2, 1) - collision!
    car_b = Car("B", 2, 2, "S")
    car_b.add_command("F")
    simulator.add_car(car_b)

    simulator.run_simulation()

    assert len(simulator.cars) == 0  # Both cars removed due to collision
    assert "A, collides with B at (2, 1)" in simulator.end_print
    assert "B, collides with A at (2, 1)" in simulator.end_print


def test_run_simulation_multiple_cars_no_collision():
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    # Car A moves to (2, 1)
    car_a = Car("A", 1, 1, "E")
    car_a.add_command("F")
    simulator.add_car(car_a)

    # Car B moves to (1, 2) - no collision
    car_b = Car("B", 1, 1, "N")
    car_b.add_command("F")
    simulator.add_car(car_b)

    simulator.run_simulation()

    assert len(simulator.cars) == 0  # Both cars finished
    assert "A, (2, 1) E" in simulator.end_print
    assert "B, (1, 2) N" in simulator.end_print


def test_run_simulation_car_finishes_early():
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    # Car A finishes in 2 steps
    car_a = Car("A", 1, 1, "E")
    car_a.add_command("FF")
    simulator.add_car(car_a)

    # Car B takes longer
    car_b = Car("B", 1, 1, "N")
    car_b.add_command("FFFF")
    simulator.add_car(car_b)

    simulator.run_simulation()

    assert len(simulator.cars) == 0  # All cars finished
    assert "A, (3, 1) E" in simulator.end_print
    assert "B, (1, 5) N" in simulator.end_print


def test_run_simulation_empty_cars():
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    simulator.run_simulation()

    assert len(simulator.cars) == 0
    assert simulator.end_print == ""


def test_car_print_format():
    simulator = Simulator()
    field = Field(10, 10)
    simulator.set_field(field)

    car = Car("TestCar", 5, 3, "S")
    car.add_command("FFRLL")
    simulator.add_car(car)

    expected_format = "- TestCar, (5, 3) S, FFRLL\n"
    assert simulator.car_print == expected_format
