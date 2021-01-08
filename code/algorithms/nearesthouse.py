

class NearestHouse:
    """ 
    Calculates the houses closest to a battery and connects them 
    until max capacity is reached, then moves to the next battery
    """

    def __init__(self, houses, batteries):
        pass


    def get_next_battery():
        pass


    def get_unconnected_houses():
        pass


    def calc_distance(battery, houses):
        """
        Calculates the distance from one battery to all unconnected houses
        """
        unconnected_houses = []

        for house in houses:
            distance = (battery.x-grid - house.x-grid) + (battery.y-grid - house.y-grid)
            house_data = {'distance': distance, 'output': house.house_output, 'id': house.house_id}
            unconnected_houses.append(house_data)

        connect_battery(unconnected_houses)


    def connect_battery(unconnected_houses):
        """
        Connects the battery to the nearest unconnected houses until max 
        capacity is reached
        """
        nearest_houses = sorted(unconnected_houses, key=lambda k: k['distance'])

        connections = []
        total_output = 0
        while total_output <= battery.battery_capacity:
            for house in nearest_houses:
                connections.append(house.house_id)
                total_output = total_output + house.house_output



