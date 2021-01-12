# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


class House():
    """This class is used for house instances"""

    def __init__(self, x_grid, y_grid, output):
        self.x_grid= int(x_grid)
        self.y_grid = int(y_grid)
        self.output = float(output)
        self.cable = 0
        self.connected = False
        self.location =  f"{self.x_grid},{self.y_grid}"
        self.cable_points = []

   
    def get_cable(self):
        """Returns the length of the cable"""
        return int(self.cable) 


    def set_cable(self, length_cable):
        """Saves length of cable"""
        self.cable = length_cable


    def construct_cable(self, bat_x, bat_y, house_x, house_y, distance):
        """Calculates the x,y-intersections the cable crosses"""
        # Needs simplification
        cx = 0
        cy = 0
        bx = bat_x
        by = bat_y
        hx = house_x
        hy = house_y
        self.cable_points.append(f"{hx},{hy}")
        for i in range(distance):
            if bx > hx:
                cx = hx+1
                hx = hx+1
            if bx < hx:
                cx = hx-1
                hx = hx-1
            if bx == hx:
                cx = hx
            if by > hy:
                cy = hy+1
                hy = hy+1
            if by < hy:
                cy = hy-1
                hy = hy-1
            if by == hy:
                cy = hy
            self.cable_points.append(f"{cx},{cy}") 
            i = i+1


    def __repr__(self):
        return self.location    