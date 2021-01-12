import random

def Random(district):
    """ Randomly connects houses and batteries """

    # begin met huizen ophalen
    # koppel huizen aan (Random batterijen)
    # hou voor elk batterij bij dat het niet meer is dan total input
    # als het meer is andere batterij koppelen

    batteries = district.get_batteries()
    

    while len(district.unconnected_houses()) > 1:
        unconnected_houses = district.unconnected_houses()
        for house in unconnected_houses:
            battery = random.choice(batteries)
            if battery.get_total_input() + house.output <= battery.capacity:
                district.make_connections(battery, house)
                district.house_connected(house)
                distance = (battery.x_grid - house.x_grid + (battery.y_grid - house.y_grid))
                house.set_cable(abs(distance))
                battery.set_total_input(house.output)
                house.construct_cable(battery.y_grid, battery.y_grid, house.x_grid, house.y_grid, house.cable)   

           
    total_cables = sum(house.get_cable() for house in district.houses)
    costs = total_cables * 9

    return costs