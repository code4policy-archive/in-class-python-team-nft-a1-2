# Create CSV file
import csv
import pprint
import json

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

with open('output/vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color'])
    for v in vegetables:
      writer.writerow([v['name'], v['color']])


# Read output/vegetables.csv (see previous section) into a variable called vegetables.
# Print the variable vegetables.
import csv
import pprint

with open('output/vegetables.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)
    print(vegetables)

# Write vegetables as a JSON file called output/vegetables.json. It should look like this:

# [
#   { "name": "eggplant", "color": "purple" },
#   { "name": "tomato", "color": "red" },
#   { "name": "corn", "color": "yellow" },
#   { "name": "okra", "color": "green" },
#   { "name": "arugula", "color": "green" },
#   { "name": "broccoli", "color": "green" }
# ]
with open('output/vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=1)
