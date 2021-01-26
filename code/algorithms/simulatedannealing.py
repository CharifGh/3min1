import copy


class SimmulatedAnnealing:
    """Check for connections if visited append them to list."""
    def __init__(self, district):
        self.district = copy.deepcopy(district)
        self.result = []
        self.start = 1000
        self.change = 0.97

    def connections(self):
        while self.start < 0.0:
            self.district.make_cables()



  
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

