import random
from unicodedata import unidata_version

# Class to solve a random problem
class Algorithm:
    
    # Algorithm to evaluate random city sequences
    def RandomAlgorithm(numb, matrix):
        dist = 0

        # Looking for random city sequence
        random_sequence = random.sample(range(0,len(numb)), len(numb))
 
        # Finding the shortest path
        for index, item in enumerate(random_sequence[:-1]):
            dist += matrix[item][random_sequence[index+1]]

        # Returning sequence and total distance
        return random_sequence, dist


    # Algorithm to evaluate greedy city sequences
    def GreedyAlgorithm(city, numb, matrix):
        # Declaring values
        first_city = city
        sequence = [city + 1]
        dist = 0
        
        # Copying matrix and unvisited cities
        unvisited_cities = numb.copy()
        unvisited_cities.pop(city)

        # When algorithm dont visit in all cities
        while unvisited_cities:
            short = float('inf')

            # For each city (which are not visited)
            for item in unvisited_cities:
                # Looking for min value of each connection
                val = matrix[city][int(int(item)-1)]
                short = min(short, val)
                # Looking for number of city (with best result)
                if val == short:
                    city_to_remove = int(item)

            # Calculating distance, adding city to sequence
            dist += short
            sequence.append(city_to_remove)
            # Removing values from unvisited cities, replacing city val
            unvisited_cities.remove(str(city_to_remove))
            city = city_to_remove - 1

        # Calculating all distance (from 1st_city to 1st_city)
        dist_to_first = dist + matrix[city][first_city]

        # Returning sequence and distance
        return sequence, dist_to_first
        