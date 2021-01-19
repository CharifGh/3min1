import copy
from operator import attrgetter
from itertools import combinations


class FirstAlgorithm:
    """Switches connections with better connections"""
    def __init__(self, valid_district):
        self.district = copy.deepcopy(valid_district)
       

    def get_true_connections(self):
        existing_cons = self.district.get_true_connections()
        return existing_cons


    def get_false_connections(self):
        potential_cons = self.district.get_false_connections()
        return potential_cons


    def find_a_connection(self, house, battery):
        """Finds a specific connection with a house and battery"""
        potential_cons = self.get_false_connections()
        get_new_con = [p_a for p_a in potential_cons if p_a.house == house and p_a.battery == battery]
        new_con = get_new_con[0]
        return new_con


    def find_multiple_connections(self, battery):
        """Finds all existing connections for a specific battery"""
        all_true = self.get_true_connections()
        cons_with_battery = [con for con in all_true if con.battery == battery]
        return cons_with_battery



    def make_switch(self, old_connection, new_connection):
        """Calls District function to make and break the connections that need to be switched"""
        self.district.break_connection(old_connection)
        self.district.make_connection(new_connection)        



    def find_some_switches(self, ex_con, valid_switches):
        cons_to_switch = {}
        # best_new_distance = float('inf')
        free_cap = ex_con.battery.get_free_capacity(ex_con.output)
        for battery_group in valid_switches:
            for i in range(3,0,-1):
                for combi in combinations(battery_group, i):
                    linked_battery = combi[0].battery
                    combi_output = sum(con.output for con in combi)
                    if combi_output <= free_cap and ex_con.output <= linked_battery.get_free_capacity(combi_output):
                        new_ex_con = self.find_a_connection(ex_con.house, linked_battery)
                        new_first = self.find_a_connection(combi[0].house, ex_con.battery)
                        total_new_distance = new_ex_con.calc_penalty() + new_first.calc_penalty()
                        if len(combi) > 1:
                            new_second = self.find_a_connection(combi[1].house, ex_con.battery)
                            total_new_distance = total_new_distance + new_second.calc_penalty()
                        if len(combi) > 2:
                            new_third = self.find_a_connection(combi[2].house, ex_con.battery)
                            total_new_distance = total_new_distance + new_third.calc_penalty()

                        total_old_distance = ex_con.calc_penalty() + sum(con.calc_penalty() for con in combi)
                        
                        if total_new_distance < total_old_distance:
                            # if total_new_distance < best_new_distance:
                            cons_to_switch = {}
                            # best_new_distance = total_new_distance
                            cons_to_switch['first_switch'] = combi[0]
                            cons_to_switch['new_first'] = new_first 
                            cons_to_switch['new_ex_con'] = new_ex_con    
                            if len(combi) > 1:
                                cons_to_switch['second_switch'] = combi[1]
                                cons_to_switch['new_second'] = new_second
                            if len(combi) > 2:
                                cons_to_switch['third_switch'] = combi[2]
                                cons_to_switch['new_third'] = new_third             
                           
        return cons_to_switch                     



    def do_stuff_with_connections(self):    
        """The run function of this algorithm"""
        changes = True
        i = 0
        while changes:
            potential_cons = self.get_false_connections()
            existing_cons = self.get_true_connections()
            existing_cons.sort(key=lambda h: h.calc_penalty(), reverse=True)
            j = 0
            for ex_con in existing_cons: 
                j = j +1  
                if j%30 == 0:
                    print(f"j = {j}")             
                other_cons_house = [och for och in potential_cons if och.house == ex_con.house]
                valid_switches = self.get_valid_switches(other_cons_house)
                cons_to_switch = self.find_some_switches(ex_con, valid_switches)

                if cons_to_switch:
                    changes = True
                    self.make_switch(ex_con, cons_to_switch['new_ex_con'])
                    self.make_switch(cons_to_switch['first_switch'], cons_to_switch['new_first'])
                    if 'second_switch' in cons_to_switch:
                        print(f"combi at {i}")
                        self.make_switch(cons_to_switch['second_switch'], cons_to_switch['new_second'])
                        if 'third_switch' in cons_to_switch:
                            print(f"And even a triple at {i}!")
                            self.make_switch(cons_to_switch['third_switch'], cons_to_switch['new_third'])
                    i = i + 1
                    break
                else:
                    changes = False


    def get_valid_switches(self, other_cons_house):
        """Gets all connections that current connection can make a valid switch with"""
        valid_switches = []
        for other_con in other_cons_house:
            other_cons_with_battery = self.find_multiple_connections(other_con.battery)
            valid_switches.append(other_cons_with_battery)
        return valid_switches                
    