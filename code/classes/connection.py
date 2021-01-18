class Connection():

    def __init__(self, district, battery, house):
        self.district = district
        self.battery = battery
        self.house = house
        self.output =  self.house.output
        self.distance = (abs(self.battery.x_grid - self.house.x_grid) + abs(self.battery.y_grid - self.house.y_grid))
        self.connected = False


    def make_connection(self):
        self.connected = True


    def break_connection(self):
        self.connected = False


    def calc_penalty(self):
        """
        Calculates if the connection if the optimal connection for its 
        house or how much the difference with the optimal connection is
        """
        other_house_cons = self.district.get_house_connections(self)
        smallest_distance = self.distance
        for con in other_house_cons:
            if con.distance < smallest_distance:
                smallest_distance = con.distance
        penalty = self.distance - smallest_distance
        return penalty