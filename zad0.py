from curses.ascii import isalpha
import numpy as np

def loader(name):
    arr, x, y = [], [], []
    name = 'TSP/' + name + '.tsp'
    with open(name,'r') as data_file:
        for line in data_file:
            whole_line = line.split()
            if whole_line:
                # NAME, TYPE, COMMENT
                if whole_line[0].isupper():
                    pass
                # ARRAY DATA
                if whole_line[0].isnumeric():
                    arr.append(whole_line)
                    x.append(whole_line[1])
                    y.append(whole_line[2])
    return arr, x, y


def matrix(arr, x, y):
    print(x)
    print(y)
    #print(arr)

            

def main(): 
    arr, x, y = loader("berlin11_modified")
    matrix(arr, x, y)

if __name__ == "__main__":
    main()