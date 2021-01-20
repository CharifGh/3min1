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
        self.connected = False
        self.cable_points = []


    def get_status(self):
        """Returns True if house is connected and False if not"""
        return self.connected


    def set_connection(self):
        """Sets connected status to True"""
        self.connected = True


    def break_connection(self):
        """Sets connected status to False"""
        self.connected = False        


    def construct_cable(self, bx, by, distance):
        """Calculates the x,y-intersections the cable crosses"""
        # Needs simplification
        cx = 0
        cy = 0
        hx = self.x_grid
        hy = self.y_grid
        self.cable_points.append(f"{hx},{hy}")
        for i in range(distance):
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