# autodrive

This Python CLI app allows the user to spawn cars in a user-defined field of dimensions x * y, then simulate the car's journey and see if they can reach their destinations without crashing.

## Features

- Field creation
- Supports multiple cars
- Define each car's actions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/leeyanhuilyh/autodrive
cd autodrive
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Application

```bash
python main.py
```

### Basic Workflow

1. **Set Field Size**: Enter the width and height of the simulation field (e.g., "10 10")
2. **Add Cars**: Choose option 1 to add cars to the field
   - Enter car name (1-63 characters)
   - Enter starting position and direction (e.g., "1 2 N")
   - Enter movement commands (e.g., "FFRFFFFRRL")
   - Repeat step 2 to add more cars
3. **Run Simulation**: Choose option 2 to start the simulation

### Input Format

- **Field Size**: `width height` (e.g., "10 10")
- **Car Position**: `x y direction` (e.g., "1 2 N")
  - `x`, `y`: Coordinates within field boundaries
  - `direction`: N (North), E (East), S (South), W (West)
- **Commands**: String of movement commands
  - `F`: Move forward
  - `L`: Turn left
  - `R`: Turn right

## Project Structure

```
autodrive/
├── main.py          # Main application entry point
├── src/             # Source code package
│   ├── __init__.py  # Package initialization
│   ├── car.py       # Car class with movement logic
│   ├── field.py     # Field/grid representation
│   ├── simulator.py # Simulation engine
│   ├── menu.py      # User interface and input handling
│   └── direction.py # Direction mapping constants
├── requirements.txt # Python dependencies
└── tests/           # Test suite
    ├── test_car.py
    ├── test_field.py
    ├── test_menu.py
    └── test_simulator.py
```

## Testing

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=.
```
