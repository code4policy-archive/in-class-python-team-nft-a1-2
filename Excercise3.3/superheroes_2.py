import csv
import json
import pprint

# Read superheroes.json
with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)

members = superheroes['members']

# Write a header to the CSV file
# Loop over the members, and for each member write a row to the csv file
with open('superheroes.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active'])
    for m in members:
        writer.writerow([m['name'],m['age'], m['secretIdentity'],m['powers'],superheroes['squadName'], superheroes['homeTown'], superheroes['formed'], superheroes['secretBase'],superheroes['active']])

