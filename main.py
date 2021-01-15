# ****************************************
# Main.py                                *
# Paulien Tideman en Charif Ghammane     *
# Implementation of Smart Grid functions *
# ****************************************


from code.algorithms.nearesthouse import nearestHouse
from code.algorithms.random import randomly_connect
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


    best_result = None
    lowest_cables = 6000
    for i in range(10000):
        test_district = district.District("data/district-1_batteries.csv","data/district-1_houses.csv")
        possibility = randomly_connect(test_district)
        if possibility.calc_costs() < lowest_cables:
            lowest_cables = possibility.calc_costs()
            best_result = possibility
    
    best_result.get_output()
    visual_district = make_district(best_result)
    print(best_result.calc_costs())
   