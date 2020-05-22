import random
MIN = 1
MAX = 1000
MAXTENT = 6

numtent = 0
guess = -1
num = random.randint(MIN, MAX)

while (numtent < MAXTENT) and (guess != num):
    print (f"O numero está entre {MIN} e {MAX}")
    guess = int (input ("Qual o número: "))
    numtent += 1
    if num == guess:
        print (f"PARABÉNS você acertou. O número é {guess}!!!")
    else:
        if guess > num:
            MAX = guess
        else:
            MIN = guess

if num != guess:
    print (f"LAMENTO, você não acertou. O número era {num}!!!")