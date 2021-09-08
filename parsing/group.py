from data.scope import Scope
from data.group import *
from parsing.parameters import *
from parsing.group_archive import *
import re



def is_group_header(line: str) -> bool:
    return re.match(r"^Group .+", line)



def parse_group(groupLines: list) -> Group:
    group: Group = Group()
    
    group.name = re.search(r"^Group (.+) \(.*", groupLines[0]).group(1)

    if group.name == "Built In Data":
        #print(f"Skipping '{group.name}' group data")
        return group

    #print(f"Parsing '{group.name}' group data")

    group.bundlesCount = get_bundles_count(groupLines[0])
    group.explicitAssetCount = get_explicit_asset_count(groupLines[0])
    group.totalSize = get_total_size(groupLines[0])

    archiveLines: list[str] = []
    scope: Scope = Scope.Group

    for line in groupLines:
        if scope == Scope.Archive:
            if re.match(r"\t{2,}", line):
                archiveLines.append(line)
            else:
                group.archives.append(parse_group_archive(archiveLines))
                scope = Scope.Group
                archiveLines.clear()
        
        if scope != Scope.Archive and is_group_archive_header(line):
            scope = Scope.Archive
            archiveLines.append(line)

    if scope == Scope.Archive:
        group.archives.append(parse_group_archive(archiveLines))

    return group