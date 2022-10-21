# Class to load values and info 
class Loader:
    # Method to save values    
    def value_loader(data):
        numb, arr, x, y = [], [], [], []

        # Saving values to arrays
        with open(data) as data_file:
            for line in data_file:
                whole_line = line.split()
                if whole_line:
                    if whole_line[0].isnumeric():
                        arr.append(whole_line)
                        numb.append(whole_line[0])
                        x.append(whole_line[1])
                        y.append(whole_line[2])

        return arr, numb, x, y


    # Method to save information
    def info_loader(data):
        # If there is no info, variables take None
        NAME = None
        TYPE = None
        COMMENT = None
        DIMENSION = None
        EDGE = None
        DISPLAY = None

        # Saving info to variables
        with open(data) as data_file:
            for line in data_file:
                whole_line = line.split()
                if whole_line:
                    if whole_line[0] == 'NAME:':
                        NAME = whole_line[1]
                    if whole_line[0] == 'TYPE:':
                        TYPE = whole_line[1]
                    if whole_line[0] == 'COMMENT:':
                        COMMENT = whole_line[1:]
                    if whole_line[0] == 'DIMENSION:':
                        DIMENSION = whole_line[1]
                    if whole_line[0] == 'EDGE_WEIGHT_TYPE:':
                        EDGE = whole_line[1]
                    if whole_line[0] == 'DISPLAY_DATA_TYPE:':
                        DISPLAY = whole_line[1]
        return NAME, TYPE, COMMENT, DIMENSION, EDGE, DISPLAY