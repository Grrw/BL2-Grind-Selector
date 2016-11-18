"""
blah blah fill this later
"""
import random
import os

# Used for cleaing the screen for the first time
os.system('cls' if os.name == 'nt' else 'clear')

# List all Seraph Bosses
def seraphs():
	seraphs = ['Master Gee the Invincible', 
		'Hyperious the Invincible', 
		'Pete the Invincible', 
		'Voracidous the Invincible', 
		'Ancient Dragons of Destruction']
	return(random.choice(seraphs))

# List all Raid Bosses
def raids():
	raids = ['Terramorphous the Invincible', 
		'Vermivorous the Invincible', 
		'Hyperious the Invincible', 
		'Master Gee the Invincible', 
		'Pete the Invincible', 
		'Voracidous the Invincible', 
		'Dexiduous the Invincible', 
		'Ancient Dragons of Destruction']
	return random.choice(raids)

# List all other re-killable enemies
# This includes Bosses who are not Raids or Seraphs
def legend():
	legend = ["Bone Head 2.0",
		"Saturn",
		"DJ Hunter Hellquist",
		"Rat Brothers",
		"BNKR",
		"Badass Creepers",
		"Blue",
		"Black Queen",
		"Jimbo & Tector Hodunk",
		"McNally",
		"Mick Zaford",
		"Mobley",
		"Gettle",
		"Wilhelm",
		"King Mong",
		"Laney White",
		"Rakkman",
		"Smash Head",
		"Shorty",
		"Clayton",
		"Spycho",
		"Scorch",
		"Old Slappy",
		"Mad Dog",
		"Dukino's Mom",
		"Sherrif Of Lynchwood",
		"Foreman",
		"Fatty Enemies",
		"Mortar",
		"Boom & Bewm",
		"Captain Flynt",
		"Midgemong",
		"The Four Assassins",
		"Boll",
		"Savage Lee",
		"Doc Mercy",
		"Madame Von Bartlesby",
		"The Warrior",
		"Pimon",
		"Son of Mothrakk",
		"Tumba",
		"Loot Midgets",
		"Knuckle Dragger"]
	return(random.choice(legend))


exit = False
while not exit:
	print(" ")
	print("Seraph Boss:")
	print(seraphs())

	print(" ")
	print("Raid Boss:")
	print(raids())

	print(" ")
	print("Re-killable Enemy:")
	print(legend())

	print("-------------------------")
	
	print("Press Return to randomize; 'quit' + Return to Quit")
	s = input()

	if s == 'quit' or s == 'q' or s == 'quit()' or s == 'exit':
		os.system('cls' if os.name == 'nt' else 'clear')
		exit = True
	else:
		os.system('cls' if os.name == 'nt' else 'clear')




