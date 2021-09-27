from dataclasses import dataclass
from data.asset_type import *



@dataclass
class Asset:
    path: str = ""
    assetType: AssetType = AssetType.Other


    def __hash__(self) -> int:
        return hash(self.path)
