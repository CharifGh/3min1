import random

def Random(district):
    """ Randomly connects houses and batteries """

    # begin met huizen ophalen
    # koppel huizen aan (Random batterijen)
    # hou voor elk batterij bij dat het niet meer is dan total input
    # als het meer is andere batterij koppelen

    batteries = district.get_batteries()
    random.shuffle(batteries)

    while district.unconnected_houses():
        unconnected_houses = district.unconnected_houses()
        for house in unconnected_houses:
            for battery in batteries:
                if battery.get_total_input() + house.output <= battery.capacity:
                    district.make_connections(battery, house)
                    house.connected = True
                    distance = (battery.x_grid - house.x_grid + (battery.y_grid - house.y_grid))
                    house.set_cable(abs(distance))
                    battery.set_total_input(house.output)
                    break
            if house.connected == False:
                for house in district.houses:
                    house.connected = False
                for battery in batteries:
                    battery.set_total_input(0)
                    battery.connected_houses = []    


           
    total_length = sum(house.get_cable() for house in district.houses)
    

    return total_length

