import copy


class DepthFirst:
    """Check for connections if visited append them to list."""
    def __init__(self, district, connection):
        self.district = copy.deepcopy(district)
        self.visited_connections = []
        self.connection = copy.deepcopy(connection)
        self.solutions=None
        self.value= float('inf')

        
    def get_next_connection(self):
        """check if connection in visited_connections else append connection to visited_connections"""
        connection = self.connection
        if connection not in self.visited_connections:
            self.visited_connections.append(connection)
            for next_con in self.visited_connections[connection]:
               dfs= get_next_connection(self.district, self.connection)

        return self.visited_connections


    def run(self):
        """Run algorith untill all connections are made"""
        while self.district:
            new_connection = self.get_next_connection()

     
            if self.district.check_validity == True:
                break


            #bepaalde state
            # state-space


            #langzaam afkoelen
            #start tempratuur (D= 1000)
            # resutltaat
            # while < D =0
            # hill climber (een verbinding veranderen)# kijken of ie beter is? > nieuw resultaat
            # zo ja = accepteer verandering.
            # random configratie


            # Conditie:
                # slechter ook accepteren
                #meer ruimte voor andere kabels beter resultaat
                # hoe kleiner tempratuur hoe kleiner de kans dat je slechter oplossing accepteert.
                # local minimum = beste oplossing als je dingen neer hebt gezegd
                # global minimum
                #1000
                # x0.97
                # kleiner dan .01 of .001
                # wanneer accepteer ik hem : math.exp 
                # delta = kosten nieuwe oplossing - oude oplossing
                #     e^-(delta/T)
                # kijken fo die groter is dan de formule. En daarmee krijg je verbetring of verslechtering. 
                # alstie groter is dan is oplossing verslechtering
                # pseudo simulated annealing

