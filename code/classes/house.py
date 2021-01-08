# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


class House():
    """This class is used for house instances"""

    def __init__(self, x_grid, y_grid, house_output):
        self.x_grid= x_grid
        self.y_grid = y_grid
        self.house_output = house_output
        self.cable = []
    


