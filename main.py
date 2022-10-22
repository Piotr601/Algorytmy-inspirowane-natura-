from loader import Loader
from algorithm import Algorithm, Crossover
from algorithm import Mutation
from problem import Problem


# Here is a variable to pick document
INPUT_NAME = 'berlin11_modified'

# Loading values from the file
'''
arr - combine [numb, x, y]    |      n - name         e - edge weight type
Numb - number of city         |      t - type        dd - display data type
x - coordinate x              |      c - comment
y - coordinate y              |      d - dimension
'''
arr, numb, x, y = Loader.value_loader(f'TSP/{INPUT_NAME}.tsp')
n, t, c, d, e, dd = Loader.info_loader(f'TSP/{INPUT_NAME}.tsp')

# Calculating matrix
m = Problem.MatrixCalculation(numb, x, y)

# # Random algorithm
# random = Algorithm.RandomAlgorithm(numb, m)

# # Greedy algorithm
# #for i in range(0, len(numb)):
# #    greedy = Algorithm.GreedyAlgorithm(i, numb, m)
# #    print(greedy)
# greedy = Algorithm.GreedyAlgorithm(0, numb, m)

# # Mutation swap operation
# swapping = Mutation.SwapMutation(numb)

# # Mutation inversion operation
# inversion = Mutation.InversionMutation(numb)

# # Ordered crossover operation
# ordered = Crossover.OrderedCrossover(numb, numb)

# # Partially Matched crossover operation
print(Crossover.PartialyMatchedCrossover(numb, numb))