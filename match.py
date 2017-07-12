import json
from pyproj import Proj, transform
from vincenty import vincenty

with open('NYC_NTA.geojson') as f:
    data = json.load(f)

DNA = open('neighborhood_centroids.csv')
DNAdata = []

# read DNA data
inProj = Proj(init='epsg:32118')
outProj = Proj(init='epsg:4326')
for line in DNA:
	tem = line.split(',')[1:]
	tem[-1] = tem[-1][:-2]
	tem[-2],tem[-1] = transform(inProj,outProj, float(tem[-2]), float(tem[-1]))		# convert espg
	DNAdata.append(tem)
DNAdata[-1][-1] = '67742.31183'
DNAdata[-1][-2], DNAdata[-1][-1] = transform(inProj,outProj, float(DNAdata[-1][-2]), float(DNAdata[-1][-1]))

	
# read NTA data
dic = {}
for feature in data['features']:
	dic[feature['properties']['NTAName']] = {'BoroName': feature['properties']['BoroName'], 'centroid': feature['properties']['centroid']['coordinates'], 'GeoJsonFile': feature['properties']['GeoJsonFile'], 'match':[]}


def match(DNAdata, NTAdata):
	for item in DNAdata:
		distance = float('Inf')
		coor_DNA = (item[-2], item[-1])
		for neigh in NTAdata:
			coor_NTA = (NTAdata[neigh]['centroid'][0], NTAdata[neigh]['centroid'][1])

			if distance > vincenty(coor_DNA, coor_NTA):
				distance = vincenty(coor_DNA, coor_NTA)
				tem = neigh

		NTAdata[tem]['match'].append(item[0])


match(DNAdata, dic)
print len(dic)
#print dic


# output the match file using csv format
import csv
with open('match_output.csv','w') as output:
	fieldnames = ['NTA', 'DNAmatch']
	writer = csv.DictWriter(output, fieldnames=fieldnames)

	writer.writeheader()
	for item in dic:
		writer.writerow({'NTA': item, 'DNAmatch': ','.join(dic[item]['match'])})
		

    

    