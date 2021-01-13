# ****************************************
# Main.py                                *
# Paulien Tideman en Charif Ghammane     *
# Implementation of Smart Grid functions *
# ****************************************


from code.algorithms.nearesthouse import nearestHouse
from code.algorithms.random import Random
from code.classes import battery, district, house
from code.visualisation.visualisation import make_district

import csv, json

if  __name__ == "__main__":
    

#Example converting csv to json output
    # csvFilePath = "data/district-1_batteries.csv"
    # jsonFilePath = "district.json"

    # data={}
    # with open(csvFilePath) as csvFile:
    #     reader = csv.DictReader(csvFile)
    #     for row in reader:
    #         positie=row["positie"]
    #         data[positie]= row
        
    # with open (jsonFilePath, "w") as jsonfile:
    #     jsonfile.write(json.dumps(data, indent=4 ))

    test_district = district.District("data/district-1_batteries.csv","data/district-1_houses.csv")
    batteries = test_district.batteries
    houses = test_district.houses

   
    
    possibility = nearestHouse(test_district)
    visual_district = make_district(test_district)
    
 
    print(possibility)

    
    for battery in batteries:
        print(battery.location)
        for house in battery.connected_houses:
            print(house.location)
            print(house.cable)
            print(house.cable_points)