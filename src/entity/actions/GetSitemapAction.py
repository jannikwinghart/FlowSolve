from entity.actions.Action import Action
import requests

class GetSitemapAction(Action):
    def __init__(
        self, 
        id: int, 
        title: str, 
        description: str, 
    ):
        super().__init__(id=id, title=title, description=description)
        self.ip = None
        self.port = None

    def run(self, ip, port):
        response = requests.get(f"http://{ip}:{port}/sitemap.xml")
        response.raise_for_status()
        return response.text