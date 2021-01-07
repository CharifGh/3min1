# ****************************************
# Main.py                                *
# Paulien Tideman en Charif Ghammane     *
# Implementation of Smart Grid functions *
# ****************************************


from . import classes
from . import data
import csv, json

if  __name__ == "__main__":

    # implement load function
    inputfiles = [file for file in data if file.endswith('.csv')]
    outputfile = "json_data"

    for file in inputfiles:
        data={}
        with open(data "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #id
                #xas
                #yas
                #output/capacity

        with open (outputfile, "a") as jsonfile:
            jsonfile.wire(json.dumps(data, indent=2, sort_keys=True ))