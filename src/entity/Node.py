from typing import List, Dict

from entity.actions.Action import Action
from entity.ActionOutput import ActionOutput
from entity.State import State
from entity.FlowchartComponent import FlowchartComponent

class Node(FlowchartComponent):
    def __init__(
        self, 
        id: int,
        title: str,
        description: str,
        inputs: Dict[str, ActionOutput],
        actions: Dict[str, Action],
    ) -> None:
        super().__init__(id=id, title=title, description=description)
        self.inputs = inputs
        self.actions = actions
        self.outputs = {actionId: None for actionId in actions.keys()}

    def run(self):
        self.state = State.RUNNING
        for key, action in self.actions.items():
            self.outputs[key] = action.run()

        if all(action.state == State.SUCCESSFUL for action in self.actions):
            self.state = State.SUCCESSFUL
        else:
            self.state = State.FAILED