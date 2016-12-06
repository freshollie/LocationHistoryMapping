import json

mapsJson = json.load(open('LocationHistory.json'))

for value in mapsJson:
    print(value)