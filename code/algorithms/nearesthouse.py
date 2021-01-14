def nearestHouse(district):
    """ 
    Calculates the houses closest to a battery and connects them 
    until max capacity is reached, then moves to the next battery.
    Returns the total costs of the cables.
    """

    all_distances = []
    for battery in district.get_batteries():
        for house in district.get_houses():
            cable_length = (abs(battery.x_grid - house.x_grid) + abs(battery.y_grid - house.y_grid))
            all_distances.append({'distance': cable_length, 'house': house, 'battery': battery})
            
    all_distances.sort(key=lambda k: k['distance'])    

    
    for item in all_distances:
        house = item['house']
        battery = item['battery']
        if house.connected == False and (house.output + battery.get_total_input()) < battery.capacity:
            district.make_connection(battery, house)
            house.connected = True
            house.set_cable_length(battery)
            house.construct_cable(battery)

    return district        






    
