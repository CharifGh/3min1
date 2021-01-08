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
        batteries = {}
        with open (batteries_file, "r") as in_file:
            reader=csv.DictReader(in_file)
            for row in reader:
                print(row)
        return batteries


    def load_houses(self, houses_file):
        """load all batteries into district"""
        houses = {}
        with open (houses_file, "r") as f:
            houses_reader=csv.DictReader(f)
            for row in houses_reader:
                print(row)
        return houses
