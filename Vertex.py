class Vertex:
	"""docstring for Vertex"""
	def __init__(self, key):
		#super(Vertex, self).__init__()
		self.id = key
		self.connectedTo = {}

	def addNeighbour(self,nbr,edge_id,weight=0):
		self.connectedTo[nbr] = [weight, edge_id]

	def __str__(self):
		return str(self.id) #+ ' connectedTo: ' + str([x.id for x in self.connectedTo])

	def getConnections(self):
		return self.connectedTo.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr][0]