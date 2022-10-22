import random
import numpy as np
import math

# Class to give a problem matrix - distance
class Problem:
    
    # Function to create and returning matrix with distance between cities
    def MatrixCalculation(numb,x,y):
        matrix = np.zeros((len(numb), len(numb)), dtype=float)

        for i in range(len(numb)):
            for j in range(len(numb)):
                if i != j:
                    # Euclidean metric in two dimensions
                    x_axis = float(x[j]) - float(x[i])
                    y_axis = float(y[j]) - float(y[i])
                    metric = math.sqrt(pow(x_axis,2) + pow(y_axis,2))

                    matrix[i][j] = round(metric, 2)

        return matrix