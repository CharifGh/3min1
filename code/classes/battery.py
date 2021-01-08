# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


class Battery():
    """This class is used for battery instances"""

    def __init__(self, x_grid, y_grid, battery_capacity):
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.battery_capacity = battery_capacity