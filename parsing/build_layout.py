from data.build_layout import *
from parsing.parameters import *
from parsing.summary import *
from parsing.group import *
from utils.layout_reader import LayoutReader



def parse_build_layout(reader: LayoutReader) -> BuildLayout:
    layout: BuildLayout = BuildLayout()
    
    try:
        isNext: bool = True

        while True:
            line: str = reader.currentLine()

            if isNext:
                line = reader.nextLine()

            isNext = True

            if is_param(line, "Unity Version"):
                layout.environment.unityVersion = get_string_param(line, "Unity Version")
            elif is_param(line, "com.unity.addressables"):
                layout.environment.addressablesPackageVersion = get_string_param(line, "com.unity.addressables")
            elif is_summary_header(line):
                layout.summary = parse_summary(reader)
                isNext = False
            elif is_group_header(line):
                layout.groups.append(parse_group(reader))
                isNext = False

    except StopIteration:
        pass

    return layout


def read_build_layout(path: str) -> BuildLayout:
    reader: LayoutReader = LayoutReader(path)
    layout: BuildLayout = parse_build_layout(reader)

    reader.close()
    return layout