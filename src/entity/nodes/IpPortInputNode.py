from typing import Dict

from entity.NodeInput import NodeInput
from entity.nodes.Node import Node
from entity.State import State

class IpPortInputNode(Node):
    def __init__(
        self, 
        id: int, 
        title: str, 
        description: str, 
        inputs: Dict[str, NodeInput],
    ):
        super().__init__(id=id, title=title, description=description, inputs=inputs)
        self.outputs["ip"] = None
        self.outputs["port"] = None        

    def run_logic(self):
        self.state = State.RUNNING
        
        self.outputs["ip"] = input("Enter the IP address: ")
        self.outputs["port"] = input("Enter the port: ")

        self.state = State.SUCCESSFUL