from menu import Menu


def main():
    menu = Menu()
    print("Welcome to Auto Driving Car Simulation!")
    print()
    field_size = input("Please enter the width and height of the simulation field in x y format: ")
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
