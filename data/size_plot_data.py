from typing import Tuple
from data.group import Group
from dataclasses import dataclass
from pandas import DataFrame
from data.asset_type import *
from data.build_layout import *
from parsing.asset_type import *
from conversion import *



@dataclass
class SizePlotData:
    frame: DataFrame = DataFrame()
    sizeDivider: int = 1
    sizePostfix: str = "B"



def get_build_categories_sizes_plot_data(layout: BuildLayout) -> SizePlotData:
    sizesLookup: dict[AssetType, int] = {}

    for group in layout.groups:
        for archive in group.archives:
            for explicitAsset in archive.explicitAssets:
                if not explicitAsset.assetType in sizesLookup:
                    sizesLookup[explicitAsset.assetType] = explicitAsset.totalSize
                else:
                    sizesLookup[explicitAsset.assetType] += explicitAsset.totalSize
            
            for file in archive.files:
                for dataFromOtherAsset in file.dataFromOtherAssets:
                    if not dataFromOtherAsset.assetType in sizesLookup:
                        sizesLookup[dataFromOtherAsset.assetType] = dataFromOtherAsset.size
                    else:
                        sizesLookup[dataFromOtherAsset.assetType] += dataFromOtherAsset.size

    if not sizesLookup:
        return SizePlotData()

    categoriesSizes: list = sorted(sizesLookup.items(), key=lambda entry:entry[1], reverse=True)
    categories: list[str] = [asset_type_to_category_name(categorySize[0]) for categorySize in categoriesSizes]
    sizes: list[int] = [categorySize[1] for categorySize in categoriesSizes]
    maxSizePower: int = get_size_power(sizes[0])

    plotData: SizePlotData = SizePlotData()
    plotData.sizeDivider = pow(1024, maxSizePower)
    plotData.sizePostfix = get_full_size_power_postfix(maxSizePower)

    sizes = [size / plotData.sizeDivider for size in sizes]

    plotData.frame = DataFrame(dict(category=categories, size=sizes, colors=categories))

    return plotData



def get_group_categories_sizes_plot_data(group: Group) -> SizePlotData:
    sizesLookup: dict[AssetType, int] = {}

    for archive in group.archives:
        for explicitAsset in archive.explicitAssets:
            if not explicitAsset.assetType in sizesLookup:
                sizesLookup[explicitAsset.assetType] = explicitAsset.totalSize
            else:
                sizesLookup[explicitAsset.assetType] += explicitAsset.totalSize

        for file in archive.files:
            for dataFromOtherAsset in file.dataFromOtherAssets:
                if not dataFromOtherAsset.assetType in sizesLookup:
                    sizesLookup[dataFromOtherAsset.assetType] = dataFromOtherAsset.size
                else:
                    sizesLookup[dataFromOtherAsset.assetType] += dataFromOtherAsset.size

    if not sizesLookup:
        return SizePlotData()

    categoriesSizes: list = sorted(sizesLookup.items(), key=lambda entry:entry[1], reverse=True)
    categories: list[str] = [asset_type_to_category_name(categorySize[0]) for categorySize in categoriesSizes]
    sizes: list[int] = [categorySize[1] for categorySize in categoriesSizes]
    maxSizePower: int = get_size_power(sizes[0])

    plotData: SizePlotData = SizePlotData()
    plotData.sizeDivider = pow(1024, maxSizePower)
    plotData.sizePostfix = get_full_size_power_postfix(maxSizePower)

    sizes = [size / plotData.sizeDivider for size in sizes]

    plotData.frame = DataFrame(dict(category=categories, size=sizes, colors=categories))

    return plotData



def get_groups_sizes_plot_data(groups: list) -> SizePlotData:
    if not groups:
        return SizePlotData()

    groupsSizes: list[Tuple] = [(group.name, group.totalSize) for group in groups]
    groupsSizes.sort(key=lambda entry:entry[1], reverse=True)
    names: list[str] = [entry[0] for entry in groupsSizes]
    sizes: list[int] = [entry[1] for entry in groupsSizes]
    maxSizePower: int = get_size_power(sizes[0])

    plotData: SizePlotData = SizePlotData()
    plotData.sizeDivider = pow(1024, maxSizePower)
    plotData.sizePostfix = get_full_size_power_postfix(maxSizePower)

    sizes = [size / plotData.sizeDivider for size in sizes]

    plotData.frame = DataFrame(dict(group=names, size=sizes, colors=names))

    return plotData