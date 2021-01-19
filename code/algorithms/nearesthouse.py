from operator import attrgetter
import random

def nearestHouse(district):
    """ 
    Calculates the houses closest to a battery and connects them 
    until max capacity is reached, then moves to the next battery.
    Returns the total costs of the cables.
    """
    while district.unconnected_houses():
        all_houses = district.get_houses()
        all_houses.sort(key=attrgetter('output'), reverse=True)

        i=0 
        for i in range(40):
            house = all_houses[i]
            house_connections = [con for con in district.get_false_connections() if con.house == house]
            house_connections.sort(key=attrgetter('distance')) 
            best_connection = house_connections[0]
            if not best_connection.house.get_status() and best_connection.output <= (best_connection.battery.capacity - best_connection.battery.get_total_input()):
                district.make_connection(best_connection)
            i = i+1

        all_connections = district.get_false_connections()
        random.shuffle(all_connections)
        for connection in all_connections:
            if not connection.house.get_status() and connection.output <= (connection.battery.capacity - connection.battery.get_total_input()):
                district.make_connection(connection)
        if district.unconnected_houses():
            district.try_again()

        if district.check_validity():
            return district      






    
