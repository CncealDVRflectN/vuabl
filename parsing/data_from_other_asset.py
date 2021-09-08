from data.data_from_other_asset import *
from data.scope import *
from parsing.parameters import *
from parsing.asset_type import *
import re



def is_data_from_other_assets_header(line: str) -> bool:
    return re.match(r"^\s*Data From Other Assets.*", line)



def parse_file_data_from_other_asset(lines: list) -> DataFromOtherAsset:
    data: DataFromOtherAsset = DataFromOtherAsset()

    data.path = re.search(r"^\s*([^(]+)\(", lines[0]).group(1).rstrip()
    data.assetType = get_asset_type(data.path)
    data.size = get_size(lines[0])
    data.sizeFromObjects = get_size_from_objects(lines[0])
    data.sizeFromStreamedData = get_size_from_streamed_data(lines[0])
    data.objectCount = get_header_integer_param(lines[0], "Object Count")

    for line in lines:
        if is_param(line, "Referencing Assets"):
            data.referencingAssets = get_assets_list_param(line, "Referencing Assets")

    return data


def parse_file_data_from_other_assets(lines: list) -> list:
    data: list[DataFromOtherAsset] = []

    scope: Scope = Scope.DataFromOtherAssets
    dataFromOtherAssetLines: list[str] = []

    for line in lines:
        if scope == Scope.DataFromOtherAsset:
            if re.match(r"^\t{6,}.+", line):
                dataFromOtherAssetLines.append(line)
            else:
                data.append(parse_file_data_from_other_asset(dataFromOtherAssetLines))
                dataFromOtherAssetLines.clear()
                scope = Scope.DataFromOtherAssets

        if scope != Scope.DataFromOtherAsset and re.match(r"^\t{5,}.+", line):
            dataFromOtherAssetLines.append(line)
            scope = Scope.DataFromOtherAsset

    if dataFromOtherAssetLines:
        data.append(parse_file_data_from_other_asset(dataFromOtherAssetLines))

    return data
