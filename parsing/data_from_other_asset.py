from data.data_from_other_asset import *
from data.scope import *
from parsing.parameters import *
from parsing.asset_type import *
from utils.layout_reader import LayoutReader
import re



def is_data_from_other_assets_header(line: str) -> bool:
    return re.match(r"^\s*Data From Other Assets.*", line)



def parse_file_data_from_other_asset(reader: LayoutReader) -> DataFromOtherAsset:
    data: DataFromOtherAsset = DataFromOtherAsset()
    intent: int = get_intent(reader.currentLine())

    data.path = re.search(r"^\s*([^(]+)\(", reader.currentLine()).group(1).rstrip()
    data.assetType = get_asset_type(data.path)
    data.size = get_size(reader.currentLine())
    data.sizeFromObjects = get_size_from_objects(reader.currentLine())
    data.sizeFromStreamedData = get_size_from_streamed_data(reader.currentLine())
    data.objectCount = get_header_integer_param(reader.currentLine(), "Object Count")

    try:
        while True:
            line: str = reader.nextLine()

            if get_intent(line) <= intent:
                break
            elif is_param(line, "Referencing Assets"):
                data.referencingAssets = get_assets_list_param(line, "Referencing Assets")

    except StopIteration:
        pass

    return data


def parse_file_data_from_other_assets(reader: LayoutReader) -> list:
    data: list[DataFromOtherAsset] = []
    intent: int = get_intent(reader.currentLine())

    try: 
        isNext: bool = True

        while True:
            line: str = reader.currentLine()

            if isNext:
                line = reader.nextLine()

            curIntent = get_intent(line)

            if curIntent <= intent:
                break
            elif curIntent == intent + 1:
                data.append(parse_file_data_from_other_asset(reader))
                isNext = False

    except StopIteration:
        pass

    return data
