"""
File for selecting enemies to farm with No GUI
"""
import random
import os
import enemies

#Used for cleaning the screen for the first time
os.system('cls' if os.name == 'nt' else 'clear')

mExit = False
while not mExit:

	print("'s' + Return for Seraphs")
	print("'r' + Return for Raids")
	print("'b' + Return for non-Raid enemies ")
	print("'q' + Return to quit")
	mQuit = input()

	if mQuit == 's' or mQuit == 'seraph':
		sExit = False
		os.system('cls' if os.name == 'nt' else 'clear')
		while not sExit:
			print(enemies.seraphs())
			print("'q' + Return to go back, Return to randomize")
			sQuit = input()
			if sQuit == 'q' or sQuit == 'quit':
				os.system('cls' if os.name == 'nt' else 'clear')
				sExit = True
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
	
	elif mQuit == 'r' or mQuit == 'raid':
		rExit = False
		os.system('cls' if os.name == 'nt' else 'clear')
		while not rExit:
			print(enemies.raids())
			print("'q' + Return to go back, Return to randomize")
			rQuit = input()
			if rQuit == 'q' or rQuit == 'quit':
				os.system('cls' if os.name == 'nt' else 'clear')
				rExit = True
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
	
	elif mQuit == 'b' or mQuit == 'boss':
		bExit = False
		os.system('cls' if os.name == 'nt' else 'clear')
		while not bExit:
			print(enemies.legend())
			print("'q' + Return to go back, Return to randomize")
			bQuit = input()
			if bQuit == 'q' or bQuit == 'quit':
				os.system('cls' if os.name == 'nt' else 'clear')
				bExit = True
			else:
				os.system('cls' if os.name == 'nt' else 'clear')

	elif mQuit == 'q' or mQuit == 'quit':
		mExit = True
		os.system('cls' if os.name == 'nt' else 'clear')
	



