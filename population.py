import numpy as np
import matplotlib.pyplot as plt
import math
import csv

r = 0.21
K = 6365749
K0 = 2600000
year0 = 2026 # change to 2026 when running agriculture.py
year_final = 2076

def get_population():
    times = np.linspace(year0, year_final, 365 * (year_final - year0))
    populations = np.array([logistic(t) for t in times])
    return times, populations

def save_population_to_csv():
    times, populations = get_population()
    with open("population.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["time", "population"])
        for i in range(len(times)):
            writer.writerow([times[i], populations[i]])

def get_half_population():
    times, populations = get_population()
    for i in range(len(populations)):
        if populations[i] > K / 2 - 500 and populations[i] < K / 2 + 500:
            print(f"Time: {times[i]}, Population: {populations[i]}")
            return times[i], populations[i]
    return times[-1], populations[-1]

def graph_population():
    times, populations = get_population()
    plt.xlabel("time")
    plt.ylabel("population")
    plt.title("Hog population vs time")
    plt.plot(times, populations)
    plt.grid()
    plt.savefig("population.png")
    plt.show()

def logistic(t):
    return K / (1 + math.exp(-1 * r * (t - 2026)) * (K - K0) / K0)

def main():
    get_half_population()
    save_population_to_csv()
    graph_population()

main()