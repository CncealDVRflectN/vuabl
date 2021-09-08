from data.file import *
from data.scope import *
from parsing.parameters import *
from parsing.data_from_other_asset import *
import re



def is_files_header(line: str) -> bool:
    return re.match(r"^\s*Files[:]{0,1}", line)


def is_file_header(line: str) -> bool:
    return re.match(r"^\s*File \d+ \(", line)



def parse_group_archive_file(lines: list) -> File:
    file: File = File()

    file.index = int(re.search(r"^\s*File (\d+) \(", lines[0]).group(1))
    file.preloadInfoSize = get_header_size_param(lines[0], "PreloadInfoSize")
    file.monoScriptsCount = get_header_integer_param(lines[0], "MonoScripts")
    file.monoScroptSize = get_header_size_param(lines[0], "MonoScript Size")

    scope: Scope = Scope.File
    dataFromOtherAssetsLines: list[str] = []

    for line in lines:
        if scope == Scope.DataFromOtherAssets:
            if re.match(r"\t{5,}.+", line):
                dataFromOtherAssetsLines.append(line)
            else:
                scope = Scope.File

        if scope != Scope.DataFromOtherAssets and is_data_from_other_assets_header(line):
            dataFromOtherAssetsLines.append(line)
            scope = Scope.DataFromOtherAssets

    file.dataFromOtherAssets = parse_file_data_from_other_assets(dataFromOtherAssetsLines)

    return file


def parse_group_archive_files(lines: list) -> list:
    files: list[File] = []

    scope: Scope = Scope.Files
    fileLines: list[str] = []

    for line in lines:
        if scope == Scope.File:
            if re.match(r"\t{4,}.+", line):
                fileLines.append(line)
            else:
                files.append(parse_group_archive_file(fileLines))
                fileLines.clear()
                scope = Scope.Files

        if scope != Scope.File and is_file_header(line):
            fileLines.append(line)
            scope = Scope.File

    if fileLines:
        files.append(parse_group_archive_file(fileLines))

    return files
