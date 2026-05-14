import numpy as np
import matplotlib.pyplot as plt
from population import get_population

hog_weight = 120 # lb
consumption_rate = 0.065
times, populations = get_population()
crop_density = 6720 # lb/acre
crop_area = 2e6 # acres
crop_growth = 0.002 # per day

def agriculture_area():
    weights = populations * hog_weight
    areas = np.zeros(len(weights))
    for i in range(len(weights)):
        if i == 0:
            areas[i] = crop_area
        else:
            areas[i] = (areas[i - 1] - weights[i] * consumption_rate / crop_density + crop_growth * (crop_area - areas[i - 1])) 
        areas[i] = np.clip(areas[i], 0, crop_area)
    return areas    

def plot_areas():
    areas = agriculture_area()
    plt.xlabel("time")
    plt.ylabel("area")
    plt.grid()
    plt.title("Agricultural area vs time")
    plt.plot(times, areas)
    plt.savefig("agriculture.png")
    plt.show()

def main():
    plot_areas()

main()

    