import gmplot
from haversine import haversine


def getCoordsInRadius(centreLat, centreLong, radius = 10, every = 1): # km radius

    x = []
    y = []
    i = 0
    for line in open('locationList.txt').readlines():
        stringCoord = line.strip().split(',')
        lat = float(stringCoord[0])
        long = float(stringCoord[1])

        if i % every == 0 and haversine((centreLat, centreLong),
                                        (lat, long)
                                        ) <= radius:
            x.append(lat)
            y.append(long)
        i += 1

    return x, y


lat, long = gmplot.GoogleMapPlotter.geocode("Crowthorne")
gmap = gmplot.GoogleMapPlotter(lat, long, zoom = 10)


xs, ys = getCoordsInRadius(lat, long, every = 20)
gmap.scatter(xs, ys, marker=False)

gmap.draw("mymap.html")