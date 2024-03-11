from typing import List, Dict

from entity.FlowchartComponent import FlowchartComponent
from entity.nodes.Node import Node
from entity.State import State
from entity.Condition import Condition

class Edge(FlowchartComponent):
    def __init__(
        self, 
        id: int, 
        title: str, 
        description: str, 
        start_node: Node,
        end_node: Node,
        conditions: List[Condition],
        parameters: Dict[str, str] = {}
    ) -> None:
        super().__init__(id=id, title=title, description=description)
        self.start_node = start_node
        self.end_node = end_node
        self.conditions = conditions
        self.start_node.addSubscriber(self)
        self.parameters = parameters
    
    def trigger(self):
        if self.state == State.TRIGGERED:
            print(f"Edge {self.title} already triggered")
            return False
        else:
            print(f"Edge {self.title} triggered")
            self.state = State.TRIGGERED
            return True

    def run(self):
        print(f"Run Edge {self.title}.")
        self.state = State.RUNNING

        if len(self.conditions) == 0:
            self.state = State.SUCCESSFUL
    
        for condition in self.conditions:
            if condition.run():
                self.state = State.SUCCESSFUL
            else:
                self.state = State.CANCELLED
    
        if self.state == State.SUCCESSFUL:
            for output_name, input_name in self.parameters.items():
                self.end_node.inputs[input_name] = self.start_node.outputs[output_name]
            self.end_node.trigger()

        return True

    

   