"""
blah blah fill this later
"""
import random

def seraphs():
	seraphs = ['Master Gee the Invincible', 
		'Hyperious the Invincible', 
		'Pete the Invincible', 
		'Voracidous the Invincible', 
		'Ancient Dragons of Destruction']
	return(random.choice(seraphs))

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

while True:
	print("Press Return to Randomize")
	print(" ")
	print("Seraph Boss")
	print(seraphs())

	print(" ")
	print("Raid Boss")
	print(raids())

	print(" ")
	print("Re-killable Enemy")
	print(legend())

	print("-------------------------")

	input()




















