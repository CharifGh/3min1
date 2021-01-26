import random

def randomly_connect(district):
    """Makes random connections between houses and batteries but only if valid"""
    while district.unconnected_houses():
        all_connections = district.get_false_connections()
        random.shuffle(all_connections)
        for connection in all_connections:
            if not connection.house.get_status() and connection.output <= (connection.battery.capacity - connection.battery.get_total_input()):
                district.make_connection(connection)

        if district.unconnected_houses():
            district.add_retry()
            district.try_again()
        
    return district 