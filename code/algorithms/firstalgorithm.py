import copy
from operator import attrgetter
from itertools import combinations


class FirstAlgorithm:
    """Switches connections with better connections"""
    def __init__(self, valid_district):
        self.district = copy.deepcopy(valid_district)
        self.improvements = []
       

    def get_true_connections(self):
        existing_cons = self.district.get_true_connections()
        return existing_cons


    def get_false_connections(self):
        potential_cons = self.district.get_false_connections()
        return potential_cons


    def find_specific_connection(self, house, battery):
        """Finds a specific connection with a house and battery"""
        potential_cons = self.get_false_connections()
        get_new_con = [p_a for p_a in potential_cons if p_a.house == house and p_a.battery == battery]
        new_con = get_new_con[0]
        return new_con


    def find_all_cons_battery(self, battery):
        """Finds all existing connections for a specific battery"""
        all_true = self.get_true_connections()
        cons_with_battery = [con for con in all_true if con.battery == battery]
        return cons_with_battery


    def make_switch(self, old_connection, new_connection):
        """Calls District function to make and break the connections that need to be switched"""
        self.district.break_connection(old_connection)
        self.district.make_connection(new_connection)        


    def get_all_options(self, other_cons_house):
        """Gets all connections that current connection might switch with"""
        all_options = []
        for other_con in other_cons_house:
            other_cons_with_battery = self.find_all_cons_battery(other_con.battery)
            all_options.append(other_cons_with_battery)
        return all_options                                 


    def switch_these(self, cons_to_switch, ex_con):
        """Calls the make_switch function for the connections that need to be switched"""
        self.make_switch(ex_con, cons_to_switch['new_ex_con'])
        self.make_switch(cons_to_switch['first_switch'], cons_to_switch['new_first'])
        if 'second_switch' in cons_to_switch:
            self.make_switch(cons_to_switch['second_switch'], cons_to_switch['new_second'])
            if 'third_switch' in cons_to_switch:
                self.make_switch(cons_to_switch['third_switch'], cons_to_switch['new_third'])
        


    def find_some_switches(self, ex_con, all_options):
        all_combis = []
        for battery_group in all_options:
            pruned_group = [c for c in battery_group if c.penalty > 0]
            for i in range(2,0,-1):
                for combi in combinations(pruned_group, i):
                    combis = self.do_stuff_with_combi(combi, ex_con)
                    if combis:
                        all_combis.append(combis)
        if all_combis:
            all_combis.sort(key=lambda a: a['distance'])
            return all_combis[0]
        return False    


    def do_stuff_with_combi(self, combi, ex_con):
        cons_to_switch = {}
        free_cap = ex_con.battery.get_free_capacity(ex_con.output)                
        linked_battery = combi[0].battery
        combi_output = sum(con.output for con in combi)
        if combi_output <= free_cap and ex_con.output <= linked_battery.get_free_capacity(combi_output):
            new_ex_con = self.find_specific_connection(ex_con.house, linked_battery)
            new_first = self.find_specific_connection(combi[0].house, ex_con.battery)
            total_new_distance = new_ex_con.distance + new_first.distance
            if len(combi) > 1:
                new_second = self.find_specific_connection(combi[1].house, ex_con.battery)
                total_new_distance = total_new_distance + new_second.distance
            
            total_old_distance = ex_con.distance + sum(con.distance for con in combi)
            
            if total_new_distance < total_old_distance: 
                cons_to_switch['distance'] = total_new_distance
                cons_to_switch['first_switch'] = combi[0]
                cons_to_switch['new_first'] = new_first 
                cons_to_switch['new_ex_con'] = new_ex_con    
                if len(combi) > 1:
                    cons_to_switch['second_switch'] = combi[1]
                    cons_to_switch['new_second'] = new_second      
                
        return cons_to_switch                     



    def do_stuff_with_connections(self):    
        """The run function of this algorithm"""
        changes = True
        for con in self.district.connections:
            con.calc_penalty()
        while changes:
            k = 0
            existing_cons = self.get_true_connections()
            existing_cons.sort(key=attrgetter('penalty'), reverse=True)
            for ex_con in existing_cons:                
                other_cons_house = [och for och in self.district.get_house_connections(ex_con)]
                all_options = self.get_all_options(other_cons_house)
                cons_to_switch = self.find_some_switches(ex_con, all_options)

                if cons_to_switch:
                    self.switch_these(cons_to_switch, ex_con)
                    changes = True
                    self.improvements.append({'i': self.district.calc_costs()})
                    break
                else: 
                    k +=1
                    if k == 150:
                        if self.district.check_validity():
                            changes = False



                    