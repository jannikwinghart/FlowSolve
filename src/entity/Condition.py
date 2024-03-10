from entity.FlowchartComponent import FlowchartComponent
from entity.State import State

class Condition(FlowchartComponent):
    def __init__(self, id: int, title: str, description: str) -> None:
        super().__init__(id=id, title=title, description=description)
        self.result = False
    
    def run(self):
        self.state = State.RUNNING
        
        # TODO: Implement condition logic
        self.result = True

        self.state = State.SUCCESSFUL

