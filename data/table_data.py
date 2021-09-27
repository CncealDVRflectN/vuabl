from pandas import DataFrame
from data.group import Group
from data.asset_data import AssetData
import utils.conversion as conversion


def get_group_assets_table_by_size(group: Group) -> DataFrame:
    assets: dict[str, AssetData] = {}

    for archive in group.archives:
        for explicitAsset in archive.explicitAssets:
            assets[explicitAsset.path] = AssetData(explicitAsset, explicitAsset.totalSize)

        for file in archive.files:
            for dataFromOtherAsset in file.dataFromOtherAssets:
                data: AssetData

                if dataFromOtherAsset.path in assets:
                    data = assets[dataFromOtherAsset.path]
                else:
                    data = AssetData(dataFromOtherAsset, dataFromOtherAsset.size)
                    assets[dataFromOtherAsset.path] = data

                for referencingAsset in dataFromOtherAsset.referencingAssets:
                    data.referencedBy.add(referencingAsset)

    assetsData: list[AssetData] = list(assets.values())

    assetsData.sort(key=lambda entry:entry.size, reverse=True)

    paths: list[str] = [assetData.asset.path for assetData in assetsData]
    types: list[str] = [assetData.asset.assetType.name for assetData in assetsData]
    sizes: list[str] = [conversion.bytes_to_readable_size(assetData.size) for assetData in assetsData]

    references: list[str] = []

    for assetData in assetsData:
        referencedBy: list[str] = [referenceAsset.path for referenceAsset in assetData.referencedBy]
        referencedBy.sort()

        referencesStr: str = ""

        for index, reference in enumerate(referencedBy):
            if index > 0:
                referencesStr += "\n"

            referencesStr += reference

        references.append(referencesStr)

    return DataFrame(dict(path=paths, type=types, size=sizes, references=references))
