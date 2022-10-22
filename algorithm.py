import random
from unicodedata import unidata_version

# Class to solve a TSP problem
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
        return random_sequence, round(dist,2)


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
        return sequence, round(dist_to_first,2)


# Class to changing items in sequence 
class Mutation:

    # Function to swap random values
    def SwapMutation(numb):
        # Copying numb lists
        arr = numb.copy()
        # Draw a two elements to swap
        elem = random.sample(range(0,len(numb)), 2)
        # Swapping values
        arr[elem[0]], arr[elem[1]] = arr[elem[1]], arr[elem[0]]
        return arr


    # Function to inverse a random range
    def InversionMutation(numb):
        new_arr = []
        # Finding a two boundary items to swap
        elem = random.sample(range(1,len(numb)+1), 2)
        elem.sort()
        
        # Replacing items in array basic on elem values
        for item in numb:
            # If items in numb are in set
            if int(item) >= elem[0] and int(item) <= elem[1]:
                new_arr.append(str(elem[1] + elem[0] - int(item)))
            # Other values (not changed)
            else:
                new_arr.append(item)

        return new_arr


# Class to cross two 
class Crossover:
    pass