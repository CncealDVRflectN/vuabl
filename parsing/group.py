from data.group import *
from parsing.parameters import *
from parsing.group_archive import *
from utils.layout_reader import LayoutReader
import re



def is_group_header(line: str) -> bool:
    return re.match(r"^\s*Group .+", line)



def parse_group(reader: LayoutReader) -> Group:
    group: Group = Group()
    intent: int = get_intent(reader.currentLine())
    
    group.name = re.search(r"^\s*Group (.+) \(.*", reader.currentLine()).group(1)
    group.bundlesCount = get_bundles_count(reader.currentLine())
    group.explicitAssetCount = get_explicit_asset_count(reader.currentLine())
    group.totalSize = get_total_size(reader.currentLine())

    try:
        isNext: bool = True

        while True:
            line: str = reader.currentLine()

            if isNext:
                line = reader.nextLine()

            if get_intent(line) <= intent:
                break
            elif is_group_archive_header(line):
                group.archives.append(parse_group_archive(reader))
                isNext = False

    except StopIteration:
        pass

    return group