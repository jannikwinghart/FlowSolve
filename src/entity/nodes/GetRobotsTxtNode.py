from entity.nodes.Node import Node
import requests
from typing import Dict
from entity.NodeInput import NodeInput

class GetRobotsTxtNode(Node):
    def __init__(
        self, 
        id: int, 
        title: str, 
        description: str, 
        inputs: Dict[str, NodeInput],
    ):
        super().__init__(id=id, title=title, description=description, inputs=inputs)

    def run_logic(self):
        response = requests.get(f"https://{self.inputs['ip']}:{self.inputs['port']}/robots.txt", verify=False)
        response.raise_for_status()
        self.outputs["robots_txt"] = response.text
        