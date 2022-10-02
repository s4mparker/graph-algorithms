import networkx as nx

from string import ascii_letters
from random import choices

# Packaging
__all__ = ['AbstractGraph']

class AbstractGraph:

    def __init__(self, **kwargs):
        """ Create a new abstract representation of a graph 
    
        Parameters:
            **kwargs (optional) : keyword arguments
                id              : graph id (created if not provided)
                weighted        : whether the graph is weighted or not (defaults to False)
                directed        : whether the graph is directed or not (defaults to False)
                multiedge       : whether two vertices may be connected by multiple edges
        """

        if type(self) is AbstractGraph : raise NotImplementedError(f'cannot create an abstract graph')

        self.graphID   = kwargs.pop('id', ''.join(choices(ascii_letters, k=5)))
        self.directed  = kwargs.pop('directed', False)
        self.weighted  = kwargs.pop('weighted', False)
        self.multiedge = kwargs.pop('multiedge', False)

        if len(kwargs) > 0 : raise ValueError(f'unexpected kwargs: {" ".join(kwargs.keys())}')

# ---- Graph Methods --------------------------------------------

    def vertices(self):
        """ Return a list of vertices present in a graph """
        raise NotImplementedError(f'must be implemented by a subclass')

    def edges(self):
        """ Return a list of edges present in a graph """
        raise NotImplementedError(f'must be implemented by a subclass')

    def addVertex(self, label):
        """ Add a new vertex to a graph 
        
        Parameters:
            label   : vertex label 
        """

        if type(self) is AbstractGraph: 
            raise NotImplementedError(f'cannot add vertex to an abstract graph')
        if label in self.vertices(): 
            raise ValueError(f'label already present in graph')

    def addEdge(self, source, destination, weight=None):
        """ Add a new edge to a graph

        Parameters:
            source              : edge's starting vertex
            destination         : edge's end vertex
            weight (optional)   : edge's weight (defaults to None / 0)
        """

        if type(self) is AbstractGraph: 
            raise NotImplementedError(f'cannot add vertex to an abstract graph')
        if self.weighted and weight is None: 
            raise ValueError(f'cannot add an unweighted edge to a weighted graph')
        if not self.weighted and weight is not None: 
            raise ValueError(f'cannot add a weighted edge to an unweighted graph')
        if source not in self.vertices(): 
            raise ValueError(f'no vertex ({source}) found in graph')
        if destination not in self.vertices(): 
            raise ValueError(f'no vertex ({destination}) found in graph')
        if not self.multiedge and (source, destination) in self.edges():
            raise ValueError(f'cannot add multiple edges ({source}->{destination}) to a non-multiedge graph')
        if not self.directed: 
            self.addEdge(source=destination, destination=source, weight=weight, skip_supercall=True)

    def getVertex(self, label):
        """ Return a list of vertices that are connected to a given vertex 
        
        Parameters:
            label   : the vertex who's connections will be retrieved
        """

        if type(self) is AbstractGraph: 
            raise NotImplementedError(f'cannot get a vertex from an abstract graph')
        if label not in self.vertices(): 
            raise ValueError(f'no vertex ({label}) found in graph')

    def getEdges(self, source, destination):
        """ Return a list of edges that connect two vertices together 
        
        Parameters:
            source      : starting vertex
            destination : ending vertex
        """

        if type(self) is AbstractGraph: 
            raise NotImplementedError(f'cannot get a vertex from an abstract graph')
        if source not in self.vertices(): 
            raise ValueError(f'no vertex ({source}) found in graph')
        if destination not in self.vertices(): 
            raise ValueError(f'no vertex ({destination}) found in graph')

