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
        """load all batteries into district"""
        with open (batteries_file, "r") as in_file:
            next(in_file)
            reader = csv.reader(in_file)
            batteries = [row for row in reader]
            battery_instance = Battery(batteries[0], batteries[1], batteries[2]) 
        return battery_instance


    def load_houses(self, houses_file):
        """load all batteries into district"""
        with open (houses_file, "r") as f:
            next(f)
            houses_reader = csv.reader(f)
            houses = [row for row in houses_reader]
            house_instance = House(houses[0], houses[1], houses[2]) 
        return house_instance
