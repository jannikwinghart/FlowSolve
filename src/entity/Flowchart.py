from entity.FlowchartComponent import FlowchartComponent
from entity.Node import Node
from entity.Edge import Edge

class Flowchart(FlowchartComponent):
    def __init__(self, id: int, title: str, description: str) -> None:
        super().__init__(id=id, title=title, description=description)
        self.nodes = []
        self.edges = []
    
    def addNode(self, node: Node):
        self.nodes.append(node)
    
    def addEdge(self, edge: Edge):
        self.edges.append(edge)
    
    def run(self):
        for edge in self.edges:
            edge.run()
    