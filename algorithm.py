import random
import logging
import numpy as np
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
        arr = np.copy(numb)
        # Draw a two elements to swap
        elem = random.sample(range(0,len(numb)), 2)
        # Swapping values
        arr[elem[0]], arr[elem[1]] = arr[elem[1]], arr[elem[0]]
        return arr


    # Function to inverse a random range
    def InversionMutation(numb):
        new_arr = []
        # Finding a two boundary items to swap
        elem = random.sample(range(len(numb)), 2)
        elem.sort()

        # Replacing items in array basic on elem values
        for pos, item in enumerate(numb):
            # If items in numb are in set
            if pos >= elem[0] and pos <= elem[1]:
                new_arr.append(str(numb[elem[1] + elem[0] - pos]))
            # Other values (not changed)
            else:
                new_arr.append(item)

        return new_arr


# Class to cross two objects into one
class Crossover:
    
    # Function to calculate OX crossover
    def OrderedCrossover(numb, sec_numb):
        # Define variables
        cities = numb.copy()
        cities2 = sec_numb.copy()[::-1]
        arr = []

        # Finding two random numbers
        elem = random.sample(range(len(numb)), 2)
        elem.sort()

        # Looking for left length and cities core
        left_len = len(cities[:elem[0]])
        cities = cities[elem[0]:elem[1]]

        # Removing repeat cities
        for item in cities:
            cities2.remove(item)

        # Adding cities to the left
        for i in range(left_len):
            arr.append(cities2[0])
            cities2.pop(0)
            
        # Adding cities to the right
        arr += cities + cities2

        # Converting array to float
        arr_float = [round(float(i)) for i in arr]

        # Checking if all value are correct (not missing)
        if sum(arr_float) != (int(len(numb))*int(len(numb)+1))/2:
            logging.error("Problem with Crossover, values doesn't agree")
            return False
        else:
            return arr


    # Class to calculate PMX crossover
    def PartialyMatchedCrossover(numb, sec_numb):
        cities = numb.copy()
        cities2 = sec_numb.copy()

        while True:
            # Finding two random numbers
            elem = random.sample(range(len(numb)), 2)
            elem.sort()

            # Part a whole array
            p1 = cities[elem[0]:elem[1]]
            p2 = cities2[elem[0]:elem[1]]

            # Changing items in value
            for pos, item in enumerate(cities):
                if item in p2:
                    a = p2.index(item)
                    cities[pos] = p1[a]

            # Replacing crossing values 
            cities[elem[0]:elem[1]] = p2

            # Converting array to float
            arr_float = [round(float(i)) for i in cities]

            # Checking if all value are correct (not missing)
            if sum(arr_float) == (int(len(numb))*int(len(numb)+1))/2:
                return cities


# Class to evaluate in EA
class Evaluate:

    # Function to create a tournament
    def TournamentEvaluate(list_numb, size, matrix):
        # Define variables
        best_val = float('inf')
        best_numb = []
        new_l = []
        rand = random.sample(range(len(list_numb)), size)
        
        # Selecting random arrays
        for item in rand:
            new_l.append(list_numb[item])

        # Counting distance
        for item in new_l:
            dist = 0

            for index, in_item in enumerate(item[:-1]):
                dist += matrix[in_item][item[index+1]]

            best_val = min(best_val, dist)
            if best_val == dist:
                best_numb = item

        return best_numb
    

    # Function to create a roulette
    def RouletteEvaluate():
        pass
