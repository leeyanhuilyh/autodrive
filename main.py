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

    # Run simulation
    menu.simulator.run_simulation()

if __name__ == "__main__":
    main()