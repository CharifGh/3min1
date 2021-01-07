# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


class House:
    """This class is used for house instances"""

    def __init__(self, house_id, x_grid, y_grid, house_output):
        self.house_id = house_id
        self.x_grid= x_grid
        self.y_grid = y_grid
        self.house_output = house_output


class Battery:
    """This class is used for battery instances"""

    def __init__(self, battery_id,x_grid, y_grid, battery_capacity):
        self.battery_id = battery_id
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.battery_capacity = battery_capacity


class Cable:
    """This class is used for cable instances to connect houses and batteries"""

    def __init__(self, cable_id, size, connection):
        self.cable_id = cable_id
        self.size = size
        self.connection = {}

    def add_connection(self, battery, house):
        self.connection[battery] = house

