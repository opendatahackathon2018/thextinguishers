from distancetime import getDurationGMAPS
def calculate_score(nodes,hubs):
    '''
    The lower the distance from hub to event and the higher the weight of the event,
    the higher the score of the hub!

    Score of hub = sum(weight_of_surrounding_events/((distance_to_event)^2))
    '''
    hub_score={}
    for hub in hubs:
        hub_score[hub]=0
    for node in nodes:
        source=str((node.nearest_hub).lat)+", "+str((node.nearest_hub).long)
        destination=str(node.lat)+", "+str(node.long)
        try:
            hub_score[node.nearest_hub]+=node.weight/((getDurationGMAPS(source,destination))*2)
        except:
            hub_score[node.nearest_hub]+=node.weight/((node.nearest_hub).getDistance(node))
    return hub_score
