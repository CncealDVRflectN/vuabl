from dataclasses import dataclass, field
from data.asset import *



@dataclass
class ExplicitAsset(Asset):
    totalSize: int = 0
    sizeFromObjects: int = 0
    sizeFromStreamedData: int = 0
    fileIndex: int = 0
    addressableName: str = ""
    internalReferences: list = field(default_factory=list)