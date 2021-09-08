from dataclasses import dataclass, field
from data.environment import *
from data.summary import *



@dataclass
class BuildLayout:
    environment: Environment = Environment()
    summary: Summary = Summary()
    groups: list = field(default_factory=list)
