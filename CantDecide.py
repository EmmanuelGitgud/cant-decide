import random

def decide(i,b):
    a = bool(random.getrandbits(1))
    if a == True:
        a = i
    else:
        a = b
    print(f"\n{i} or {b} = {a}")

def get_input():
    global choice1, choice2
    choice1 = input("enter first parameter: ")
    choice2 = input("enter second parameter: ")

get_input()
decide(choice1, choice2)
    