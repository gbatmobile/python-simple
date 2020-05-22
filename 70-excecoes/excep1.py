def f():
    x = int (input("Numero: "))
    x1 = x**2
    return x1

def g():
    y = f() + 2
    return y

try:
    print (g())
except:
    print ("Numero errado")

