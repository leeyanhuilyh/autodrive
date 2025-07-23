import numpy as np

class Field:

    def __init__(self, width: int, height: int):
        assert width > 0 and height > 0, "Width and height must be positive"
        self.width = width
        self.height = height
        self.field = np.zeros((height, width))