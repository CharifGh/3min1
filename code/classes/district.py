# **************************************
# Classes.py                           *
# Paulien Tideman en Charif Ghammane   *
# Implementation of Smart Grid classes *
# **************************************


# loads houses and batteries 

#output = return batteries and houses

from .battery import Battery
from .house import House
from .connection import Connection

import csv, json

class District():
    def __init__(self, batteries_file, houses_file):
        self.name = 1
        self.batteries = self.load_batteries(batteries_file)
        self.houses = self.load_houses(houses_file)
        self.retries = 0
        self.connections = self.get_all_connections()


    def get_name(self):
        """District is going to need a name"""
        pass


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
        for battery in self.get_batteries():
            for house in self.get_houses():
                connection = Connection(self, battery, house)
                connections.append(connection)
        return connections      

    
    def get_batteries(self):
        """Returns all the batteries"""
        return self.batteries


    def get_houses(self):
        """Returns all the houses"""
        return self.houses    
    
    
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


    def get_house_connections(self, connection):
        """Gets the other connections with the house of the given connection"""
        other_house_cons = [con for con in self.connections if con.house == connection.house and con != connection]
        return other_house_cons


    def check_validity(self):
        """Checks if solution is valid"""
        if self.unconnected_houses():
            return False
        return True        


    def make_cables(self):
        """For each house calls the function to construct the cable to the connected battery"""
        true_connections = self.get_true_connections()
        for connection in true_connections:
            connection.house.construct_cable(connection.battery, connection.distance)


    def calc_costs(self):
        """Returns the total length of all cables"""
        true_connections = self.get_true_connections()
        total_cable_length = sum(connection.distance+1 for connection in true_connections)   
        return total_cable_length


    def get_output(self):
        """Get all necessary data and puts it in a json file"""
        all_data = []
        costs_own = 0
        costs_own = self.calc_costs()*9  
        for battery in self.get_batteries():
            costs_own = costs_own+5000
        all_data.append({'district': 1, 'costs-own': costs_own})
        for battery in self.get_batteries():
            houses = [] 
            for house in battery.connected_houses:
                houses.append({'location': house.location, 'output': house.output, 'cables': house.cable_points})
            all_data.append({'location': battery.location, 'capacity': battery.capacity, 'houses': houses})

        out_file = open('output.json', 'w')
        json.dump(all_data, out_file)

        out_file.close()   