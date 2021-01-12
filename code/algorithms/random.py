import random

def Random(district):
    """ Randomly connects houses and batteries """

    # begin met huizen ophalen
    # koppel huizen aan (Random batterijen)
    # hou voor elk batterij bij dat het niet meer is dan total input
    # als het meer is andere batterij koppelen

    
    houses = district.get_houses()

    for house in houses:
        batteries = district.get_batteries()
        random.choice(batteries)
        for battery in batteries:
            if battery.capacity < house.output and house.connected == False:
                   district.make_connections(house, battery)
                   house.house_connected(house)
                   battery.set_total_input(house)
                   
            else:
                 random.choice(batteries)

            if len(houses) > 0:
                for house in houses:
                    distance = (battery.x_grid - house.x_grid + (battery.y_grid - house.y_grid))
                    house.set_cable(abs(distance))
                    
                    house.construct_cable(battery.x_grid, battery.y_grid, house.x_grid, house.y_grid, house.cable)

    total_cables = sum(house.get_cable() for house in houses)
    costs = total_cables * 9

    return costs