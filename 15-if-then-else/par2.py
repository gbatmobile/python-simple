num = int (input("Digite um número: "))

if num >= 0:
    if num % 2 == 1:
        print ("É ímpar")
    else:
        print ("É par")
else:
    print ("O número dever ser positivo")