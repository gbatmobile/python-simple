#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      Euler Project - Problem 706
#
# Author:      GBat
#
# Created:     30/03/2020
# Copyright:   (c) Galileu Batista 2020
#-------------------------------------------------------------------------------
import copy

NUM = 1000
base = [[0, 4, 0], [3, 3, 0], [4, 2, 0], [3, 1, 0] ]
basediv3 = [6, 4, 0]

for d0 in range (1, 10):
    for d1 in range (1, 10):
        for d2 in range (1, 10):
            b3 = copy.deepcopy(base[3])
            for d3 in range (0, 10):
                if basediv3[0] % 3 == 0:
                    print (d0, d1, d2, d3)

                basediv = [basediv3[0] - b3[0], basediv3[1] - b3[1], basediv3[2] - b3[2]]
                b3 = [b3[2], b3[0], b3[1]]
                basediv = [basediv3[0] + b3[0], basediv3[1] + b3[1], basediv3[2] + b3[2]]


print (NUM, tots)
dig = 0

for num in range(NUM+1, NUM+100):
    if num % 10 == 0:
        tots[1] = [tots[1][2], tots[1][0], tots[1][1]]
        tots[0][0] -= 1
        tots[0] = [tots[0][2], tots[0][0], tots[2][1]]
        tots[0][0] += 1
    else:
        tots[0] = [tots[0][2], tots[0][0], tots[0][1]]

    if (tots[0][0]+ tots[1][0]+ tots[2][0]) % 3 == 0:
        print (num, tots )
