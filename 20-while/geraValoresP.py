
p = 1

while p <= 1000:

    ndiv = 0
    n = 1
    while n <= p:

        if p%n == 0:
            ndiv = ndiv + 1

        n = n + 1

    if ndiv == 2:
        print (p, "é primo")


    p = p + 1
