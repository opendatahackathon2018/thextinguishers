import math

class Node:
    def __init__(self,lat,long,type,popDist):
        types=("event","hub")
        if type not in types:
            raise TypeError
        self.type=type
        self.lat=lat
        self.long=long
        self.populationDistribution=popDist

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long

    def getDistance(self,target_node):
        lat1, lon1 = self.lat,self.long
        lat2, lon2 = target_node.lat,target_node.long
        radius = 6371 # km radius of earth

        dlat = math.radians(lat2-lat1)
        dlon = math.radians(lon2-lon1)
        a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
            * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        d = radius * c
        return d

    def calculateWeight(self):
        raise NotImplementedError

    def getNearestX(self,x,listOfNodes):
        distances=[]
        distances_to_nodes={}
        original_len=len(listOfNodes)
        while 0<len(listOfNodes):
            node=listOfNodes[0]
            distance_from_new_node=self.getDistance(node)
            distances.append(self.getDistance(node))
            listOfNodes.remove(node)
            try:
                distances_to_nodes[distance_from_new_node].append(node)
            except:
                distances_to_nodes[distance_from_new_node]=[node]
        distances.sort()
        #print(distances)
        nearest=[]
        for number in distances[:x]:
            nearest+=distances_to_nodes[number]
        nearest=nearest[:x]
        return nearest
