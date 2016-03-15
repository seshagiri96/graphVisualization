from Vertex import *

class Graph:

    #i = 0
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        global i
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbour(self.vertList[t].id,self.numEdges,cost)
        self.vertList[t].addNeighbour(self.vertList[f].id,self.numEdges,cost)
        self.numEdges = self.numEdges + 1

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
