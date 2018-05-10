#Coin flip simulation.py
"""
 Write some code that simulates flipping a single coin 
 however many times the user decides. The code should 
 record the outcomes and count the number of tails and heads.

"""
from random import randint

inputa = int(input("Insert how many coin flips you want:\n>>> "))
tails=0
heads=0

for i in range(inputa):
	var = randint(0,1)
	print(var,end=',')
	if var == 0: #Tails = 0, heads = 1
		tails += 1
	elif var == 1:
		heads += 1


#deviation
print('\n\nThere are:\n{} tails and \n{} heads'.format(tails, heads))
deviation = ((abs((inputa/2) - tails) + abs((inputa/2) - heads))/inputa) * 100
print('There is a {}% deviation from the expected 1/2 tails and 1/2 heads'.format(deviation))

input("\n\nPress enter to exit\n")