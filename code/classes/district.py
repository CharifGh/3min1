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

    # still returns address instead of info
    def load_batteries(self, batteries_file):
        """load all batteries into district"""   
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
        """load all batteries into district"""
        houses = []     
        with open(houses_file, "r") as f:
            reader = csv.DictReader(f)
            all_houses = list(reader)
            all_houses.pop(0)
            for house in all_houses:
                houses.append(House(house['x'], house['y'], house['maxoutput']))
        return houses 


# first try was with dictionary using csv.DictReader.