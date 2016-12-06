import heatmap
locationList = []

for line in open('locationList.txt').readlines():
    stringCoord = line.strip().split(',')
    locationList.append([float(stringCoord[0]), float(stringCoord[1])])

h = heatmap.Heatmap()
img = h.heatmap()
img.save('test.png')