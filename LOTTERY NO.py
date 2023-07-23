#Write a program to generate random numbers between 1 to 6 and check whether a user won a lottery or not

import random
while(True):
    choice=input("ENTER(r) FOR DICE -")
    if(choice != 'r'):
        break
    n = random.randint(1,6)
    print(n)
