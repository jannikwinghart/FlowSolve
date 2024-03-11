from entity.nodes.Node import Node
import requests
from typing import Dict
from entity.NodeInput import NodeInput

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