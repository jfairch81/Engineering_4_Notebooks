# Automatic Dice Roller
# Written by Jude Fairchild

from random import randint

print ("Automatic Dice Roller") # Prints out the name of the game 
roll = True # Sets roll to a boolean to determine if the user wants to roll again

while roll: 
	i = str(input("Do you want to roll again?, enter for yes, x for no"))
	if i == "":
		print(randint(1,6)) # if yes, roll again 
	elif i == "x": 
		roll = False # if not set roll to false and write that the game is ending 
		print("Game Ending")
	else:
		print("Error, Please enter an x or enter") # if x or " " not end game
		run = False
	
	
