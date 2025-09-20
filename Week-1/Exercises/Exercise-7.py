"""
Have a look at the script called 'human-guess-a-number.py' (in the same folder as this one).

Your task is to invert it: You should think of a number between 1 and 100, and the computer 
should be programmed to keep guessing at it until it finds the number you are thinking of.

At every step, add comments reflecting the logic of what the particular line of code is (supposed 
to be) doing. 
"""
from random import randint

print("Think of a number between 1 and 100. I will try to guess it \n Press s to start") 
start=input()
if start=="s":
    highLimit = 100
    lowLimit = 1

    def greater():
        print("If the number is greater press g, if it's lower press l")
        great=input()
        if great=="g":
            return True
        else:
            return False
    
    correct = False

    while not correct:
        guess = randint(lowLimit, highLimit)
        print("Is your number " + str(guess) + "? (y = correct / n = incorrect) ")
        number=input()
        if number == 'y':
            print("I guessed it!")
            correct = True
        elif greater():
            lowLimit=guess+1
        else:
            highLimit=guess-1
        