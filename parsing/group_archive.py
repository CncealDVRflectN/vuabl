from parsing.file import is_files_header, parse_group_archive_files
from data.scope import Scope
from data.group_archive import *
from parsing.asset_type import *
from parsing.parameters import *
from parsing.explicit_asset import *
import re



def is_group_archive_header(line: str) -> bool:
    return re.match(r"^\s*Archive .+", line)



def parse_group_archive(archiveLines: list) -> GroupArchive:
    archive: GroupArchive = GroupArchive()

    archive.name = re.search(r"^\s*Archive (.+) \(.*", archiveLines[0]).group(1)
    #print(f"\tParsing '{archive.name}' archive data")

    archive.size = get_size(archiveLines[0])
    archive.assetBundleObjectSize = get_asset_bundle_object_size(archiveLines[0])
    archive.compression = get_compression(archiveLines[0])

    scope: Scope = Scope.Archive
    explicitAssetsLines: list[str] = []
    filesLines: list[str] = []

    for line in archiveLines:
        if scope == Scope.ExplicitAssets:
            if re.match(r"^\t{3,}", line):
                explicitAssetsLines.append(line)
            else:
                scope = Scope.Archive
        elif scope == Scope.Files:
            if re.match(r"^\t{3,}", line):
                filesLines.append(line)
            else:
                scope = Scope.Archive
        
        if scope != Scope.ExplicitAssets and is_explicit_assets_header(line):
            scope = Scope.ExplicitAssets
            explicitAssetsLines.append(line)

        if scope != Scope.Files and is_files_header(line):
            scope = Scope.Files
            filesLines.append(line)

    archive.explicitAssets = parse_archive_explicit_assets(explicitAssetsLines)
    archive.files = parse_group_archive_files(filesLines)

    return archive