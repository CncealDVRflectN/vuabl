from data.file import *
from data.scope import *
from parsing.parameters import *
from parsing.data_from_other_asset import *
from utils.layout_reader import LayoutReader
import re



def is_files_header(line: str) -> bool:
    return re.match(r"^\s*Files[:]{0,1}", line)


def is_file_header(line: str) -> bool:
    return re.match(r"^\s*File \d+ \(", line)



def parse_group_archive_file(reader: LayoutReader) -> File:
    file: File = File()
    intent: int = get_intent(reader.currentLine())

    file.index = int(re.search(r"^\s*File (\d+) \(", reader.currentLine()).group(1))
    file.preloadInfoSize = get_header_size_param(reader.currentLine(), "PreloadInfoSize")
    file.monoScriptsCount = get_header_integer_param(reader.currentLine(), "MonoScripts")
    file.monoScroptSize = get_header_size_param(reader.currentLine(), "MonoScript Size")

    try:
        isNext: bool = True

        while True:
            line: str = reader.currentLine()

            if isNext:
                line = reader.nextLine()

            if get_intent(line) <= intent:
                break
            elif is_data_from_other_assets_header(line):
                file.dataFromOtherAssets = parse_file_data_from_other_assets(reader)
                isNext = False

    except StopIteration:
        pass

    return file


def parse_group_archive_files(reader: LayoutReader) -> list:
    files: list[File] = []
    intent: int = get_intent(reader.currentLine())

    try:
        isNext: bool = True

        while True:
            line: str = reader.currentLine()

            if isNext:
                line = reader.nextLine()

            if get_intent(line) <= intent:
                break
            elif is_file_header(line):
                files.append(parse_group_archive_file(reader))
                isNext = False

    except StopIteration:
        pass

    return files
