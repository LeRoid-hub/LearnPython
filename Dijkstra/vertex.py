import math

class vertex:

    def __init__ (self, id, x,y):
        self.id = id
        self.x = x
        self.y = y
        self.edges = []
        self.cost = float('inf')
    
    def getID(self):
        return self.id

    def getEdges(self):
        return self.edges

    def reachedFromAtCost(self, vertex, cost):
        self.reachedFrom = vertex
        self.cost = cost

    def getFrom(self):
        return self.reachedFrom

    def getCost(self):
        return self.cost

    def distanceTo(self, vertex):
        return math.sqrt((self.x - vertex.x)**2 + (self.y - vertex.y)**2)
