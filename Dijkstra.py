from Vertex import *
from Graph import *
from PriorityQueue import *
import render
from time import sleep

INFINITE = 10000000

def dij(graph,src_id,tar_id):
    if src_id == tar_id:
        return 0
    dist = {src_id:0}
    c_dist = {src_id:1}
    # create a .png state
    #prev = {}

    Q = BinHeap()

    for v in graph.vertList:
        if v != src_id:
            dist[v] = INFINITE
            c_dist[v] = 0
            #prev[v] = None

        # create a .png state updating the vertex label
        Q.insert([v,dist[v]])

    #print Q.heapList
    #g = Graph()
    reng = render.render(graph,dist,c_dist)
    sleep(1.25)
    
    while not Q.isEmpty():
        u = Q.delMin()
        c_dist[u] = 1
        reng = render.render(graph,dist,c_dist)
        sleep(1.25)
        #try to color the deleted vertex
        #print u
        unb = graph.vertList[u].connectedTo
        for nb in unb:
            tup = [u,nb]
            #print type(unb[nb][0])
            alt = dist[u] + unb[nb][0]
            if Q.check(nb) :
                reng = render.render(graph,dist,c_dist,tup=tup)
            if alt < dist[nb]:
                #print 'altered',nb,dist[nb],'->',alt
                dist[nb] = alt
                sleep(1.25)
                #reng = render.render(graph,'0')
                #prev[nb] = u
                Q.editPriority([nb,alt])# changed Q.editPriority([v,alt]) --> ...([nb,alt] )
                reng = render.render(graph,dist,c_dist,tup=tup)

    #return dist[tar_id]

[n,m] = map(int,raw_input().split())

graph = Graph()
#dumb_graph = Graph()

for i in range(m):
    [u,v,d] = map(int, raw_input().split())
    graph.addEdge(u,v,d)
    graph.addEdge(v,u,d)
    #dumb_graph.addEdge(u,v,d)

k = int(raw_input())

for i in range(k):
    [u,v] = map(int, raw_input().split())
    print dij(graph,u,v)
