import gmaps

locationList = []

for line in open('locationList.txt').readlines():
    stringCoord = line.strip().split(',')
    locationList.append([stringCoord[0], stringCoord[1]])

gmaps.heatmap(locationList)