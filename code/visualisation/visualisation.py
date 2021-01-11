import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def make_district(district):
    
    batteries = district.get_batteries()
    houses = district.get_houses()

    fig, ax = plt.subplots()
    ax.axis([-1, 51, -1, 51])
    bx = list(battery.get_x() for battery in batteries)
    by = list(battery.get_y() for battery in batteries)
    ax.plot([bx], [by], 'ro')

    hx = list(house.get_x() for house in houses)
    hy = list(house.get_y() for house in houses)
    ax.plot([hx], [hy], 'g+') 
    
    ax.set_xticks(np.arange(0, 51, 5))
    ax.set_yticks(np.arange(0, 51, 5))
    ax.set_xticks(np.arange(0, 51, 1), minor=True)
    ax.set_yticks(np.arange(0, 51, 1), minor=True)
    ax.minorticks_on()
    ax.tick_params(which='minor', grid_alpha=0.5)
    ax.grid(True, which='both')
    
    visual_district = fig.savefig('visual_district.png')   

    return visual_district