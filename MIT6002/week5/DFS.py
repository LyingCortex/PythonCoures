from graph import *

def DFS(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        
        return path
    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            newPath = DFS(graph,node,end,path,shortest)
            
            if newPath != None:
                print 'path:', printPath(newPath)
                return newPath

def DFSShortest(graph, start, end, path = [], shortest = None):
    #assumes graph is a Digraph
    #assumes start and end are nodes in graph
    path = path + [start]
    print 'Current dfs path:', printPath(path)
    if start == end:
        return path
    for node in graph.childrenOf(start):
        print 'node = ' ,
        print node
        if node not in path: #avoid cycles
            if shortest == None or len(path)<len(shortest):
                print 'hi'
                newPath = DFSShortest(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
                    print 'path:', printPath(newPath)
                    print '-------------------'
    return shortest

def dfs(graph, start_node, end_node, path=[], valid_paths=[]):
        path = path + [start_node]
        if start_node == end_node:
            valid_paths.append(path)
            print 'Current dfs path:', printPath(path)
            return valid_paths
        for node in graph.childrenOf(start_node):
            if node not in path:
                valid_paths = dfs(graph, node, end_node, path, valid_paths)
        return valid_paths

def testSP():
    nodes = []
    for name in range(6):
        nodes.append(Node(str(name)))
    g = Digraph()
    for n in nodes:
        g.addNode(n)
    
    g.addEdge(Edge(nodes[0],nodes[1]))
    g.addEdge(Edge(nodes[1],nodes[2]))
    g.addEdge(Edge(nodes[2],nodes[3]))
    g.addEdge(Edge(nodes[2],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[4]))
    g.addEdge(Edge(nodes[3],nodes[5]))
    g.addEdge(Edge(nodes[0],nodes[2]))
    g.addEdge(Edge(nodes[1],nodes[0]))
    g.addEdge(Edge(nodes[3],nodes[1]))
    g.addEdge(Edge(nodes[4],nodes[0]))
    g.addEdge(Edge(nodes[0],nodes[3]))
    
    print g
#    sp = DFSShortest(g, nodes[0], nodes[5])
    sp =dfs(g, nodes[0], nodes[5])
#    print 'Shortest path found by DFS:', printPath(sp)
    print 'Shortest path found by DFS:'
    print sp
    
testSP()