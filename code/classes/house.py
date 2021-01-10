# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


class House():
    """This class is used for house instances"""

    def __init__(self, x_grid, y_grid, output):
        self.x_grid= x_grid
        self.y_grid = y_grid
        self.output = output
        self.cable = 0
        self.connected = False


    def get_x(self):
        """Returns x-coordinate"""
        return int(self.x_grid)


    def get_y(self):
        """Returns y-coordinate"""
        return int(self.y_grid)  


    def get_output(self):
        """Returns output as a float"""
        return int(float(self.output))


    def get_cable(self):
        """Returns the length of the cable"""
        return int(self.cable) 


    def is_connected(self):
        """Returns a boolean value"""
        return self.connected


    def make_connection(self):
        """Sets the connected value to True"""
        self.connected = True    


    def set_cable(self, length_cable):
        self.cable = length_cable