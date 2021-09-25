from dash_table import DataTable
from pandas import DataFrame
from conversion import *
import theming


def create_group_assets_by_size_table(groupName, data: DataFrame) -> DataTable:
    groupID: str = to_layout_id(groupName)

    headerStyle: dict = theming.get_data_table_header_theme()
    cellStyle: dict = theming.get_data_table_cell_theme()

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
            style_table={ "overflowX": "auto" }, 
            style_header=headerStyle, 
            style_cell=cellStyle
        )
