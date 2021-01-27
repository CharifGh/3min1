# ****************************************
# Main.py                                *
# Paulien Tideman en Charif Ghammane     *
# Implementation of Smart Grid functions *
# ****************************************


from code.algorithms.hillclimber import HillClimber as hc
from code.algorithms.random import randomly_connect
from code.classes import district
from code.visualisation.visualisation import make_district
from code.visualisation.supporting_visuals import make_graph
from code.algorithms.greedy_sharing import share_cables, make_groups
from code.algorithms.depthfirstcombis import DepthFirstCombinations as dfc


if  __name__ == "__main__":
    
    # Choose a district
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

    # Choose an algorithm
    which_algorithm = input("Welk algoritme wil je toepassen?:\n HillClimber = 1\n Combinations = 2\n Shared cables = 3\n")

    if which_algorithm == '1':
        random_district = randomly_connect(chosen_district)
        hillclimb = hc(random_district)
        hillclimb.do_stuff_with_connections()
        hillclimb.district.make_cables()
        print(hillclimb.district.calc_costs())
        visual = make_district(hillclimb.district)

    # With the current parameters this only works on district 2 and it takes a long time
    elif which_algorithm == '2':
        chosen_district.connect_bests(11)
        chosen_district.prune_some_more(45)
        dfc_district = dfc(chosen_district)
        best_one = dfc_district.find_best_combi()
        if best_one:
            best_one.make_cables()
            print(best_one.calc_costs())
            best_one.get_output()
            visual = make_district(best_one)   

    # Won't give valid solutions yet
    elif which_algorithm == '3':
        make_groups(chosen_district)
        share_cables(chosen_district)
        chosen_district.calc_distance()
        visuals = make_district(chosen_district)

    else:
        print("Algorithm not found")    
        exit()
