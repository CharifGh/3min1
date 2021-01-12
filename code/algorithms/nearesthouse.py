import random

def nearestHouse(district):
    """ 
    Calculates the houses closest to a battery and connects them 
    until max capacity is reached, then moves to the next battery.
    Returns the total costs of the cables.
    """

    batteries = district.get_batteries()
    houses = district.get_houses()
    
    for battery in batteries:
        unconnected_houses = district.unconnected_houses()

        if len(unconnected_houses) > 0:
            for house in unconnected_houses:
                distance = (abs(battery.x_grid - house.x_grid) + abs(battery.y_grid - house.y_grid - 1))
                house.set_cable(distance)
            
            unconnected_houses.sort(key=lambda k: k.get_cable())
            total_output = 0
            for house in unconnected_houses:
                if total_output + house.output <= battery.capacity:
                    district.house_connected(house) 
                    total_output = total_output + house.output
                    district.make_connections(battery, house)

                    # Needs simplification
                    house.construct_cable(battery.x_grid, battery.y_grid, house.x_grid, house.y_grid, house.cable)
                else:
                    break      
        else:
            break

    total_cables = sum(house.get_cable() for house in houses)
    costs = total_cables * 9

    return costs
