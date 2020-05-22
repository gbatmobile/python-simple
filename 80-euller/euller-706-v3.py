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

tots   = {1: [4, 3, 3] }
newDig = [3, 3, 3]

print (tots)


def genNew (new):
    newTots = [3, 3, 3]  # Novo digito sozinho
    for prev in range(1, new):
        newTots = sumList(newTots, tots[prev])


    return [9 * tots[atual][2], 9 * tots[atual][0], 9 * tots[atual][1]]

def sumList (l1, l2):
    print ('l1', l1)
    print ('l2', l2)
    l3 = [0,0,0]
    for i in range(3):
        l3[i] = l1[i] + l2[i]
    print ('l3', l3)
    return l3

tots[2] = {2: genNew(1)}
print ('tots', tots)
