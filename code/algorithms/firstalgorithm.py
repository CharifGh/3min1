import copy
from operator import attrgetter


class FirstAlgorithm:
    def __init__(self, valid_district):
        self.district = copy.deepcopy(valid_district)
       

    def get_true_connections(self):
        existing_cons = self.district.get_true_connections()
        return existing_cons


    def get_false_connections(self):
        potential_cons = self.district.get_false_connections()
        return potential_cons


    def get_valid_switches(self, ex_con, other_cons_house):
        """Gets all connections that current connection can make a valid switch with"""
        valid_switches = []
        for other_con in other_cons_house:
            other_cons_with_battery = self.find_multiple_connections(other_con.battery)
            for ocb in other_cons_with_battery:
                free_cap_a = ex_con.battery.get_free_capacity(ex_con.output)
                free_cap_b = other_con.battery.get_free_capacity(ocb.output)
                if free_cap_a >= ocb.output and free_cap_b >= ex_con.output:
                    valid_switches.append(ocb)
        return valid_switches                


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


    def find_best_switch(self, ex_con, valid_switches):
        """Finds the best connection to switch with from a list of valid switches"""
        cons_to_switch = {}
        best_new_distance = float('inf')
        for valid_switch in valid_switches:
            new_con_a = self.find_a_connection(valid_switch.house, ex_con.battery)
            new_con_b = self.find_a_connection(ex_con.house, valid_switch.battery)

            total_new_distance = new_con_a.distance + new_con_b.distance
            total_old_distance = ex_con.distance + valid_switch.distance

            if total_new_distance < total_old_distance:
                if total_new_distance < best_new_distance:
                    best_new_distance = total_new_distance
                    cons_to_switch['best_switch'] = valid_switch
                    cons_to_switch['new_con_a'] = new_con_a
                    cons_to_switch['new_con_b'] = new_con_b      
        return cons_to_switch
                        

    def make_switch(self, old_connection, new_connection):
        """Calls District function to make and break the connections that need to be switched"""
        self.district.break_connection(old_connection)
        self.district.make_connection(new_connection)        


    def do_stuff_with_connections(self, iterations):    
        """The run function of this algorithm"""
        i = 0
        for i in range(iterations): 
            potential_cons = self.get_false_connections()
            existing_cons = self.get_true_connections()
            existing_cons.sort(key=attrgetter('distance', 'output'), reverse=True)

            for ex_con in existing_cons:                
                other_cons_house = [och for och in potential_cons if och.house == ex_con.house and och.distance < ex_con.distance]
                
                if other_cons_house:
                    valid_switches = self.get_valid_switches(ex_con, other_cons_house)

                    if valid_switches:
                        cons_to_switch = self.find_best_switch(ex_con, valid_switches)

                        if cons_to_switch:
                            self.make_switch(ex_con, cons_to_switch['new_con_a'])
                            self.make_switch(cons_to_switch['best_switch'], cons_to_switch['new_con_b'])

                            break

            i = i+1


