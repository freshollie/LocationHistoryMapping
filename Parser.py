import json

mapsJson = json.load(open('LocationHistory.json'))


i = 0

with open('locationList.txt', 'w') as f:
    for location in mapsJson['locations']:
        i += 1
        f.write(str(location['latitudeE7'] * 0.0000001) + ',' + str(location['longitudeE7'] * 0.0000001)+'\n')