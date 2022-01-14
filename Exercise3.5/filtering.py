# Read output/vegetables.csv into a variable called vegetables.

import csv
import json
import pprint

with open('output/vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

#vegetables = [
# {"name": "eggplant", "color": "purple"},
# {"name": "tomato", "color": "red"},
# {"name": "corn", "color": "yellow"},
# {"name": "okra", "color": "green"},
# {"name": "arugula", "color": "green"},
# {"name": "broccoli", "color": "green"},
#]

# Loop through vegetables and filter down to only green vegtables using a whitelist.
green_veggies = []
color_list = ['green']
for v in vegetables:
    if v['color'] in color_list:
        green_veggies.append(v)

# Print veggies to the terminal
print(green_veggies)

# Write the veggies to a json file called output/greenveggies.json
with open('output/greenveggies.json', 'w') as f:
    json.dump(green_veggies, f)

# Bonus: Output another csv called output/green_vegetables.csv.
with open('output/greenveggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color'])
    for v in green_veggies:
    	writer.writerow([v['name'], v['color']])