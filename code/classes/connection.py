from operator import attrgetter


class Connection():

    def __init__(self, district, battery, house):
        self.district = district
        self.battery = battery
        self.house = house
        self.output =  self.house.output
        self.distance = (abs(self.battery.x_grid - self.house.x_grid) + abs(self.battery.y_grid - self.house.y_grid))
        self.connected = False
        self.penalty = 0
        self.x_best = 0


    def make_connection(self):
        self.connected = True


    def break_connection(self):
        self.connected = False


    def calc_rating(self):
        """
        Calculates if the connection is an optimal connection for its house 
        and if it isn't how much the difference with the first better connection is
        """
        house_cons = self.district.get_house_connections(self.house)
        house_cons.sort(key=attrgetter('distance', 'output'))
        self.x_best = house_cons.index(self) + 1
        if self.x_best != 1:
            better_connection = house_cons[self.x_best - 2]
            self.penalty = self.distance - better_connection.distance


    def battery_available(self):
        if (self.battery.get_total_input() + self.output) <= self.battery.capacity:
            return True
        return False    

