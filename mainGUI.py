"""
Created Using EasyGUI
"""

import random
import easygui
import enemies

easygui.msgbox("""
	'Seraphs' is Seraph Guardians
	'Raid Bosses' is for all Raid Bosses, including Seraph Guardians
	'Legendaries' is all other farmable enemies, including bosses
	""")

mExit = False
while not mExit:

	mQuit = easygui.buttonbox('Select an Enemy Type', 'Main Menu', ('Seraphs', 'Raid Bosses', 'Legendaries', 'Quit'))
	if mQuit == 'Quit':
		mExit = True
	elif mQuit == 'Seraphs':
		sExit = False
		while not sExit:
			sQuit = easygui.buttonbox(enemies.seraphs(), 'Seraphs', ('Reroll', 'Back'))
			if sQuit == 'Back':
				sExit = True
	elif mQuit == 'Raid Bosses':
		rExit = False
		while not rExit:
			rQuit = easygui.buttonbox(enemies.raids(), 'Raid Bosses', ('Reroll', 'Back'))
			if rQuit == 'Back':
				rExit = True
	elif mQuit == 'Legendaries':
		lExit = False
		while not lExit:
			lQuit = easygui.buttonbox(enemies.legend(), 'Legendaries', ('Reroll', 'Back'))
			if lQuit == 'Back':
				lExit = True
	else:
		print('You shouldn\'t get here')
			







