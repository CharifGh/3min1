# ****************************************
# Main.py                                *
# Paulien Tideman en Charif Ghammane     *
# Implementation of Smart Grid functions *
# ****************************************


from code.algorithms.nearesthouse import nearestHouse
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

    visual_district = make_district(test_district)
    costs = nearestHouse(test_district)
    for battery in batteries:
        print(f"this is battery at: {battery}")
        for house in battery.connected_houses:
            print(f"this is house at: {house.location}")
            print(f"cable has length: {house.cable}")
            print(house.cable_points)

    # To do: 
    print(costs)
    print(test_district)


    