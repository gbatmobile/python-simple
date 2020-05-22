# Esse programa mostra a situação de um número
# ele foi desenvolvido por gbat em abril/2019
# email gbatmobile at gmail com
#


x = int(input ("numero: "))
if x % 2 == 1:    # Testando se é impar
    print ("impar")
else:
    if x % 5 == 0:
        print ("par bonito")
    else:
        print ("par")

print ("fim")
