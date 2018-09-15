from datetime import datetime
import googlemaps


def getDistance(source,destination):
    return call_api(source,destination,"distance")

def getDuration(source,destination):
    return call_api(source,destination,"duration")


def call_api(source,destination,api_type):
    api_key="AIzaSyAZdfgkmRFRdS4AYanI1j0fiJDrq8C1FYk"
    gmaps=googlemaps.Client(key=api_key)
    now=datetime.now()
    directions_result=gmaps.directions(source,destination,mode="driving",departure_time=now)
    for map1 in directions_result:
            overall_stats=map1['legs']
            for dimensions in overall_stats:
                    distanceOrTime=dimensions[api_type]
                    return distanceOrTime['value'] #distance returned in meters, time returned in seconds
