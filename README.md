# GeneticAlgorithm

Based on 
https://en.wikipedia.org/wiki/Genetic_algorithm

This algorithm was implemented with:
- 2 types of crossover (OX, PMX)
- 2 types of mutation (swap, inversion)
- one evaluate method (tournament)

### Input Format:
- Optional inputs:

  _NAME, TYPE, COMMENT, EDGE_WEIGHT_TYPE, NODE_COORD_SECTION, _DIMENSION__

- Required inputs:
  
  (int, float, float)
  
  _No. city, x_coordinate, y_coordinate_

More on Data Example

### Output:
- The shortest distance through all points path

### Requirements:
- Python 3.x
- Numpy
- Random
- CSV

### Data Example
```
NAME: berlin52
TYPE: TSP
COMMENT: 11 locations selected from berlin52
DIMENSION: 11
EDGE_WEIGHT_TYPE: EUC_2D
NODE_COORD_SECTION
1 565.0 575.0
2 25.0 185.0
3 345.0 750.0
4 945.0 685.0
5 845.0 655.0
6 880.0 660.0
7 25.0 230.0
8 525.0 1000.0
9 580.0 1175.0
10 650.0 1130.0
11 1605.0 620.0 
EOF
```
