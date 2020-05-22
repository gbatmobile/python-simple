num = int (input("Digite um número: "))

if num >= 0:
    if num % 2 == 1:
        print ("É ímpar")

    if num % 2 == 0:
        print ("É par")

if num < 0:
    print ("O número dever ser positivo")