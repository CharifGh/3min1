import random

def nearestHouse(district):
    """ 
    Calculates the houses closest to a battery and connects them 
    until max capacity is reached, then moves to the next battery.
    Returns the total costs of the cables.
    """

    batteries = district.get_batteries()
    houses = district.get_houses()
    
    random.shuffle(batteries)
    for battery in batteries:
        unconnected_houses = district.unconnected_houses()

        if len(unconnected_houses) > 0:
            for house in unconnected_houses:
                distance = (battery.get_x() - house.get_x()) + (battery.get_y() - house.get_y())
                house.set_cable(abs(distance))
            
            unconnected_houses.sort(key=lambda k: k.get_cable())
            total_output = 0
            for house in unconnected_houses:
                if total_output + house.get_output() <= battery.get_capacity():
                    district.house_connected(house) 
                    total_output = total_output + house.get_output()
                    district.make_connections(battery, house)
                else:
                    break      
        else:
            break

    total_cables = sum(house.get_cable() for house in houses)
    costs = total_cables * 9

    return costs
