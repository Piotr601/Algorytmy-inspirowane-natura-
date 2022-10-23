from audioop import cross
import random
import csv
import numpy as np
from statistics import mean 
from loader import Loader
from algorithm import Algorithm, Crossover
from algorithm import Mutation, Evaluate
from problem import Problem


# Here is a variable to pick document
INPUT_NAME = 'gr666'

# EA Parameters
POP_SIZE = 150
GEN = 5000
PX = 70         # in %
PM = 20         # in %
TOUR = 8
HOW_MANY = 10

HOW_MANY_RANDOM = 50000

# Loading values from the file
#
# Numb - number of city         |      t - type        dd - display data type
# x - coordinate x              |      c - comment     e - edge weight type
# y - coordinate y              |      d - dimension   n - name
numb, x, y = Loader.value_loader(f'TSP/{INPUT_NAME}.tsp')
n, t, c, d, e, dd = Loader.info_loader(f'TSP/{INPUT_NAME}.tsp')

# Function to create a genetic algorithm
def GeneticAlgorihm(numb, x, y):

    # Saving items to CSV file
    f = open(f'CSV/{INPUT_NAME}.csv', 'w')
    writer = csv.writer(f)

    # Creating matrix
    m = Problem.MatrixCalculation(numb, x, y)

    # Define variables
    pop_vec, pop_dist = [], []
    best_val = float('inf')
    average_val = 0

    # Creating a population, distance values
    for i in range(0,POP_SIZE):
        random_list, random_dist = Algorithm.RandomAlgorithm(numb, m)
        pop_vec.append(random_list)
        pop_dist.append(random_dist)

    # Generations algorithm
    for i in range(GEN):

        # Moving into population
        for pos, item in enumerate(pop_vec):
            # Evaluating first parent
            parent1 = Evaluate.TournamentEvaluate(pop_vec, TOUR, m)
            child = parent1

            # Randomize values px and pm
            prop_px, prop_pm = random.sample(range(0,100), 2)

            # Crossover 
            if prop_px <= PX:
                parent2 = Evaluate.TournamentEvaluate(pop_vec, TOUR, m)
                child = Crossover.OrderedCrossover(child, parent2)

            # Mutation
            if prop_pm <= PM:
                child = Mutation.InversionMutation(child)

            # Saving child into population
            pop_vec[pos] = child

        worst_val = -1

        # Evaluating distance per each gen
        for i_item in pop_vec:
            start = i_item[0]
            dist = 0

            # Calculating distance + return to the starting city
            for index, in_item in enumerate(i_item):
                dist += m[in_item][i_item[index-1]]
            dist += m[i_item[index-1]][start]

            # Collect best/worst/average dsitance
            average_val += dist
            worst_val = max(dist, worst_val)
            best_val = min(best_val, dist)

        # Save distance to CSV file
        writer.writerow([best_val, worst_val, average_val/(GEN*len(pop_vec))])
    
    # Closing file
    f.close()
    # Returing variables
    return round(best_val,2), round(worst_val,2), round(average_val/(GEN*len(pop_vec)),2)


# Function to create a random algorithm
def RandomAlgorithm(numb, x, y):
    list_numb, dist_numb = [], []
    m = Problem.MatrixCalculation(numb, x, y)

    for _ in range(HOW_MANY_RANDOM):
        random_list, random_dist = Algorithm.RandomAlgorithm(numb, m)
        list_numb.append(random_list)
        dist_numb.append(random_dist)

    return min(dist_numb), max(dist_numb), round(mean(dist_numb),2)


# Function to create a greedy algorithm
def GredyAlgorithm(numb, x,y):
    greddy_arr = []
    m = Problem.MatrixCalculation(numb, x, y)

    for i in range(0, len(numb)):
        seq, greedy = Algorithm.GreedyAlgorithm(i, numb, m)
        greddy_arr.append(greedy)

    return min(greddy_arr), max(greddy_arr), round(mean(greddy_arr),2)
    

# Main function
if __name__ == "__main__":

    # Calling generic Algorithm
    # results = GeneticAlgorihm(numb, x, y)

    # Calling random Algorithm
    #results = RandomAlgorithm(numb, x, y)

    # Calling greddy Algorithm
    results = GredyAlgorithm(numb, x, y)
    print(results[0])
    print(results[1]) 
    print(results[2])


"""
Comments / Testing functions


# Mutation swap operation
swapping = Mutation.SwapMutation(numb)
print(numb)
print(swapping)

# Mutation inversion operation
inversion = Mutation.InversionMutation(numb)

# Ordered crossover operation
ordered = Crossover.OrderedCrossover(numb, numb)

# Partially Matched crossover operation
crossover = Crossover.PartialyMatchedCrossover(numb, numb)

# Tournament evaluate operation
tournament = Evaluate.TournamentEvaluate(list_numb, 200, m)
"""