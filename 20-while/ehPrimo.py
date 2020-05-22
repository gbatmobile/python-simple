ndiv = 0
n = 1
while n <= p:

    if p%n == 0:
        ndiv = ndiv + 1
        print (n)

    n = n + 1

if ndiv == 2:
    print (p, "é primo")
