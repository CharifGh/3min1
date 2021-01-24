import copy


class DepthFirst:
    """Check for connections if visited append them to list."""
    def __init__(self, connections):
        self.connections = copy.deepcopy(connection)
        self.visited_connections = []
 
    def get_next_connection(self, connection):
        """check if connection in visited_connections else append connection to visited_connections"""
        if connection not in visited_connections:
            visited_connections.append(connection)
            for next_con in visited_connections[connection]:
                get_next_connection(connection)
        return visited_connections