import matplotlib.pyplot as plt
import numpy as np


def make_district(district):
    
    batteries = district.get_batteries()
    houses = district.get_houses()

    fig, ax = plt.subplots()
    ax.axis([-1, 51, -1, 51])
    bx = list(battery.x_grid for battery in batteries)
    by = list(battery.y_grid for battery in batteries)
    ax.plot([bx], [by], 'ro')

    hx = list(house.x_grid for house in houses)
    hy = list(house.y_grid for house in houses)
    ax.plot([hx], [hy], 'g+') 
    
    ax.set_xticks(np.arange(0, 51, 5))
    ax.set_yticks(np.arange(0, 51, 5))
    ax.set_xticks(np.arange(0, 51, 1), minor=True)
    ax.set_yticks(np.arange(0, 51, 1), minor=True)
    ax.minorticks_on()
    ax.tick_params(which='minor', grid_alpha=0.5)
    ax.grid(True, which='both')

    all_colors = ['black', 'yellow', 'blue', 'green', 'red']
    i = 0
    for battery in district.batteries:
        color = all_colors[i]
        for house in battery.connected_houses:
            x_values = []
            y_values = []
            for point in house.cable_points:
                cxy = point.split(",")
                cx = int(cxy[0])
                cy = int(cxy[1])
                x_values.append(cx)
                y_values.append(cy)
            plt.plot(x_values, y_values, color=color)
        i = i+1    
    
    visual_district = fig.savefig('visual_district.png')   

    return visual_district