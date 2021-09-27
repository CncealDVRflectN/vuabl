from dataclasses import dataclass, field
from data.asset import Asset


@dataclass
class AssetData:
    asset: Asset = Asset()
    size: int = 0
    referencedBy: set = field(default_factory=set)
