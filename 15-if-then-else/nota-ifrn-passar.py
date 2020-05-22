# Questao 10 - Lista 1

t1 = float (input("Nota do trabalho1: "))
p1 = float (input("Nota dq prova1: "))
t2 = float (input("Nota do trabalho2: "))

notaU1 = 0.3*t1 + 0.7*p1

p2 = ((6 - notaU1*0.4)/0.6 - t2*0.3)/0.7

if p2 <= 10:
    print ("A nota minina na prova2 é:", p2)
else:
    print ("Você está reprovado!!!")