import numpy as np
from car import Car
from menu import Menu
from field import Field
from simulator import Simulator

def main():
    simulator = Simulator()
    print("Welcome to Auto Driving Car Simulation!")
    print()
    field_size = input("Please enter the width and height of the simulation field in x y format: ")
    if field_size == 'd1':
        print("Debug case 1")
        field = Field(10, 10)
        simulator.set_field(field)
        car = Car("A", 1, 2, "N")
        car.add_command("FFRFFFFRRL")
        simulator.add_car(car)
    elif field_size == 'd2':
        print("Debug case 2")
        field = Field(10, 10)
        simulator.set_field(field)
        car = Car("A", 1, 2, "N")
        car.add_command("FFRFFFFRRL")
        simulator.add_car(car)
        car = Car("B", 7, 8, "W")
        car.add_command("FFLFFFFFFF")
        simulator.add_car(car)
    elif field_size == 'd3':
        print("Debug case 3")
        field = Field(10, 10)
        simulator.set_field(field)
        car = Car("A", 1, 2, "N")
        car.add_command("FFRFFFFRRL")
        simulator.add_car(car)
        car = Car("B", 7, 8, "W")
        car.add_command("FFLFFFFFFF")
        simulator.add_car(car)
        car = Car("C", 5, 5, "N")
        car.add_command("RRFF")
        simulator.add_car(car)
    else:
        assert len(field_size.split()) == 2, "Field size must be in x y format"
        field_size = field_size.split()
        assert int(field_size[0]) > 0, "Width must be positive"
        assert int(field_size[1]) > 0, "Height must be positive"
        width, height = int(field_size[0]), int(field_size[1])

        # create field of w x h (width is column, height is row)
        field = Field(width, height)
        simulator.set_field(field)
        print(f"You have created a field of {width} x {height}.")
        print()

        mode = -1
        while mode != "2":
            mode = input("""\
Please choose from the following options: 
[1] Add a car to field
[2] Run simulation
""")
            assert mode in ["1", "2"], "Invalid mode"
            if mode == "1":
                car_name = input("Please enter the name of the car: ")
                assert 0 < len(car_name) < 64, "Car name must be non-empty and less than 64 characters"
                car_position = input(f"Please enter the position of the car {car_name} in x y Direction format: ")
                assert len(car_position.split()) == 3, "Car position must be in x y Direction format"
                car_position = car_position.split()
                assert int(car_position[0]) >= 0 and int(car_position[0]) < width, "Car position must be within the field"
                assert int(car_position[1]) >= 0 and int(car_position[1]) < height, "Car position must be within the field"
                assert car_position[2].upper() in ["N", "E", "S", "W"], "Invalid direction. Must be N, E, S, or W (case insensitive)."
                car_direction = car_position[2].upper()
                car_position = (int(car_position[0]), int(car_position[1]))
                car_commands = input(f"Please enter the commands for the car {car_name}: ")
                assert len(car_commands) < 128, "Car commands must be less than 128 characters"
                car_commands = car_commands.upper()
                assert all(command in ["F", "L", "R"] for command in car_commands), "Invalid command. Must be f, b, l, or r (case insensitive)."
                print("Your current list of cars are:")
                car = Car(car_name, car_position[0], car_position[1], car_direction)
                car.add_command(car_commands)
                simulator.add_car(car)
                print(simulator.car_print)
                print()
 
    # Reading inputs
    # 1) name of car
    # 2) x pos, y pos, direction (only n, e, s, w)
    # 3) enter commands for car
    #   3a) eg. FFRFFFFRRL
    #   This means car A will move forward twice, turn right, move forward four times, turn right twice, and turn left once.
    # 4) print out current list of cars with name, position, direction, commands
    #   4a) eg. - A, (1,2) N, FFRFFFFRRL
    # 5) Give user choice to add 1 more car, or run simulation

    # Run simulation
    # 1) at each step, advance all cars by 1 command
    step = 1
    while len(simulator.cars):
        curr_positions = {}
        to_remove = []
        print(f"Step {step}")
        for i, car in enumerate(simulator.cars):
            if not len(car.commands): # car successfully reached destination
                # simulator.end_state[(car.x, car.y)] = (car.name, None, 0, car.direction, step)
                simulator.end_print += f"{car.name}, ({car.x}, {car.y}) {car.direction}\n"
                to_remove.append(i)
                continue
            simulator.forward(car)
            print(f"Car {car.name} at ({car.x}, {car.y}) {car.direction}")
            if (car.x, car.y) in curr_positions: # car crash
                # print(f"Car {car.name} collided with car {curr_positions[car.x, car.y]}")
                # simulator.end_state[(car.x, car.y)] = (car.name, simulator.cars[curr_positions[car.x, car.y]].name, 1, None, step)
                simulator.end_print += f"{simulator.cars[curr_positions[car.x, car.y]].name}, collides with {car.name} at ({car.x}, {car.y}) at step {step}\n"
                simulator.end_print += f"{car.name}, collides with {simulator.cars[curr_positions[car.x, car.y]].name} at ({car.x}, {car.y}) at step {step}\n"
                to_remove.append(i)
                to_remove.append(curr_positions[car.x, car.y])
            else:
                curr_positions[(car.x, car.y)] = i
        # remove cars in to_remove
        for i in to_remove:
            simulator.cars.pop(i)            
        step += 1

    # print(simulator.end_state)
    print(simulator.end_print)
    # 2) if there is a collision, both cars collide at THAT square

if __name__ == "__main__":
    main()