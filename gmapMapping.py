import gmplot
import mapper

lat, long = gmplot.GoogleMapPlotter.geocode("Coventry")
gmap = gmplot.GoogleMapPlotter(lat, long, zoom=13)

xs, ys = mapper.getCoordsInRadius(lat, long, every=10, radius=2)
gmap.scatter(xs, ys, marker=False, size=2)

gmap.draw("mymap.html")