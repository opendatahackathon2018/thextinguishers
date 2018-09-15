import os
import json
from gmplot import gmplot

filename="saved.html"

os.chdir(#directory)
with open('archive.json', 'r') as f:
    fire_dict = json.load(f)


bigList=[]
for fire in fire_dict:
    lat,long=fire['latitude'],fire['longitude']
    bigList.append((lat,long))

gmap = gmplot.GoogleMapPlotter(lat,long, 100)
fire_lats, fire_lons=zip(*bigList)


gmap.scatter(fire_lats,fire_lons,'#FF0000',size=400,marker=False)
gmap.draw("C:\\Users\\PythonTesting\\Desktop\\"+filename)
