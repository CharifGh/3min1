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
        self.location =  f"{self.x_grid},{self.y_grid}"
        self.output = float(output)
        self.cable_length = 0
        self.connected = False
        self.cable_points = []

   
    def get_cable_length(self):
        """Returns the length of the cable"""
        return self.cable_length


    def set_cable_length(self, battery):
        """Saves length of cable"""
        self.cable_length = (abs(battery.x_grid - self.x_grid) + abs(battery.y_grid - self.y_grid))


    def reset_cable_length(self):
        """Sets cable_length back to 0"""
        self.cable_length = 0    


    def construct_cable(self, battery):
        """Calculates the x,y-intersections the cable crosses"""
        # Needs simplification
        cx = 0
        cy = 0
        bx = battery.x_grid
        by = battery.y_grid
        hx = self.x_grid
        hy = self.y_grid
        self.cable_points.append(f"{hx},{hy}")
        for i in range(self.cable_length):
            if bx > hx:
                cx = hx+1
                hx = hx+1
                cy = hy
            elif bx < hx:
                cx = hx-1
                hx = hx-1
                cy = hy
            elif bx == hx:
                cx = hx
                if by > hy:
                    cy = hy+1
                    hy = hy+1
                elif by < hy:
                    cy = hy-1
                    hy = hy-1
                elif cy == hy:
                    cy = hy       
            self.cable_points.append(f"{cx},{cy}") 
            i = i+1


    def __repr__(self):
        return self.location    