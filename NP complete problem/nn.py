"""
In this assignment we will revisit an old friend, the traveling salesman problem (TSP). This week you will implement a heuristic for the TSP, rather than an exact algorithm, and as a result will be able to handle much larger problem sizes. Here is a data file describing a TSP instance (original source: http://www.math.uwaterloo.ca/tsp/world/bm33708.tsp).
nn.txt
The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.
...
Repeatedly visit the closest city that the tour hasn't visited yet. In case of a tie, go to the closest city with the lowest index. For example, if both the third and fifth cities have the same dist_square from the first city (and are closer than any other city), then the tour should begin by going from the first city to the third city.
Once every city has been visited exactly once, return to the first city to complete the tour.
In the box below, enter the cost of the traveling salesman tour computed by the nearest neighbor heuristic for this instance, rounded down to the nearest integer.
[Hint: when constructing the tour, you might find it simpler to work with squared Euclidean dist_squares (i.e., the formula above but without the square root) than Euclidean dist_squares. But don't forget to report the length of the tour in terms of standard Euclidean dist_square.]
"""

import csv as csv
from math import sqrt

f = open('week3/nn.txt');
reader = csv.reader(f,delimiter=' ', quoting=csv.QUOTE_NONE)

G = {}
number_of_cities = int(next(reader, None)[0])

for row in reader:
    index = int(row[0])
    x = float(row[1])
    y = float(row[2])
    G[index]=[]
    G[index].append(x)
    G[index].append(y)

city = 1
first_city_x = G[city][0]
first_city_y = G[city][1]
mileage = 0

while len(G)>0:
    x = G[city][0]
    y = G[city][1]
    del G[city]
    min_dist_square = float("inf")
    min_index = 0
    for c in G:
        dist_square = (G[c][0]-x) ** 2 + (G[c][1]-y) ** 2
        if dist_square < min_dist_square:
            min_index = c
            min_dist_square = dist_square

    #Travel to next city
    if (min_index != 0):
        mileage += sqrt(min_dist_square)
        city = min_index
        #print str(city)+' : ' +str(sqrt(min_dist_square))

    #Back to the first city
    else:
        min_dist_square = (x-first_city_x) ** 2 + (y-first_city_y) ** 2
        mileage += sqrt(min_dist_square)
        print '1 : ' +str(sqrt(min_dist_square))

print mileage
#answer: 1203406