from graphviz import Graph
from time import sleep

class render:

	def __init__(self,our_graph,wt_dist,colour_list,tup=[-1,-1]):
		self.G = Graph(format='png')
		self.edgeList = []
		#i=0

		
		for vertex in our_graph.vertList:
			self.G.node(str(vertex),label='INF' if wt_dist[vertex]==10000000 else str(wt_dist[vertex]),color='red' if colour_list[vertex] else 'black')
			for adjvertices in our_graph.vertList[vertex].connectedTo:
				if tup==[vertex,adjvertices] or tup==[adjvertices,vertex]: 
					cl='green'  
				else: 
					cl='black'

				#print vertex.connectedTo[adjvertices] 
				if our_graph.vertList[vertex].connectedTo[adjvertices][1] in self.edgeList:
					pass
				else:
					self.G.edge(str(vertex),str(adjvertices),str(our_graph.vertList[vertex].connectedTo[adjvertices][0]),color=cl)
					self.edgeList.append(our_graph.vertList[vertex].connectedTo[adjvertices][1])
			#self.G.edge(str(vertex),str((vertex+1)%10),label='edge',color='green')


		self.G.view()
		#self.G.render(filename='output/'+str(i)+'.png')
		#i = i+1

	

	

	