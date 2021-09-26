from data.summary import *
from parsing.parameters import *
from utils.layout_reader import LayoutReader
import re



def is_summary_header(line: str) -> bool:
    return re.match(r"^\s*Summary.*", line)



def parse_summary(reader: LayoutReader) -> Summary:
    summary: Summary = Summary()
    intent: int = get_intent(reader.currentLine())

    try:
        while True:
            line: str = reader.nextLine()

            if get_intent(line) <= intent:
                break
            elif is_param(line, "Addressable Groups"):
                summary.groupsCount = get_integer_param(line, "Addressable Groups")
            elif is_param(line, "Total Build Size"):
                summary.totalBuildSize = get_size_param(line, "Total Build Size")
            elif is_param(line, "Total MonoScript Size"):
                summary.totalMonoScriptSize = get_size_param(line, "Total MonoScript Size")
            elif is_param(line, "Total AssetBundle Object Size"):
                summary.totalAssetBundleObjectSize = get_size_param(line, "Total AssetBundle Object Size")
    
    except StopIteration:
        pass

    return summary