import random

    a = bool(random.getrandbits(1))
Choices = []

def choose ():
    x = random.choice(Choices)
    print(x)

def get_input():
    x = input('enter a choice(and click "q" to start): ')
    
    if x == "q":
        choose()
    else:
        Choices.append(x)
        get_input()

get_input()