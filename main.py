import numpy as np
from car import Car
from menu import Menu

def main():
    print("Welcome to Auto Driving Car Simulation!")
    print()
    field_size = input("Please enter the width and height of the simulation field in x y format: ")
    assert len(field_size.split()) == 2, "Field size must be in x y format"
    field_size = field_size.split()
    assert int(field_size[0]) > 0, "Width must be positive"
    assert int(field_size[1]) > 0, "Height must be positive"
    width, height = int(field_size[0]), int(field_size[1])
    
    print(f"You have created a field of {width} x {height}.")
    print()

    mode = -1
    menu = Menu()
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
            menu.add_car(car)
            print(menu.car_print)
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


# create field of w x h (width is column, height is row)

# Add car with name, position, direction
# make a class for car

# Run simulation
# 1) at each step, advance all cars by 1 command
# 2) if there is a collision, both cars collide at THAT square

if __name__ == "__main__":
    main()