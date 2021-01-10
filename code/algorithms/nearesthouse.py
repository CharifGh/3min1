def nearestHouse(district):
    """ 
    Calculates the houses closest to a battery and connects them 
    until max capacity is reached, then moves to the next battery
    """
    batteries = district[0:4]
    houses = district[5:]

    for battery in batteries:
        unconnected_houses = []
        for house in houses:
            if house.connected == False:
                unconnected_houses.append(house)
        
        if len(unconnected_houses) > 0:
            for house in unconnected_houses:
                distance = (battery.x - house.x) + (battery.y - house.y)
                # Hier coördinaten van de cable ipv alleen distance
                house.cable = abs(distance)
            
            unconnected_houses.sort(key=lambda k: k.get('cable'))
            total_output = 0
            for house in unconnected_houses:
                if total_output + house.maxoutput <= battery.capaciteit:
                    house.connected = True
                    total_output = total_output + house.maxoutput
                else:
                    break      
        else:
            break

    total_cables = sum(house['cable'] for house in houses)
    costs = total_cables * 9

    return costs



