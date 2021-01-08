# ****************************************
# Main.py                                *
# Paulien Tideman en Charif Ghammane     *
# Implementation of Smart Grid functions *
# ****************************************


from code.classes import battery, district, house

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
    print(f"this is{test_district}")