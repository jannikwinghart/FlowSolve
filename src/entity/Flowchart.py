from entity.FlowchartComponent import FlowchartComponent
from entity.nodes.Node import Node
from entity.Edge import Edge
from entity.State import State

class Flowchart(FlowchartComponent):
    def __init__(self, id: int, title: str, description: str) -> None:
        super().__init__(id=id, title=title, description=description)
        self.nodes = []
        self.edges = []
        self.timeout = 10
    
    def addNode(self, node: Node):
        self.nodes.append(node)
    
    def addEdge(self, edge: Edge):
        self.edges.append(edge)
    
    def run(self):
        while self.timeout > 0:
            has_changed = False

            for node in self.nodes:
                if node.state == State.TRIGGERED:
                    has_changed = node.run()
            
            for edge in self.edges:                
                if edge.state == State.TRIGGERED:
                    has_changed = edge.run()              
    
            if not has_changed:
                break

            self.timeout -= 1

        # TODO: edge connection

        