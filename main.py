import numpy as np
from car import Car
from menu import Menu
from field import Field
from simulator import Simulator

def main():
    menu = Menu()
    print("Welcome to Auto Driving Car Simulation!")
    print()
    field_size = input("Please enter the width and height of the simulation field in x y format: ")
    if field_size == 'd1':
        print("Debug case 1")
        field_size = "10 10"
        menu.set_field(field_size)
        menu.add_car("A", (1, 2, "N"), "FFRFFFFRRL")
    elif field_size == 'd2':
        print("Debug case 2")
        field_size = "10 10"
        menu.set_field(field_size)
        menu.add_car("A", (1, 2, "N"), "FFRFFFFRRL")
        menu.add_car("B", (7, 8, "W"), "FFLFFFFFFF")
    elif field_size == 'd3':
        print("Debug case 3")
        field_size = "10 10"
        menu.set_field(field_size)
        menu.add_car("A", (1, 2, "N"), "FFRFFFFRRL")
        menu.add_car("B", (7, 8, "W"), "FFLFFFFFFF")
        menu.add_car("C", (5, 5, "N"), "RRFF")
    else:
        menu.set_field(field_size)
        while menu.mode != "2":
            mode = input("""\
Please choose from the following options: 
[1] Add a car to field
[2] Run simulation
""")
            menu.set_mode(mode)
            if menu.mode == "1":
                car_name = input("Please enter the name of the car: ")
                menu.get_car_name(car_name)
                car_position = input(f"Please enter the position of the car {car_name} in x y Direction format: ")
                car_position = menu.get_car_position_direction(car_position)

                car_commands = input(f"Please enter the commands for the car {car_name}: ")
                car_commands = menu.get_car_commands(car_commands)

                print("Your current list of cars are:")
                menu.add_car(car_name, car_position, car_commands)
 
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
    simulator = menu.simulator
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