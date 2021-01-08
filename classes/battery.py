class Battery:
    """This class is used for battery instances"""

    def __init__(self, battery_id,x_grid, y_grid, battery_capacity):
        self.battery_id = battery_id
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.battery_capacity = battery_capacity