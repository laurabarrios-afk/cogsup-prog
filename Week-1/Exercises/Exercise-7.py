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
    highLimit = 100 #Stablishes limits for the random number generator
    lowLimit = 1

    def greater(): #Provides a way of knowing if the number is higher or lower
        print("If the number is greater press g, if it's lower press l")
        great=input()
        if great=="g":
            return True
        else:
            return False
    
    correct = False #Sets incorrect as default until the user indicates that the answer is right

    while not correct:
        guess = randint(lowLimit, highLimit) 
        print("Is your number " + str(guess) + "? (y = correct / n = incorrect) ")
        number=input()
        if number == 'y':
            print("I guessed it!")
            correct = True
        elif greater(): #If the number is not correct and is greater, the random generator range will start with guess+1
            lowLimit=guess+1
        else: #If the number is lower, the random generator range will finish with guess-1
            highLimit=guess-1 
        