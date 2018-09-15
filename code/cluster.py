class Cluster:
    def __init__(self):
        self.nodes_in_cluster=[]
        self.mean_location=(0.0,0.0)

    def calculate_mean_location(self):
        cumulative_lat,cumulative_long=0,0
        for node in self.nodes_in_cluster:
            cumulative_lat+=node.lat
            cumulative_long+=node.long
        average_lat=cumulative_lat/len(self.nodes_in_cluster)
        average_long=cumulative_long/len(self.nodes_in_cluster)
        self.mean_location=(average_lat,average_long)

    def form_cluster(self,starting_node,x,incident_nodes):
        nearest=starting_node.getNearestX(x+1,incident_nodes)
        nextOne=nearest[-1]
        (self.nodes_in_cluster)=nearest[:-1]
        self.calculate_mean_location()
        return nextOne
