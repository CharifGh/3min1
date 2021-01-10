# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


class Battery():
    """This class is used for battery instances"""

    def __init__(self, x_grid, y_grid, capacity):
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.capacity = capacity
        self.houses = []


    def get_x(self):
        """Returns x-coordinate"""
        return int(self.x_grid)
        

    def get_y(self):
        """Returns y-coordinate"""
        return int(self.y_grid)


    def get_capacity(self):
        """Returns the capacity as a float"""
        return int(float(self.capacity))    