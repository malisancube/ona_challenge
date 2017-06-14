import requests
import simplejson as json
from collections import defaultdict

web_request = requests.get('https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json')
content = web_request.content
data = json.loads(content)

district = {}
total_functioning = 0

for i in range(0, len(data)):
    community = data[i]['communities_villages']
    water_functioning = data[i]['water_functioning']
    if water_functioning == 'yes':
        total_functioning += 1
        if community in district:
            district[community] += 1
        else:
            district[community] = 1

for w in sorted(district, key=district.get, reverse=True):
  print w, district[w]







#for communities_villages, water_functioning in zip(j[0]['communities_villages'], j[0]['water_functioning']):
#    print item['repository']['name']
	
#for x,y in zip(a, b):
	
#number_functional = reduce(lambda x, y: x + y, j['water_functioning'])
