import numpy as np

class Loader:
    NAME = ''
    TPYE = ''
    COMMENT = ''
    DIMENSION = ''
    EDGE_WEIGHT_TYPE = ''
    DISPLAY_DATA_TYPE = ''
    NODE_COORD_SECTION = ''

    def loader(name):
        numb, arr, x, y = [], [], [], []
        name = 'TSP/' + name + '.tsp'

        with open(name,'r') as data_file:
            for line in data_file:
                whole_line = line.split()
                print(type(whole_line))
                if whole_line:
                    # NAME, TYPE, COMMENT
                    if whole_line[0].isupper():
                        if whole_line: 
                            print('damn')
                    # ARRAY DATA
                    if whole_line[0].isnumeric():
                        arr.append(whole_line)
                        numb.append(whole_line[0])
                        x.append(whole_line[1])
                        y.append(whole_line[2])
        return arr, numb, x, y


    def matrix(arr, numb, x, y):
        print(x)
        print(y)
        #print(arr)

        for i in range(len(x)):
            #print(i)
            pass

                
                

def main(): 
    load = Loader
    arr, numb, x, y = load.loader("berlin11_modified")
    load.matrix(arr, numb, x, y)

if __name__ == "__main__":
    main()