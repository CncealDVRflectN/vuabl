from data.scope import Scope
from data.explicit_asset import *
from parsing.parameters import *
from parsing.asset_type import *
import re



def is_explicit_assets_header(line: str) -> bool:
    return re.match(r"^\s*Explicit Assets[:]{0,1}.*", line)



def parse_archive_explicit_asset(lines: list) -> ExplicitAsset:
    asset: ExplicitAsset = ExplicitAsset()

    asset.path = re.search(r"^\s*([^(]+)\(", lines[0]).group(1).rstrip()
    asset.assetType = get_asset_type(asset.path)
    asset.totalSize = get_total_size(lines[0])
    asset.sizeFromObjects = get_size_from_objects(lines[0])
    asset.sizeFromStreamedData = get_size_from_streamed_data(lines[0])
    asset.fileIndex = get_file_index(lines[0])
    asset.addressableName = get_addressable_name(lines[0])

    for line in lines:
        if is_param(line, "Internal References"):
            asset.internalReferences = get_assets_list_param(line, "Internal References")

    return asset



def parse_archive_explicit_assets(lines: str) -> list:
    assets: list[ExplicitAsset] = []

    scope: Scope = Scope.ExplicitAssets
    explicitAssetLines: list[str] = []

    for line in lines:
        if scope == Scope.ExplicitAsset:
            if re.match(r"^\t{4,}.+", line):
                explicitAssetLines.append(line)
            else:
                assets.append(parse_archive_explicit_asset(explicitAssetLines))
                explicitAssetLines.clear()
                scope = Scope.ExplicitAssets

        if scope != Scope.ExplicitAsset and re.match(r"^\t{3,}.+", line):
            explicitAssetLines.append(line)
            scope = Scope.ExplicitAsset

    if explicitAssetLines:
        assets.append(parse_archive_explicit_asset(explicitAssetLines))

    return assets