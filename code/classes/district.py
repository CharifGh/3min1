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
            all_batteries.pop(0)
            for battery in all_batteries:
                batteries.append(Battery(battery['x'], battery['y'], battery['capaciteit']))  
        return batteries

    # still returning address instead of info
    def load_houses(self, houses_file):
        """Load all batteries into district"""
        houses = []     
        with open(houses_file, "r") as f:
            reader = csv.DictReader(f)
            all_houses = list(reader)
            all_houses.pop(0)
            for house in all_houses:
                houses.append(House(house['x'], house['y'], house['maxoutput']))
        return houses 

    
    def unconnected_houses(self):
        """List of all unconnected houses"""
        unconnected_houses = [house for house in self.houses if house.connected == False] 
        return unconnected_houses


    def make_connections(self, battery, house):
        """Make connections between the battery and house instances"""
        battery.connected_houses.append(house)
        
    
    def house_connected(self, house):
        """Sets the connected value of a house to True"""
        house.connected = True    


    def get_batteries(self):
        return self.batteries
    

    def get_houses(self):
        return self.houses

    
    #Toegang  tot alle afstanden
