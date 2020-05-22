#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      Euler Project - Problem 706
#
# Author:      GBat
#
# Created:     30/03/2020
# Copyright:   (c) Galileu Batista 2020
#-------------------------------------------------------------------------------

baseTots = {(4,0,0): 4, (0,3,0): 3, (0,0,3): 3}

print (baseTots)

def genNewKey(key, offset):
    newKey = [0, 0, 0]
    for k in range(3):
        newKey[(k+offset)%3] = key[k]
    return tuple(newKey)

def jointDicts (newTots, baseTots):
    for k in baseTots:
        newTots[k] += baseTots[k]

def getDiv3(tots):
    tot = 0
    for k in tots:
        if (k[0] != 0) and (sum(k[1:]) == 0):
            tot += tots[k]
    return tot

tots = baseTots
print ("SUM: ", getDiv3(tots))

for q in range (2, 6):
    newTots = {}
    for dig in range(1, 10):
        for key in tots:
            newKey = genNewKey(key, dig % 3)
            newTots[newKey] = newTots.get(newKey, 0) + tots[key]
    print ("Valores previos com ", q, 'digitos:', newTots, '-->', sum(newTots.values()))
    jointDicts (newTots, tots)
    tots = newTots
    print ("Valores com ", q, 'digitos:', tots, '-->', sum(tots.values()))
    print ("SUM: ", getDiv3(tots))