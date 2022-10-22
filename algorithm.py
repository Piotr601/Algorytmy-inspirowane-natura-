import random

# Class to solve a random problem
class Algorithm:
    
    # Algorithm to evaluate random city sequences
    def RandomAlgorithm(numb, matrix):
        dist = 0

        # Looking for random city sequence
        random_cities = random.sample(range(0,len(numb)), len(numb))
        random_cities.append(random_cities[0])
 
        # Finding the shortest path
        for index, item in enumerate(random_cities[:-1]):
            dist += matrix[item][random_cities[index+1]]

        # Returning sequence and total distance
        return random_cities, dist


    # Algorithm to evaluate greedy city sequences
    def GreedyAlgorithm(numb, matrix):
        dist = 0