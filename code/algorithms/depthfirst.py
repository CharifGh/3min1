import copy


class DepthFirst:
    """Check for connections if visited append them to list."""
    def __init__(self, connection):
        self.connection = copy.deepcopy(connection)
        self.visited_connections = []
 
    def get_next_connection(self, connection):
        """check if connection in visited_connections else append connection to visited_connections"""
        if self.connection not in visited_connections:
            visited_connections.append(self.connection)
            for next_con in visited_connections[self.connection]:
                get_next_connection(self.connection)
        return visited_connections

    def valid_solution(self):
        """Do some calculation to check if connection is valid"""
        pass
    
    def run(self):
        """Run algorith untill all connections are made"""
        while self.connection:
            new_connection = self.get_next_connection()

            # check if calculation has valid solution break the algorithm else continue making connections
            if valid_solution():
                break