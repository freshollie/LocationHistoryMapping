from haversine import haversine


def getCoords():
    coords = []

    for line in open('locationList.txt').readlines():
        stringCoord = line.strip().split(',')
        coords.append((float(stringCoord[0]), float(stringCoord[1])))
    return coords

def getCoordsInArea(n, e, s, w, every=1):
    lats, longs = [], []
    i = 0
    for lat, long in getCoords():
        if w < long < e and n > lat > s and i % every == 0:
            lats.append(lat)
            longs.append(long)
        i += 1

    return lats, longs

def getCoordsInRadius(centreLat, centreLong, radius=10, every=1): # km radius

    lats = []
    longs = []
    i = 0
    for lat, long in getCoords():

        if i % every == 0 and haversine((centreLat, centreLong),
                                        (lat, long)
                                        ) <= radius:
            lats.append(lat)
            longs.append(long)
        i += 1

    return lats, longs