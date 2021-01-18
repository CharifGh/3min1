# ****************************************
# Main.py                                *
# Paulien Tideman en Charif Ghammane     *
# Implementation of Smart Grid functions *
# ****************************************


from code.algorithms.firstalgorithm import FirstAlgorithm as fa
from code.algorithms.random import randomly_connect
from code.algorithms.nearesthouse import nearestHouse
from code.classes import district
from code.visualisation.visualisation import make_district

if  __name__ == "__main__":
    

    total_best = None
    total_lowest = 10000

    for f in range(1):
        test_district = district.District("data/district-1_batteries.csv","data/district-1_houses.csv")
        possibility = nearestHouse(test_district)
        print(f"Total cable length of semi-random valid solution ({f}): {possibility.calc_costs()}")

        first_algorithm = fa(possibility)
        first_algorithm.do_stuff_with_connections(200)

        print(f"Total cable length after algorithm ({f}): {first_algorithm.district.calc_costs()}")
        
        if first_algorithm.district.calc_costs() < total_lowest:
            total_best = first_algorithm.district
            total_lowest = first_algorithm.district.calc_costs()

    print(f"Best solution: {total_lowest}")
    total_best.make_cables()
    visual_district = make_district(total_best)