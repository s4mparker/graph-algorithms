
from abstract import AbstractGraph
from util import supercall

# Packaging
__all__ = ['AbstractGraph']

class AdjencencyGraph(AbstractGraph):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.graph = {}

# ---- Graph Methods --------------------------------------------

    @supercall
    def addVertex(self, label):
        self.graph[label] = []

    @supercall
    def addEdge(self, source, destination, weight=None):
        self.graph[source].append((destination, weight))

    def vertices(self):
        return list(self.graph.keys())

    def edges(self):
        all_edges = []
        for source in self.vertices():
            for (destination, weight) in self.graph[source]:
                all_edges.append((source, destination))
        return all_edges

if __name__ == '__main__':
    g = AdjencencyGraph()
    g.addVertex('A')
    g.addVertex('B')
    g.addEdge('A', 'B')
    
        
