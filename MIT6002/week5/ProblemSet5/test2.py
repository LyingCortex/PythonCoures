# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:28:32 2015

@author: LY
"""
import string
# This imports everything from `graph.py` as if it was defined in this file!
from graph import * 
def load_map(mapFilename):
    """ 
    Parses the map file and constructs a directed graph

    Parameters: 
        mapFilename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive 
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a directed graph representing the map
    """
    # TODO
    print "Loading map from file..."
    f = open(mapFilename, 'r',0)
#    nodes = []
#    edges = []
    g = WeightedDigraph()
    for line in f:
        w = string.split(line)
#        nodes.append(Node(w[0]))
#        nodes.append(Node(w[1]))
#        edges.append(WeightedEdge(w[0], w[1], w[2], w[3]))
        
        node1 = Node(int(w[0]))
        node2 = Node(int(w[1]))
        edge = WeightedEdge(node1,node2, float(w[2]), float(w[3]))
        if not g.hasNode(node1):
            g.addNode(node1)
        if not g.hasNode(node2):
            g.addNode(node2)
        g.addEdge(edge)
    return g
        


def getDistanceOfAjcentNodes(digraph, node1, node2):  # get the distance between two adjacent  points
   
    child_lst = digraph.edges[node1]
    for cl in child_lst:
        if cl[0] == node2:
            return [cl[1], cl[2]]
    

def getPathDistance(digraph, path):    # get the total distance of the path
    total_dist = 0.0
    dist_outdoor = 0.0
    if path:
        if len(path) > 1:
            for i in xrange(len(path)-1):
                [dist1, dist2] = getDistanceOfAjcentNodes(digraph,path[i], path[i+1])
                total_dist += dist1
                dist_outdoor += dist2
    return [total_dist, dist_outdoor]
    
    
    
    
    
    
def dfs(graph, start_node, end_node, path=[], valid_paths=[]):
        path = path + [start_node]
        if start_node == end_node:
            valid_paths.append(path)
            
            return valid_paths
        for node in graph.childrenOf(start_node):
            if node not in path:
                valid_paths = dfs(graph, node, end_node, path, valid_paths)
        return valid_paths

        
        
        
    
def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    
    valid_paths = dfs(digraph, Node(start), Node(end))
    
    shortest_path = None
    shortest_path_dist = maxTotalDist + 1
    for p in valid_paths:
       [total_dist, dist_outdoor] = getPathDistance(digraph, p)
       if total_dist <= maxTotalDist and dist_outdoor <= maxDistOutdoors:
           if total_dist < shortest_path_dist:
               shortest_path = p
               shortest_path_dist = total_dist
    if shortest_path is None:
        raise ValueError
    else:
        clear_path = []
        for e in shortest_path:
            clear_path.append(str(e))
        return clear_path
              
       
        








mitMap = load_map("mit_map.txt")
LARGE_DIST = 1000000


print "---------------"
print "Test case 1:"
print "Find the shortest-path from Building 32 to 56"
expectedPath1 = ['32', '56']
brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)
print "Expected: ", expectedPath1
print "Brute-force: ", brutePath1
print "---------------------------------------------------------------------"

print "Test case 2:"
print "Find the shortest-path from Building 32 to 56 without going outdoors"
expectedPath2 = ['32', '36', '26', '16', '56']
brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)

print "Expected: ", expectedPath2
print "Brute-force: ", brutePath2