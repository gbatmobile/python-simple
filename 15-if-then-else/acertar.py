import random
min = 1
max = 100
num = random.randint(min, max)
print ("O numero é", num)

guess = int (input ("Qual o número: "))
if num == guess:
    print ("PARABÉNS você acertou. O número é: ", guess)
else:
    if guess > num:
        max = guess
    else:
        min = guess
    print ("O numero está entre ", min, "e", max)

    guess = int (input ("Qual o número: "))
    if num == guess:
        print ("PARABÉNS você acertou. O número é: ", guess)
    else:
        if guess > num:
            max = guess
        else:
            max = guess
        print ("O numero está entre ", min, "e", max)
