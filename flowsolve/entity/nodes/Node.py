from typing import List, Dict
from abc import ABC, abstractmethod

from flowsolve.entity.NodeInput import NodeInput
from flowsolve.entity.State import State
from flowsolve.entity.FlowchartComponent import FlowchartComponent

class Node(FlowchartComponent, ABC):
    def __init__(
        self, 
        id: int,
        title: str,
        description: str,
        inputs: Dict[str, NodeInput],
        subscribers: List[FlowchartComponent] = []
    ) -> None:
        super().__init__(id=id, title=title, description=description)
        self.inputs = inputs
        self.outputs = {}
        self.subscribers = subscribers

    @abstractmethod
    def run_logic(self):
        pass

    def run(self):
        print(f"Run Node {self.title}.")
        self.run_logic()
        if self.state == State.SUCCESSFUL:
            self.triggerSubscribers()
        return True

    def trigger(self):
        if self.state == State.TRIGGERED:
            print(f"Node {self.title} already triggered")
            return False
        else:
            print(f"Node {self.title} triggered")
            self.state = State.TRIGGERED
            return True
        
    def addSubscriber(self, subscriber: FlowchartComponent):
        self.subscribers.append(subscriber)

    def triggerSubscribers(self):
        for subscriber in self.subscribers:
            subscriber.trigger()