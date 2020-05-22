#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:      Euler Project - Problem 706
#
# Author:      GBat
#
# Created:     30/03/2020
# Copyright:   (c) Galileu Batista 2020
#-------------------------------------------------------------------------------


totfn = 0
for num in range(100, 1000):
    num = str(num)
    fn = 0
    for beg in range(0, len(num)):
        for end in range(beg, len(num)):
            val = int(num[beg:end+1])
            if val % 3 == 0:
                fn += 1
    if fn % 3 == 0:
        print (num, end = ' ')
        totfn += 1
print ('\ntotfn ', totfn)