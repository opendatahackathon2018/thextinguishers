from math import sin, cos, sqt, radians

class Node:
    def __init__(self,lat,long):
        self.lat=lat
        self.long=long

    def getLat(self):
        return self.lat

    def getLong(self):
        return self.long

    def getDistance(self,target_node):
        R=6373 #radius of earth in km

        lat1=radians(self.lat)
        lon1=radians(self.long)
        lat2=target_node.lat
        lon2=target_node.long

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
        c=2*atan2(sqrt(a),sqrt(1-a))
        distance=R*c
        return distance

    def calculateWeight(self):
        raise NotImplementedError
