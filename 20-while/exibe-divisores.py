n = 1
while n <= 10000:
    ########################################
    #   calcular a soma dos divisores de n #
    ########################################
    s = 0
    d = 1
    while d < n:
        if n % d == 0:
            s = s + d
        d = d + 1

    print ("A soma dos divisores de ",n, "eh", s)
    n = n + 1