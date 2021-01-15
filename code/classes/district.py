# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


# loads houses and batteries 

#output = return batteries and houses

from .battery import Battery
from .house import House

import csv, json

class District():
    def __init__(self, batteries_file, houses_file):
        self.batteries = self.load_batteries(batteries_file)
        self.houses = self.load_houses(houses_file)
        self.retries = 0

    def load_batteries(self, batteries_file):
        """Load all batteries into district"""   
        batteries = []     
        with open(batteries_file, "r") as in_file:
            reader = csv.DictReader(in_file)
            all_batteries = list(reader)
            for battery in all_batteries:
                batteries.append(Battery(battery['x'], battery['y'], battery['capaciteit']))  
        return batteries


    def load_houses(self, houses_file):
        """Load all batteries into district"""
        houses = []     
        with open(houses_file, "r") as f:
            reader = csv.DictReader(f)
            all_houses = list(reader)
            for house in all_houses:
                houses.append(House(house['x'], house['y'], house['maxoutput']))
        return houses 

    
    def get_batteries(self):
        """Returns all the batteries"""
        return self.batteries


    def get_houses(self):
        """Returns all the houses"""
        return self.houses    
    
    
    def unconnected_houses(self):
        """List of all unconnected houses"""
        unconnected_houses = [house for house in self.houses if house.connected == False] 
        return unconnected_houses


    def make_connection(self, battery, house):
        """Make connections between the battery and house instances"""
        battery.connected_houses.append(house)
        

    def check_validity(self):
        """Checks if solution is valid"""
        for house in self.houses:
            if house.connected == False:
                return False
        return True        


    def calc_costs(self):
        """Returns the total length of all cables"""
        total_cable_length = sum(house.get_cable_length() for house in self.houses)    
        return total_cable_length


    def add_retry(self):
        self.retries = self.retries +1


    def try_again(self):
        """Resets values to default"""
        for house in self.get_houses():
            house.connected = False
            house.cable_points = []
            house.reset_cable_length()
        for battery in self.get_batteries():
            battery.connected_houses = []    

            
    def get_all_distances(self):
        """Calculates all distances between batteries and houses, returns a list of dicts"""
        all_distances = []
        for battery in self.get_batteries():
            for house in self.get_houses():
                cable_length = (abs(battery.x_grid - house.x_grid) + abs(battery.y_grid - house.y_grid))
                all_distances.append({'distance': cable_length, 'house': house, 'output': house.output, 'battery': battery})
                  
        return all_distances


    def get_output(self):
        """Get all necessary data and puts it in a json file"""
        all_data = []
        costs_own = 0
        costs_own = self.calc_costs()*9  
        for battery in self.get_batteries():
            costs_own = costs_own+5000
        all_data.append({'district': 1, 'costs-own': costs_own})
        for battery in self.get_batteries():
            houses = [] 
            for house in battery.connected_houses:
                houses.append({'location': house.location, 'output': house.output, 'cables': house.cable_points})
            all_data.append({'location': battery.location, 'capacity': battery.capacity, 'houses': houses})

        out_file = open('output.json', 'w')
        json.dump(all_data, out_file)

        out_file.close()   