import json
import csv
from collections import defaultdict

# read geojson file
jsonFile = open('NYC_NTA.geojson', "r+")
data = json.load(jsonFile)


# read match file and create a dictionary
columns = defaultdict(list)		# each value in each columns is appended to a list

with open('match.csv') as f:
	reader = csv.DictReader(f)	# read rows into a dictionary format
	for row in reader:
		for (k,v) in row.items():
			columns[k].append(v)
match = {}						# initialize a dictionary
for i in xrange(len(columns['NTA'])):
	match[columns['NTA'][i]] = columns['DNAmatch'][i]


# convert filename's format
for item in match:
	L = match[item].split(',')
	temL = []
	for each in L:
		each = each.lower()
		each = each.replace(' (', '-')
		each = each.replace(' / ', '-')
		each = each.replace('/ ', '-')	
		each = each.replace(' ', '-')
		each = each.replace('\'','')
		if each == 'bedford-park-':			# corner case
			each = each[:-1]
		if len(each) != 0:
			each += '_poly.geojson'
		else:
			each += 'NONE'
		temL.append(each)
	match[item] =  ', '.join(temL)

# output data into a new geojson file
for feature in data['features']:
	if feature['properties']['NTAName'] in match:
		feature['properties']['GeoJsonFile'] =  match[feature['properties']['NTAName']]

output = open('output.geojson', "w")
output.write(json.dumps(data))



