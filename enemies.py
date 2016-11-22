"""
List of all enemies for easy reading purposes
"""
import random

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

def all():
	all = ['Terramorphous the Invincible', 
		'Vermivorous the Invincible', 
		'Hyperious the Invincible', 
		'Master Gee the Invincible', 
		'Pete the Invincible', 
		'Voracidous the Invincible', 
		'Dexiduous the Invincible', 
		'Ancient Dragons of Destruction',
		"Bone Head 2.0",
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
	return(random.choice(all))
				
