from entity.FlowchartComponent import FlowchartComponent

class Action(FlowchartComponent):
    def __init__(self, id: int, title: str, description: str):
        super().__init__(id=id, title=title, description=description)
    
    def run(self, *args, **kwargs):
        pass