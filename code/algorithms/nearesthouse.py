def nearestHouse(district):
    """ 
    Calculates the houses closest to a battery and connects them 
    until max capacity is reached, then moves to the next battery.
    Returns the total costs of the cables.
    """

    batteries = district.get_batteries()
    
    for battery in batteries:
        unconnected_houses = district.unconnected_houses()

        for house in unconnected_houses:
            house.set_cable_length(battery)
        
        unconnected_houses.sort(key=lambda k: k.get_cable_length())
        for house in unconnected_houses:
            if battery.get_total_input() + house.output <= battery.capacity:
                house.connected = True 
                district.make_connection(battery, house)
                house.construct_cable(battery)
            else:
                break      


    return district
