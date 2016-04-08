# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 21:04:21 2015

@author: LY
"""

from graph import *

nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

# add edges
edges = []

edges.append(Edge(nodes[0], nodes[1]))
edges.append(Edge(nodes[0], nodes[2]))


edges.append(Edge(nodes[1], nodes[4]))

edges.append(Edge(nodes[2], nodes[3]))


edges.append(Edge(nodes[3], nodes[5]))


edges.append(Edge(nodes[4], nodes[5]))

for e in edges:
    g.addEdge(e)
    
    
class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        # Your code here
        return self.weight
    def __str__(self):
        # Your code here
        return str(self.src) + '->' + str(self.dest)+' ('+str(self.weight)+')'
