import os
import json
from gmplot import gmplot
from pathlib import Path
from FireNode import FireNode
from cluster import Cluster

def loadEvents(PATH_TO_DATA,archiveName):
    os.chdir(PATH_TO_DATA)
    with open(archiveName, 'r') as f:
        event_dict = json.load(f)
    f.close()
    return event_dict

def plotAndDisplay(incidents,hubs,special,means,gmap):
    '''
    Incidents is a tuple of incident lats and incident longs
    Hubs is a tuple of hub lats and hub longs
    '''
    gmap.scatter(incidents[0],incidents[1],'#FF0000',size=400,marker=False)
    gmap.scatter(hubs[0],hubs[1],"#0000FF",size=1600,marker=False)
    gmap.scatter(special[0],special[1],"#000000",size=400,marker=False)
    gmap.scatter(means[0],means[1],"#008000",size=400,marker=False)
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
incident_nodes=[]
for e in archive_dict: #each e is another event
    incident_nodes.append(FireNode(e["latitude"],e["longitude"],"event",0,e["acq_date"],e["confidence"],e["frp"]))
    incidentList.append((e["latitude"],e["longitude"]))
copy_incident_nodes=incident_nodes[:]

genesis_cluster=Cluster()
genesis_cluster.form_cluster(incident_nodes[-1],5,incident_nodes)

special_nodes=[]
for node in genesis_cluster.nodes_in_cluster:
    special_nodes.append((node.lat,node.long))
mean_node=[(genesis_cluster.mean_location)]
special_lats,special_lons=zip(*special_nodes)
specials=(special_lats,special_lons)
mean_lat,mean_lons=zip(*mean_node)
means=(mean_lat,mean_lons)


gmap = gmplot.GoogleMapPlotter(incidentList[0][0],incidentList[0][1], 9)
incident_lats, incident_lons=zip(*incidentList)
hubs_lats,hubs_lons=zip(*locations)
incidents=(incident_lats,incident_lons)
hubs=(hubs_lats,hubs_lons)
plotAndDisplay(incidents,hubs,specials,means,gmap)
