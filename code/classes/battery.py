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


    def add_house(self, house): 
        self.connected_houses.append(house)


    def remove_house(self, house):
        self.connected_houses.remove(house)


    def remove_all_houses(self):
        self.connected_houses = []    


    def get_total_input(self):
        """Returns total input the battery receives from the connected houses"""
        total_input = sum(house.output for house in self.connected_houses)
        return total_input


    def get_free_capacity(self, output):
        free_capacity = self.capacity - (self.get_total_input() - output)
        return free_capacity


    def __repr__(self):
        return self.location        