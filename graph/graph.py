from string import ascii_letters
from random import choices

# Packaging
__all__ = ['Graph']

class Graph:

    def __init__(self, vertices=None, edges=None, **kwargs):
        self.id          = ''.join(choices(ascii_letters, k=5))
        self.weighted    = kwargs.pop('weighted', False)
        self.directed    = kwargs.pop('directed', False)

        self.connections = {}

        for vertex in vertices:
            self.addVertex(vertex=vertex)

        for edge in edges:
            source, destination, weight = None, None, None
            if len(edge) == 2:
                (source, destination) = edge
            elif len(edge) == 3:
                (source, destination, weight) = edge
            else:
                raise ValueError('unexpected edge format')
            self.addEdge(source=source, destination=destination, weight=weight)

    def addVertex(self, vertex, **edges):
        pass

    def addVertices(self, *vertices):
        for vertex in vertices : self.addVertex(vertex=vertex)

    def addEdge(self, source, destination, weight=None):
        if self.weighted and not weight:
            raise ValueError('cannot add an unweighted edge to a weighted graph')
        elif not self.weighted and weight:
            raise ValueError('cannot add a weighted edge to an unweighted graph')
        
        if not self.weighted and not weight:
            weight = 1
        
        pass

        if not self.directed:
            pass

    def addEdges(self, *edges):
        for edge in edges:
            source, destination, weight = None, None, None
            if len(edge) == 2:
                (source, destination) = edge
            elif len(edge) == 3:
                (source, destination, weight) = edge
            else:
                raise ValueError('unknown edge format')
            self.addEdge(source=source, destination=destination, weight=weight)
            
            



    

    