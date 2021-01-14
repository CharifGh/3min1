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

    # test_district = district.District("data/district-1_batteries.csv","data/district-1_houses.csv")
   
    
    
    # visual_district = make_district(test_district)
    
 
    # print(possibility.calc_costs())
    # print(possibility.retries)
   
    # Calculate baseline
    total_costs = 0
    total_retries = 0
    lowest_costs = 6000
    i=0
    for i in range(1000):
        test_district = district.District("data/district-1_batteries.csv","data/district-1_houses.csv")
        possibility = randomly_connect(test_district)
        total_retries = total_retries + possibility.retries
        total_costs = total_costs + possibility.calc_costs()
        if possibility.calc_costs() < lowest_costs:
            lowest_costs = possibility.calc_costs()
        i= i+1    

    print(f"Lowest: {lowest_costs}")
    average_retries = total_retries / 1000
    print(f"Average amount of retries: {average_retries}")
    average_costs = total_costs / 1000
    print(f"Average costs: {average_costs}")    
