# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************

from .battery import Battery
from .house import House
from .connection import Connection
from operator import attrgetter
from itertools import combinations
import csv, json

class District():
    def __init__(self, batteries_file, houses_file):
        self.name = self.get_name(batteries_file)
        self.batteries = self.load_batteries(batteries_file)
        self.houses = self.load_houses(houses_file)
        self.connections = self.get_all_connections()
        self.retries = 0
        self.total_free_cap = self.calc_total_free_cap()
        

    def get_name(self, batteries_file):
        """District is going to need a name"""
        file = open(batteries_file, 'r')
        for x in file.name:
            if x.isdigit():
                name = x
                file.close()
                return name        


    def load_batteries(self, batteries_file):
        """Load all batteries into district"""   
        batteries = []     
        with open(batteries_file, "r") as in_file:
            reader = csv.DictReader(in_file)
            all_batteries = list(reader)
            for battery in all_batteries:
                batteries.append(Battery(battery['x'], battery['y'], battery['capaciteit']))  
        return batteries


    def load_houses(self, houses_file):
        """Load all batteries into district"""
        houses = []     
        with open(houses_file, "r") as f:
            reader = csv.DictReader(f)
            all_houses = list(reader)
            for house in all_houses:
                houses.append(House(house['x'], house['y'], house['maxoutput']))
        return houses 

               
    def get_all_connections(self):
        """Calculates all distances between batteries and houses, returns a list of dicts"""
        connections = []
        for battery in self.batteries:
            for house in self.houses:
                connection = Connection(self, battery, house)
                connections.append(connection)
        return connections    

    
    def unconnected_houses(self):
        """List of all unconnected houses"""
        unconnected_houses = [house for house in self.houses if not house.get_status()] 
        return unconnected_houses 


    def make_connection(self, connection):
        """Make a connection between a battery and a house"""
        connection.make_connection()
        connection.battery.add_house(connection.house)
        connection.house.set_connection()
        

    def break_connection(self, connection):
        """Break a connection between a battery and a house"""    
        connection.break_connection()
        connection.battery.remove_house(connection.house)
        connection.house.break_connection()


    def add_retry(self):
        """Add 1 for every time the random algorithm finds invalid solution"""
        self.retries = self.retries +1


    def try_again(self):
        """Resets values to default"""
        for connection in self.connections:
            connection.break_connection()
        for house in self.houses:
            house.break_connection()
        for battery in self.batteries:
            battery.remove_all_houses()        
          

    def get_true_connections(self):
        """Returns all existing connections between the batteries and houses"""
        true_connections = [connection for connection in self.connections if connection.connected]
        return true_connections


    def get_false_connections(self):
        """Returns all possible, but not existing, connections between batteries and houses"""
        false_connections = [connection for connection in self.connections if not connection.connected]
        return false_connections    


    def find_specific_connection(self, house, battery):
        """Finds a specific connection with a house and battery"""
        get_new_con = [p_a for p_a in self.connections if p_a.house == house and p_a.battery == battery]
        new_con = get_new_con[0]
        return new_con


    def find_all_cons_battery(self, battery):
        """Finds all existing connections for a specific battery"""
        cons_with_battery = [con for con in self.get_true_connections() if con.battery == battery]
        return cons_with_battery


    def get_house_connections(self, house):
        """Gets the other connections with the house of the given connection"""
        house_cons = [con for con in self.connections if con.house == house]
        return house_cons


    def check_validity(self):
        """Checks if solution is valid"""
        if self.unconnected_houses():
            return False 
        for battery in self.batteries:
            if battery.get_total_input() > battery.capacity:
                return False
        return True    


    def calc_distance(self):
        """Calculates the total distance of all true connections"""
        total_distance = sum([connection.distance for connection in self.get_true_connections()])
        return total_distance


    def make_cables(self):
        """For each house calls the function to construct the cable to the connected battery"""
        for connection in self.get_true_connections():
            if not connection.house.cable_points:
                connection.house.construct_cable(connection.battery.x_grid, connection.battery.y_grid, connection.distance)


    def calc_costs(self):
        """Returns the total length of all cables"""
        cable_points = 0
        for house in self.houses:
            cable_points = cable_points + len(house.cable_points)
        return cable_points


    def get_output(self):
        """Get all necessary data and puts it in a json file"""
        all_data = []
        costs_own = 0
        costs_own = self.calc_costs()*9  
        for battery in self.batteries:
            costs_own = costs_own+5000
        all_data.append({'district': 1, 'costs-own': costs_own})
        for battery in self.batteries:
            houses = [] 
            for house in battery.connected_houses:
                houses.append({'location': house.location, 'output': house.output, 'cables': house.cable_points})
            all_data.append({'location': battery.location, 'capacity': battery.capacity, 'houses': houses})

        out_file = open('output.json', 'w')
        json.dump(all_data, out_file)

        out_file.close()   

        
    def get_bat_cons(self, battery):
        """Returns a list of all available connections for a battery"""
        all_cons = self.get_false_connections()
        bat_cons = [bc for bc in all_cons if bc.battery == battery and not bc.house.get_status()]
        return bat_cons

            
    def get_fullest_batteries(self):
        """Returns a list of the batteries sorted by the highest input"""
        batteries = self.batteries
        batteries.sort(key=lambda s: s.get_total_input(), reverse=True)
        return batteries


    def get_all_combis(self, battery, extra, some_value):
        """Finds possible combis for a battery"""
        max_houses = self.get_max_houses(battery)
        min_houses = self.get_min_houses(battery)

        bat_cons = self.get_bat_cons(battery)
        bat_cons.sort(key=attrgetter('x_best'))
        bat_cons2 = bat_cons[0:max_houses+extra]

        bat_combis = []
        for i in range(min_houses, max_houses+1, 1):
            for combi in combinations(bat_cons2, i):
                combi_output = sum(com.output for com in combi)
                free_battery_cap = battery.capacity - battery.get_total_input()
                if combi_output <= free_battery_cap and (battery.capacity - combi_output - battery.get_total_input()) < (self.total_free_cap/some_value):
                    bat_combis.append({
                        'distance': sum(con.distance for con in combi),
                        'output': combi_output,
                        'combi': combi
                    })
        return bat_combis


    def calc_total_free_cap(self):
        """Calculates the difference in total max capacity of the batteries and the total max output of the houses"""
        total_cap = sum([battery.capacity for battery in self.batteries])
        total_output = sum([house.output for house in self.houses])
        total_free_cap = total_cap - total_output
        return total_free_cap        


    def get_min_houses(self, battery):
        """Calculates the lowest number of houses that can still be connected to the battery"""
        free_space = battery.capacity - battery.get_total_input()
        houses = self.unconnected_houses()
        houses.sort(key=attrgetter('output'), reverse=True)
        min_houses = 0
        for house in houses:
            if (free_space - house.output) >= 0:
                min_houses += 1
                free_space = free_space - house.output        
        return min_houses


    def get_max_houses(self, battery):
        """Calculates the highest number of houses that can still be connected to the battery"""
        free_space = battery.capacity - battery.get_total_input()
        houses = self.unconnected_houses()
        houses.sort(key=attrgetter('output'))
        max_houses = 0
        for house in houses:
            if (free_space - house.output) >= 0:
                max_houses = max_houses + 1
                free_space = free_space - house.output        
        return max_houses


    def connect_bests(self, penalty):
            """Connects the houses with a high penalty for their second best battery to their best battery"""
            x_bests = [con for con in self.connections if con.x_best == 2 and con.penalty > penalty]
            x_bests.sort(key=attrgetter('penalty'), reverse=True)
            for connection in x_bests:
                other_connections = [con for con in self.get_house_connections(connection.house) if con.x_best < 2]
                if other_connections:
                    best = other_connections[0]
                    if (best.battery.get_total_input() + best.output) <= best.battery.capacity and not best.house.get_status():
                        self.make_connection(best)      


    def prune_some_more(self, number_of_houses):
        """Connects some more houses that could otherwise lead to high penalties"""
        while (len(self.unconnected_houses()) > number_of_houses):
            connections = self.get_lowest_available_con()
            for connection in connections:
                if self.connect_worst(connection):
                    break


    def get_lowest_available_con(self):
        """Returns a sorted list of connections with high penalties""" 
        houses = self.unconnected_houses()
        all_best_options = []
        for house in houses:
            all_cons = self.get_house_connections(house)
            selected_cons = [con for con in all_cons if con.battery_available()]
            if len(selected_cons) > 1:
                selected_cons.sort(key=attrgetter('x_best'))
                all_best_options.append(selected_cons[1])    
        all_best_options.sort(key=attrgetter('penalty'), reverse=True) 
        return all_best_options
        

    def connect_worst(self, connection):
        """Makes connections for houses that would otherwise get high penalties"""
        free_cap = self.total_free_cap
        other_connections = [con for con in self.get_house_connections(connection.house)]
        best_options = [oc for oc in other_connections if oc.battery_available() and oc.x_best < connection.x_best]
        best_option = best_options[0]
        total = (best_option.battery.capacity - best_option.battery.get_total_input() - best_option.output)
        if total > free_cap or total < (free_cap/10):       
            self.make_connection(best_option)
            return True            
