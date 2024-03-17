"""
FlowchartComponent.py
This file contains the FlowchartComponent class which is used to represent a flowchart component.

Classes:
    FlowchartComponent
"""
from abc import ABC, abstractmethod

from flowsolve.entity.State import State

"""
FlowchartComponent
This class is used to represent a flowchart component.    
"""
class FlowchartComponent(ABC):
    """
    __init__
    The constructor for the FlowchartComponent class.
    
    :param id: The id of the flowchart component.
    :param title: The title of the flowchart component.
    :param description: The description of the flowchart component.
    :param state: The state of the flowchart component.

    :type id: int
    :type title: str
    :type description: str
    :type state: State

    :return: None
    """
    def __init__(self, id: int, title: str, description: str, state: State = State.INACTIVE) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.state = state

    def activate(self):
        self.state = State.TRIGGERED

    @abstractmethod
    def run(self):
        self.state = State.RUNNING
        self.state = State.SUCCESSFUL