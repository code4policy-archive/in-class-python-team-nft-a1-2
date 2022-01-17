# Read vegtables.csv into a variable called vegtables.

import csv
import json
from pprint import pprint

with open('vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegtables = list(reader)

# Group vegtables by color as a variable vegtables_by_color.
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

vegtables_by_color = {}
for veg in vegetables:
    cc = veg['color']
    if cc in vegtables_by_color:
        vegtables_by_color[cc].append(veg)
    else:
        vegtables_by_color[cc] = [veg]

pprint(vegtables_by_color)

# Output vegtables_by_color into a json called vegtables_by_color.json
with open('vegtables_by_color.json', 'w') as f:
    json.dump(vegtables_by_color, f)