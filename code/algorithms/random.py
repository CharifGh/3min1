def Random(district):
    """ Randomly connects houses and batteries """

    batteries = district.get_batteries()
    houses = district.get_houses()

    total_cables = sum(house.get_cable() for house in houses)
    costs = total_cables * 9

    for battery in batteries:
        unconnected_houses = district.unconnected_houses()

        if len(unconnected_houses) > 0:
            for house in unconnected_houses:
                distance = (battery.get_x() - house.get_x()) + (battery.get_y() - house.get_y())
                house.set_cable(abs(distance))
            
            unconnected_houses.sort(key=lambda k: k.get_cable())
            total_output = 0
            for house in unconnected_houses:   
                district.house_connected(house) 
                total_output = total_output + house.get_output()
                district.make_connections(battery, house)

                house.construct_cable(battery.get_x(), battery.get_y(), house.get_x(), house.get_y(), house.cable)
            else:
                break      
        else:
            break

    total_cables = sum(house.get_cable() for house in houses)
    costs = total_cables * 9

    return costs