from dataclasses import dataclass, field
from data.environment import Environment
from data.summary import Summary



@dataclass
class BuildLayout:
    environment: Environment = Environment()
    summary: Summary = Summary()
    groups: list = field(default_factory=list)
    assetsData: dict = field(default_factory=dict)
