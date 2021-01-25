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
    
    # Chose a district
    which_district = input("Welk district wil je zien?: 1, 2, 3\n")
    if which_district == '1':
        chosen_district = district.District("data/district-1_batteries.csv","data/district-1_houses.csv")
    elif which_district == '2':
        chosen_district = district.District("data/district-2_batteries.csv","data/district-2_houses.csv")
    elif which_district == '3':
        chosen_district = district.District("data/district-3_batteries.csv","data/district-3_houses.csv")
    else:
        print("District not found")
        exit()            
    
    # Update the connections
    for con in chosen_district.connections:
        con.calc_rating()

    # Chose an algorithm
    which_algorithm = input("Welk algoritme wil je toepassen?:\n HillClimber = 1\n Combinations = 2\n")

    if which_algorithm == '1':
        random_district = randomly_connect(chosen_district)
        hillclimb = fa(random_district)
        hillclimb.do_stuff_with_connections()
        hillclimb.district.make_cables()
        print(hillclimb.district.calc_costs())
        hillclimb.district.get_output()
        visual_district = make_district(hillclimb.district)

    # elif which_algorithm == '2':
        # chosen_district.connect_bests(11)
        # chosen_district.prune_some_more(45)
        # dfc_district = dfc(chosen_district)
        # best_one = dfc_district.find_best_combi()
        # if best_one:
            # best_one.make_cables()
            # print(best_one.calc_costs())
            # best_one.get_output()
            # visual = make_district(best_one)
        


    else:
        print("Algorithm not found")    
        exit()


    