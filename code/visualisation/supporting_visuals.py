import matplotlib.pyplot as plt

def make_graph(all_districts):

    max_i = 0
    max_all_costs = []
    for r in all_districts:
        local_max = 0
        i = len(r.improvements)
        if i > max_i:
            max_i = i
        for j in r.improvements:
            if j['i'] > local_max:
                local_max = j['i']
        max_all_costs.append(local_max)        
    length = max(max_all_costs)


    fig, ax = plt.subplots()
    ax.axis([0, max_i, 3000, length])
    ax.set_xlabel('Aantal geruilde connecties')
    ax.set_ylabel('Totale lengte van de kabels')

    
    
    colour = ['blue', 'green', 'red', 'gold', 'magenta']
    c = 0
    for s in all_districts:
        x = 0
        x_values = []
        y_values = []
        for t in s.improvements:
            y_values.append(t['i'])
            x_values.append(x)
            x +=1
        plt.plot(x_values, y_values, color=colour[c])
        c += 1

    fig.savefig('make-graph.png')