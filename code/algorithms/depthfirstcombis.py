import copy

class DepthFirstCombinations():
    def __init__(self, district):
        self.district = copy.deepcopy(district)
        self.shortest_distance = float('inf')
        self.all_distances = []
        self.best_result = None
        self.states = [copy.deepcopy(self.district)]
        self.valid_solutions = []   


    def find_best_combi(self):
        """The run function of this algorithm"""
        while self.states:
            new_district = self.get_next_state()
            
            if len(new_district.free_batteries) > 0:
                battery = new_district.get_available_batteries()
                combis = new_district.get_all_combis(battery) 
                
                if combis:
                    for combi in combis:
                        self.add_states(new_district, combi)
                else:
                    self.check_solution(new_district)
            else:
                self.check_solution(new_district)
           


    def get_next_state(self):
        return self.states.pop()


    def add_states(self, new_district, combi):
        """Adds new states to the stack"""
        next_district = copy.deepcopy(new_district)
        for con in combi:
            next_district.make_connection(con)
        self.states.append(next_district)    


    def compare_solution(self, valid_solution):
        """Checks if the new solution is better than any previous solutions"""
        total_distance = valid_solution.calc_distance()
        if total_distance < self.shortest_distance:
            self.all_distances.append(total_distance)
            self.shortest_distance = total_distance
            self.best_result = valid_solution


    def check_solution(self, new_district):
        """Checks if a state is valid"""
        if new_district.check_validity():    
            valid_solution = copy.deepcopy(new_district)
            self.valid_solutions.append(valid_solution)
            self.compare_solution(valid_solution)
            return True
        return False    
           