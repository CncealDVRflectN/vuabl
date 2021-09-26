from parsing.file import is_files_header, parse_group_archive_files
from data.group_archive import *
from parsing.asset_type import *
from parsing.parameters import *
from parsing.explicit_asset import *
from utils.layout_reader import LayoutReader
import re



def is_group_archive_header(line: str) -> bool:
    return re.match(r"^\s*Archive .+", line)



def parse_group_archive(reader: LayoutReader) -> GroupArchive:
    archive: GroupArchive = GroupArchive()
    intent: int = get_intent(reader.currentLine())

    archive.name = re.search(r"^\s*Archive (.+) \(.*", reader.currentLine()).group(1)

    archive.size = get_size(reader.currentLine())
    archive.assetBundleObjectSize = get_asset_bundle_object_size(reader.currentLine())
    archive.compression = get_compression(reader.currentLine())

    try:
        isNext: bool = True

        while True:
            line: str = reader.currentLine()

            if isNext:
                line = reader.nextLine()

            if get_intent(line) <= intent:
                break
            elif is_explicit_assets_header(line):
                archive.explicitAssets = parse_archive_explicit_assets(reader)
                isNext = False
            elif is_files_header(line):
                archive.files = parse_group_archive_files(reader)
                isNext = False

    except StopIteration:
        pass

    return archive