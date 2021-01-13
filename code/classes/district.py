# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


# loads houses and batteries 

#output = return batteries and houses

from .battery import Battery
from .house import House

import csv

class District():
    def __init__(self, batteries_file, houses_file):
        self.batteries = self.load_batteries(batteries_file)
        self.houses = self.load_houses(houses_file)

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