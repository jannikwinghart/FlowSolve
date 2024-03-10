"""
State.py
This file contains the State enum which is used to represent the state of a FlowchartComponent.
"""
import enum

"""
State
This enum is used to represent the state of a FlowchartComponent.

Attributes:
    INACTIVE: 0
    PREPARING: 1
    RUNNING: 2
    SUCCESSFUL: 3
    FAILED: 4
"""
class State(enum.Enum):
    INACTIVE = 0
    TRIGGERED = 1
    RUNNING = 2
    SUCCESSFUL = 3
    FAILED = 4