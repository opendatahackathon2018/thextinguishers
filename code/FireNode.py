from Node import Node

class FireNode(Node):
    def __init__(self,lat,long,type,popDist,acq_date,confidence,frp):
        super().__init__(lat,long,type,popDist)
        self.acq_date=acq_date
        self.confidence=confidence
        self.frp=frp

    def calculateWeight(self):
        '''
        Need to calculate weight
        '''
