import requests
from typing import Dict

from flowsolve.entity.NodeInput import NodeInput
from flowsolve.entity.nodes.Node import Node

class GetSitemapNode(Node):
    def __init__(
        self, 
        id: int, 
        title: str, 
        description: str, 
        inputs: Dict[str, NodeInput],
    ):
        super().__init__(id=id, title=title, description=description, inputs=inputs)

    def run_logic(self):
        response = requests.get(f"{self.inputs['ip']}:{self.inputs['port']}/sitemap.xml")
        response.raise_for_status()
        return response.text