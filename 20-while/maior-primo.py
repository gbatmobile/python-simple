n = 1
maior = 2
soma = 0
while n <= 1000:
    ndiv = 0
    div = 1
    while div <= n:
        if n % div == 0:
            ndiv = ndiv + 1
        div = div + 1
    if ndiv == 2:
        maior = n
        soma = soma + n
    n = n + 1
print ("O maior primo é:", maior)
print ("A soma é:", soma)
