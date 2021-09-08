from dash_table import DataTable
from pandas import DataFrame
from conversion import *



def create_group_assets_by_size_table(groupName, data: DataFrame) -> DataTable:
    groupID: str = to_layout_id(groupName)
    return DataTable(
            id=f"group-{groupID}-assets-table", 
            data=data.to_dict("records"), 
            columns=[
                {"id": "path", "name": "Path"},  
                {"id": "type", "name": "Type"}, 
                {"id": "size", "name": "Size"}, 
                {"id": "references", "name": "Referenced By"}
            ], 
            page_size=25, 
            style_cell={"whiteSpace": "pre-line"}
        )
