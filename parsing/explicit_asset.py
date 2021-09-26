from data.explicit_asset import *
from parsing.parameters import *
from parsing.asset_type import *
from utils.layout_reader import LayoutReader
import re



def is_explicit_assets_header(line: str) -> bool:
    return re.match(r"^\s*Explicit Assets[:]{0,1}.*", line)



def parse_archive_explicit_asset(reader: LayoutReader) -> ExplicitAsset:
    asset: ExplicitAsset = ExplicitAsset()
    intent: int = get_intent(reader.currentLine())

    asset.path = re.search(r"^\s*([^(]+)\(", reader.currentLine()).group(1).rstrip()
    asset.assetType = get_asset_type(asset.path)
    asset.totalSize = get_total_size(reader.currentLine())
    asset.sizeFromObjects = get_size_from_objects(reader.currentLine())
    asset.sizeFromStreamedData = get_size_from_streamed_data(reader.currentLine())
    asset.fileIndex = get_file_index(reader.currentLine())
    asset.addressableName = get_addressable_name(reader.currentLine())

    try:
        while True: 
            line: str = reader.nextLine()

            if get_intent(line) <= intent: 
                break
            if is_param(line, "Internal References"):
                asset.internalReferences = get_assets_list_param(line, "Internal References")

    except StopIteration:
        pass

    return asset



def parse_archive_explicit_assets(reader: LayoutReader) -> list:
    assets: list[ExplicitAsset] = []
    intent: int = get_intent(reader.currentLine())

    try:
        isNext: bool = True

        while True:
            line: str = reader.currentLine()

            if isNext:
                line = reader.nextLine()

            if get_intent(line) <= intent:
                break
            else:
                assets.append(parse_archive_explicit_asset(reader))
                isNext = False

    except StopIteration:
        pass

    return assets