from pandas import DataFrame
from data.group import *
import utils.conversion as conversion



def get_group_assets_table_by_size(group: Group) -> DataFrame:
    assets: list[dict] = []

    for archive in group.archives:
        for explicitAsset in archive.explicitAssets:
            assets.append({
                "path": explicitAsset.path, 
                "type": explicitAsset.assetType, 
                "size": explicitAsset.totalSize, 
                "referenced": ""
            })

        for file in archive.files:
            for dataFromOtherAsset in file.dataFromOtherAssets:
                referencedBy: str = ""

                for referencingAsset in dataFromOtherAsset.referencingAssets:
                    if referencedBy:
                        referencedBy += " "

                    referencedBy += referencingAsset.path

                assets.append({
                    "path": dataFromOtherAsset.path, 
                    "type": dataFromOtherAsset.assetType, 
                    "size": dataFromOtherAsset.size, 
                    "referenced": referencedBy
                })

    assets.sort(key=lambda entry:entry["size"], reverse=True)

    paths: list[str] = [asset["path"] for asset in assets]
    types: list[str] = [asset["type"].name for asset in assets]
    sizes: list[str] = [conversion.bytes_to_readable_size(asset["size"]) for asset in assets]
    references: list[str] = [asset["referenced"] for asset in assets]

    return DataFrame(dict(path=paths, type=types, size=sizes, references=references))
