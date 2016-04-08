nx = Node('x')
ny = Node('y')
nz = Node('z')
e1 = WeightedEdge(nx, ny, 18, 8)
e2 = WeightedEdge(ny, nz, 20, 1)
e3 = WeightedEdge(nz, nx, 7, 6)
g = WeightedDigraph()
g.addNode(nx)
g.addNode(ny)
g.addNode(nz)
g.addEdge(e1)
g.addEdge(e2)
g.addEdge(e3)
print g
Traceback (most recent call last):
  File "submission.py", line 94, in __str__
    for d in self.edges[str(k)]:
  File "submission.py", line 13, in __eq__
    return self.name == other.name
AttributeError: 'str' object has no attribute 'name'

*** ERROR: Failing test. We printed out and sorted the lines in your graph and our graph, and found failures in the following pairs of lines:
[(u'x->y (18.0, 8.0)', u'File "submission.py", line 94, in __str__'), (u'y->z (20.0, 1.0)', u'Traceback (most recent call last):'), (u'z->x (7.0, 6.0)', u'for d in self.edges[str(k)]:')] ***