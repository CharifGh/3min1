import random


def get_next_house(district):
    return random.choice(district.unconnected_houses())


def get_all_batteries(district):
    batteries = district.get_batteries()
    random.shuffle(batteries)
    return batteries
        
            
def randomly_connect(district):
    while district.unconnected_houses():
        house = get_next_house(district)
        for battery in get_all_batteries(district):
            if battery.get_total_input() + house.output <= battery.capacity:
                district.make_connection(battery, house)
                house.connected = True
                house.set_cable_length(battery)
                house.construct_cable(battery)
                break
        if house.connected == False:
            district.add_retry()
            district.try_again()
    return district        
   

