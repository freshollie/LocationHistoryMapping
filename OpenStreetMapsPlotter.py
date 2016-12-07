from mpl_toolkits.basemap import Basemap
import mapper
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image
import threading
import requests
import os
import haversine
from numpy import meshgrid

def downloadImage(n, e, s, w, scale, name):
    print('Downloading map image')
    print("http://render.openstreetmap.org/cgi-bin/export?bbox=%s,%s,%s,%s&scale=%s&format=png" % (w, s, e, n, scale))
    data = requests.get(
        "http://render.openstreetmap.org/cgi-bin/export?bbox=%s,%s,%s,%s&scale=%s&format=png" % (w, s, e, n, scale))

    if data.status_code == 200:
        with open('Output/' + name + '_map.png', 'wb') as mapBackground:
            for chunk in data.iter_content(1024):
                mapBackground.write(chunk)
        print('Downloaded map image')
    else:
        print('Could not download')



def generatePointsMap(n, e, s, w, imageScale, name, every = 1):
    if not os.path.exists('Output'):
        os.mkdir('Output')

    downloadThread = threading.Thread(target=downloadImage, args=[n, e, s, w, imageScale, name])
    downloadThread.start()

    lon_0 = w + abs(w - e) / 2
    lat_0 = s + abs(n - s) / 2

    coords = mapper.getCoordsInArea(n, e, s, w, every=every)
    print("Plotting %s location coordinates" % (len(coords[0])))

    m = Basemap(llcrnrlon=w, llcrnrlat=s, urcrnrlon=e, urcrnrlat=n,
                resolution='h', projection='merc', lon_0=w + abs(w - e) / 2, lat_0=s + abs(n - s) / 2)

    x1, y1 = m(coords[1], coords[0])

    m.drawmapboundary(fill_color='white')  # fill to edge

    m.plot(x1, y1, 'o', markersize=5, markerfacecolor='black', markeredgecolor="none", alpha=0.5)
    #m.scatter(x1, y1, s=5, c='red', cmap=cm.jet, alpha=0.5)

    print('Finished plotting')
    if downloadThread.is_alive():
        print('Waiting for download to complete')
    while downloadThread.is_alive():
        pass

    try:
        backgroundImage = Image.open('Output/' + name + '_map.png')
        print('Loaded map image')
    except:
        return

    print('Saving plot')
    fig = plt.gcf()

    fig.set_size_inches(backgroundImage.width/100, backgroundImage.height/100)

    fig.savefig('Output/' + name + '_coords.png', dpi = 100, bbox_inches='tight', pad_inches=0, transparent=True, alpha=0.5)

    print('Opening plot image')
    foregroundImage = Image.open('Output/' + name + '_coords.png').resize((backgroundImage.width,backgroundImage.height))

    print('Compiling images')
    Image.alpha_composite(backgroundImage, foregroundImage).save('Output/' + name + '.png')


#generatePointsMap(*[float(input('Side Coord: ')) for i in range(4)], name=input('Name: '), every=int(input('Divide number of coords by?: ')))

#generatePointsMap(56.304, 7.229, 44.277, -5.955, imageScale = 5655207, name='France', every=1)
56.304, 2.373, 49.838  -5.955, 3000000
generatePointsMap(56.390, 2.823, 50.723, -11.678, 2631424, name='UK', every=1)

        #http://render.openstreetmap.org/cgi-bin/export?bbox=w,s,e,n&scale=10556&format=png
