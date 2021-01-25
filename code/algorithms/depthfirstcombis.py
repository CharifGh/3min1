import copy

class DepthFirstCombinations():
    def __init__(self, district):
        self.district = copy.deepcopy(district)
        self.batteries = self.district.get_fullest_batteries()
        self.shortest_distance = float('inf')
        self.all_distances = []
        self.best_result = None
        self.states = []
        self.valid_solutions = []


    def find_best_combi(self):
        """The run function of this algorithm"""
        first_combis = self.district.get_all_combis(self.batteries[0], 6, 10)
        for combi in first_combis:
            self.add_states(combi)
        print(f"number of states: {len(self.states)}")
        while self.states:
            new_district = self.get_next_state()
            self.second_combis = new_district.get_all_combis(new_district.batteries[1], 4, 10)
            print(len(self.second_combis))
            for combi2 in self.second_combis:
                self.make_second_descent(new_district, combi2)
        return self.best_result                


    def make_second_descent(self, new_district, combi2):
        for con in combi2['combi']:
            new_district.make_connection(con)   
        self.third_combis = new_district.get_all_combis(new_district.batteries[2], 3, 7)
        print(len(self.third_combis))
        for combi3 in self.third_combis:
            self.make_third_descent(new_district, combi3)
        for con in combi2['combi']:
            new_district.break_connection(con)    
            

    def make_third_descent(self, new_district, combi3):
        for con in combi3['combi']:
            new_district.make_connection(con)
        self.fourth_combis = new_district.get_all_combis(new_district.batteries[3], 3, 4)
        print(f"got to fourth {len(self.fourth_combis)}")
        for combi4 in self.fourth_combis:
            self.make_fourth_descent(new_district, combi4)
        for con in combi3['combi']:
            new_district.break_connection(con)    
            
    
    def make_fourth_descent(self, new_district, combi4):
        for con4 in combi4['combi']:
            new_district.make_connection(con4)
        self.fifth_combis = new_district.get_all_combis(new_district.batteries[4], 1, 2)
        while self.fifth_combis:
            combi5 = self.get_fifth_combis()
            for con5 in combi5['combi']:
                new_district.make_connection(con5)
            if new_district.check_validity():
                print("got one!------------------------------------------------")
                valid_solution = copy.deepcopy(new_district)
                self.valid_solutions.append(valid_solution)
                self.compare_solution(valid_solution)
                self.fifth_combis = []
            else:
                for con5 in combi5:
                    new_district.break_connection   
        for con4 in combi4['combi']:
            new_district.break_connection(con4)                                                       


    def get_fifth_combis(self):
        self.fifth_combis.sort(key=lambda d: d['distance'])
        first_fifth = self.fifth_combis[0]
        for any_distance in self.all_distances:
            if (first_fifth['distance'] + self.district.calc_distance()) >= any_distance:
                return False
        return self.fifth_combis.pop(0)


    def get_next_state(self):
        return self.states.pop()


    def add_states(self, combi):
        new_district = copy.deepcopy(self.district)
        all_cons = combi['combi']
        for con in all_cons:
            new_district.make_connection(con)
        self.states.append(new_district)    


    def compare_solution(self, valid_solution):
        total_distance = valid_solution.calc_distance()
        if total_distance < self.shortest_distance:
            self.all_distances.append(total_distance)
            self.shortest_distance = total_distance
            self.best_result = valid_solution
