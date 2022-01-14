import csv
import json
import pprint

# Reads superheroes.json (in this folder)

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)
    
#print(superheroes)

# Creates an empty array called powers
member_powers = []

# Loop thorough the members of the squad, and
 # append the powers of each to the powers array.
members = superheroes['members']

#print(members)

for m in members:
	powers = m['powers']
	member_powers = member_powers + m['powers']

member_powers = list(set(member_powers))

print(member_powers)


# Prints those powers to the terminal