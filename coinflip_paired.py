#Coin flip simulation.py
"""
 Write some code that simulates flipping a single coin 
 however many times the user decides. The code should 
 record the outcomes and count the number of tails and heads.

"""
from random import randint

inputa = int(input("Insert how many coin flips you want:\n>>> "))
h_h=0
h_t=0
t_h=0
t_t=0


for i in range(inputa):
    c_one = randint(0,1)
    c_two = randint(0,1)
    print(str(c_one) +''+ str(c_two), end='.')
    if c_one == 1 and c_two == 1: #Tails = 0, heads = 1
        h_h += 1
    elif c_one == 1 and c_two == 0:
        h_t += 1
    elif c_one == 0 and c_two == 1:
        t_h += 1
    elif c_one == 0 and c_two == 0:
        t_t += 1

print('\n\nLegend:\n0 = Tails\n1 = Heads')

print('\n\nThere are:\n{} Headhead\n{} headtail\n{} tailhead\n{} tailtail'.format(h_h,h_t,t_h,t_t))

input("\n\nPress enter to exit\n")