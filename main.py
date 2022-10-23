from audioop import cross
from loader import Loader
from algorithm import Algorithm, Crossover
from algorithm import Mutation, Evaluate
from problem import Problem


# Here is a variable to pick document
INPUT_NAME = 'berlin11_modified'

# EA Parameters
POP_SIZE = 100
GEN = 100
PX = 0.7
PM = 0.1
TOUR = 5

# Loading values from the file
'''
                              |      n - name         e - edge weight type
Numb - number of city         |      t - type        dd - display data type
x - coordinate x              |      c - comment
y - coordinate y              |      d - dimension
'''
numb, x, y = Loader.value_loader(f'TSP/{INPUT_NAME}.tsp')
n, t, c, d, e, dd = Loader.info_loader(f'TSP/{INPUT_NAME}.tsp')

list_numb, dist_numb = [], []

# # Calculating matrix
# m = Problem.MatrixCalculation(numb, x, y)

# Random algorithm
# for i in range(0,20):
#     random_list, random_dist = Algorithm.RandomAlgorithm(numb, m)
#     list_numb.append(random_list)
#     dist_numb.append(random_dist)

# Greedy algorithm
# for i in range(0, len(numb)):
#    greedy = Algorithm.GreedyAlgorithm(i, numb, m)
# greedy = Algorithm.GreedyAlgorithm(0, numb, m)

# # Mutation swap operation
# swapping = Mutation.SwapMutation(numb)

# # Mutation inversion operation
# inversion = Mutation.InversionMutation(numb)

# # Ordered crossover operation
# ordered = Crossover.OrderedCrossover(numb, numb)

# # Partially Matched crossover operation
# crossover = Crossover.PartialyMatchedCrossover(numb, numb)

# # Tournament evaluate operation
# tournament = Evaluate.TournamentEvaluate(list_numb, 0, m)

# Generic algorithm

def GenericAlgorihm(numb, x, y):
    pop_vec, pop_dist = [], []
    t = 0
    m = Problem.MatrixCalculation(numb, x, y)

    for i in range(0,POP_SIZE):
        random_list, random_dist = Algorithm.RandomAlgorithm(numb, m)
        pop_vec.append(random_list)
        pop_dist.append(random_dist)

    #print(pop_vec)
    #print(pop_dist)
    for t in range(GEN):
        #print(t)
        pass
    

    


GenericAlgorihm(numb, x, y)