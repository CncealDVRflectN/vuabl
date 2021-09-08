from data.summary import *
from parsing.parameters import *
import re



def is_summary_header(line: str) -> bool:
    return re.match(r"^Summary.*", line)



def parse_summary(summaryLines: list) -> Summary:
    summary: Summary = Summary()

    for line in summaryLines:
        if is_param(line, "Addressable Groups"):
            summary.groupsCount = get_integer_param(line, "Addressable Groups")
        elif is_param(line, "Total Build Size"):
            summary.totalBuildSize = get_size_param(line, "Total Build Size")
        elif is_param(line, "Total MonoScript Size"):
            summary.totalMonoScriptSize = get_size_param(line, "Total MonoScript Size")
        elif is_param(line, "Total AssetBundle Object Size"):
            summary.totalAssetBundleObjectSize = get_size_param(line, "Total AssetBundle Object Size")

    return summary