import gmaps
gmaps.configure('AIzaSyDkKaasomnWFDxMdRHM5QAxRbxzZIkIBaw')

locationList = []

for line in open('locationList.txt').readlines():
    stringCoord = line.strip().split(',')
    locationList.append([float(stringCoord[0]), float(stringCoord[1])])

m = gmaps.Map()
layer = gmaps.Heatmap(data=locationList)
m.add_layer(layer)