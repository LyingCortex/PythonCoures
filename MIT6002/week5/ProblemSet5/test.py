# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 10:28:32 2015

@author: LY
"""

def getDistanceOfAjcentNodes(digraph, node1, node2):
    Node1= Node(node1)
    Node2 = Node(node2)
    child_lst = digraph.edges[Node1]
    for cl in child_lst:
        if cl[0] == Node2:
            return [cl[1], cl[2]]
    
    
def DFSShortest(digraph, start, end, maxTotalDist, maxDistOutdoors,path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
#    print 'Current dfs path:', printPath(path)
    print 'path = ' + str(path)
    print '----------------'
    total_dist = 0
    dist_outdoor = 0
    if len(path) > 1:
        for i in xrange(len(path)-1):
            [dist1, dist2] = getDistanceOfAjcentNodes(digraph,path[i], path[i+1])
            
            
            total_dist += dist1
            dist_outdoor += dist2
            
            print 'd1 = ' +str(dist1),
            print '  total = ' + str(total_dist)
            print 'd2 = ' +str(dist2),
            print '  outdoor = ' + str(dist_outdoor)
    if start == end:
        return path
    if total_dist <= maxTotalDist and dist_outdoor <= maxDistOutdoors: 
        print 'hi'
        
        for node in digraph.childrenOf(Node(start)):
            if node.getName() not in path: #avoid cycles
                if shortest == None or len(path)<len(shortest):
                    newPath = DFSShortest(digraph,node.getName(),end,maxTotalDist, maxDistOutdoors,path,shortest)
                    if newPath != None:
                        shortest = newPath
        return shortest
#    else:
#        raise ValueError('Exceed the max value')



def bruteForceSearch(digraph, start, end, maxTotalDist, maxDistOutdoors):    
    """
    Finds the shortest path from start to end using brute-force approach.
    The total distance travelled on the path must not exceed maxTotalDist, and
    the distance spent outdoor on this path must not exceed maxDistOutdoors.

    Parameters: 
        digraph: instance of class Digraph or its subclass
        start, end: start & end building numbers (strings)
        maxTotalDist : maximum total distance on a path (integer)
        maxDistOutdoors: maximum distance spent outdoors on a path (integer)

    Assumes:
        start and end are numbers for existing buildings in graph

    Returns:
        The shortest-path from start to end, represented by 
        a list of building numbers (in strings), [n_1, n_2, ..., n_k], 
        where there exists an edge from n_i to n_(i+1) in digraph, 
        for all 1 <= i < k.

        If there exists no path that satisfies maxTotalDist and
        maxDistOutdoors constraints, then raises a ValueError.
    """
    #TODO
    return DFSShortest(digraph, start, end,maxTotalDist, maxDistOutdoors, path = [] )








mitMap = load_map("mit_map.txt")
#print isinstance(mitMap, Digraph)
#print isinstance(mitMap, WeightedDigraph)
#print 'nodes', mitMap.nodes
#print 'edges', mitMap.edges


LARGE_DIST = 1000000


print "---------------"
print "Test case 1:"
print "Find the shortest-path from Building 32 to 56"
expectedPath1 = ['32', '56']
brutePath1 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, LARGE_DIST)

print "Expected: ", expectedPath1
print "Brute-force: ", brutePath1



print "---------------"
print "Test case 2:"
print "Find the shortest-path from Building 32 to 56 without going outdoors"
expectedPath2 = ['32', '36', '26', '16', '56']
brutePath2 = bruteForceSearch(mitMap, '32', '56', LARGE_DIST, 0)
    # dfsPath2 = directedDFS(mitMap, '32', '56', LARGE_DIST, 0)
print "Expected: ", expectedPath2
print "Brute-force: ", brutePath2