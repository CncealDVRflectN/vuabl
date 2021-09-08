from data.scope import Scope
from data.build_layout import *
from parsing.parameters import *
from parsing.summary import *
from parsing.group import *
from io import TextIOWrapper
import re



def parse_build_layout(file: TextIOWrapper) -> BuildLayout:
    layout: BuildLayout = BuildLayout()
    
    groupLines: list[str] = []
    summaryLines: list[str] = []
    scope: Scope = Scope.Global
    
    for line in file:
        line = line.rstrip()

        if scope == Scope.Global:
            if is_param(line, "Unity Version"):
                layout.environment.unityVersion = get_string_param(line, "Unity Version")
            elif is_param(line, "com.unity.addressables"):
                layout.environment.addressablesPackageVersion = get_string_param(line, "com.unity.addressables")
        elif scope == Scope.Summary:
            if re.match(r"\s+.+", line):
                summaryLines.append(line)
            else:
                layout.summary = parse_summary(summaryLines)
                scope = Scope.Global
                summaryLines.clear()
        elif scope == Scope.Group:
            if re.match(r"\s+.+", line):
                groupLines.append(line)
            else:
                layout.groups.append(parse_group(groupLines))
                scope = Scope.Global
                groupLines.clear()

        if scope != Scope.Summary and is_summary_header(line):
            scope = Scope.Summary


        if scope != Scope.Group and is_group_header(line):
            scope = Scope.Group
            groupLines.append(line)
        
    if scope == Scope.Summary:
        layout.summary = parse_summary(summaryLines)
    if scope == Scope.Group:
        layout.groups.append(parse_group(groupLines))

    return layout


def read_build_layout(path: str) -> BuildLayout:
    buildLayoutFile: TextIOWrapper = open(path, "r")
    layout: BuildLayout = parse_build_layout(buildLayoutFile)

    buildLayoutFile.close()
    return layout