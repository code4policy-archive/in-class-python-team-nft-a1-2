import csv
vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

with open('vegetables.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color', 'length name'])
    for v in vegetables:
    	writer.writerow([v['name'], v['color'], len(v['name'])])