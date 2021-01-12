# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


class Battery():
    """This class is used for battery instances"""

    def __init__(self, x_grid, y_grid, capacity):
        self.x_grid = int(x_grid)
        self.y_grid = int(y_grid)
        self.capacity = float(capacity)
        self.location = f"{self.x_grid},{self.y_grid}"
        self.connected_houses = []
        self.total_input = 0


    def get_total_input(self):
        return self.total_input

    def set_total_input(self, house):
        self.total_input = self.total_input + house 




    def __repr__(self):
        return self.location        