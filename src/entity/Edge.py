from typing import List

from entity.FlowchartComponent import FlowchartComponent
from entity.Node import Node
from entity.State import State
from entity.Condition import Condition

class Edge(FlowchartComponent):
    def __init__(
        self, 
        id: int, 
        title: str, 
        description: str, 
        startNode: Node,
        endNode: Node,
        conditions: List[Condition]
    ) -> None:
        super().__init__(id=id, title=title, description=description)
        self.startNode = startNode
        self.endNode = endNode
        self.conditions = conditions
    
    def trigger(self):
        self.state = State.TRIGGERED

    def run(self):
        self.state = State.RUNNING
        for condition in self.conditions:
            if condition.run():
                self.state = State.SUCCESSFUL
                break
        else:
            self.state = State.FAILED
        return self.state

    

   