from entity.actions.Action import Action

class IpPortInputAction(Action):
    def __init__(
        self, 
        id: int, 
        title: str, 
        description: str, 
    ):
        super().__init__(id=id, title=title, description=description)
        self.output.ip = None
        self.output.port = None        

    def run(self):
        self.output.ip = input("Enter the IP address: ")
        self.output.port = input("Enter the port: ")