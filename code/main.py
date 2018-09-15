import os
import json
from gmplot import gmplot
from pathlib import Path

def loadEvents(PATH_TO_DATA,archiveName):
    os.chdir(PATH_TO_DATA)
    with open(archiveName, 'r') as f:
        fire_dict = json.load(f)
    f.close()
    return fire_dict

def plotAndDisplay(incidents,hubs,gmap):
    '''
    Incidents is a tuple of incident lats and incident longs
    Hubs is a tuple of hub lats and hub longs
    '''
    gmap.scatter(incidents[0],incidents[1],'#FF0000',size=400,marker=False)
    gmap.scatter(hubs[0],hubs[1],"#0000FF",size=1600,marker=False)
    gmap.draw(PATH_TO_SAVE+"\\"+FILENAME)

def loadHubs(PATH_TO_DATA,txtName):
    pass

locations = [(34.8302, 33.3933),
            (35.1283, 33.3145),
            (34.6815, 33.0281),
            (34.6903, 33.0692),
            (34.6684, 32.9928),
            (34.9207, 33.6163),
            (34.9608, 33.6574),
            (34.8739, 33.6177),
            (34.7694, 32.4355),
            (35.0297, 32.4306),
            (34.7152, 32.4782),
            (35.0575, 33.9704),
            (35.1728, 33.3573),
            (35.1883, 33.394)]

FILENAME="saved.html"
PATH_TO_CODE=os.path.dirname(os.path.abspath(__file__))
PATH_TO_SAVE=(Path(PATH_TO_CODE).parent).__str__()+"\\saves"
PATH_TO_DATA=(Path(PATH_TO_CODE).parent).__str__()+"\\data"
archiveName="archive.json"
archive_dict = loadEvents(PATH_TO_DATA,archiveName)

'''
os.chdir(PATH_TO_DATA)
loadHubs()
'''
os.chdir(PATH_TO_CODE)

incidentList=[]
for incident in archive_dict:
    lat,long=incident['latitude'],incident['longitude']
    incidentList.append((lat,long))


gmap = gmplot.GoogleMapPlotter(lat,long, 9)
incident_lats, incident_lons=zip(*incidentList)
hubs_lats,hubs_lons=zip(*locations)
incidents=(incident_lats,incident_lons)
hubs=(hubs_lats,hubs_lons)
plotAndDisplay(incidents,hubs,gmap)
