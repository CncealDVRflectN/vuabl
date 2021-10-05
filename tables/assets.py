from dash.dash_table import DataTable
from pandas import DataFrame
import utils.theming as theming



def create_duplicates_table(data: DataFrame) -> DataTable:
    headerStyle: dict = theming.get_data_table_header_theme()
    cellStyle: dict = theming.get_data_table_cell_theme()

    return DataTable(
        id="duplicates-table", 
        data=data.to_dict("records"), 
        columns=[
            {"id": "path", "name": "Path"},  
            {"id": "size", "name": "Size"}, 
            {"id": "groups", "name": "Referenced By Groups"}, 
            {"id": "references", "name": "Referenced By Assets"}
        ], 
        page_size=25, 
        style_table={ "overflowX": "auto" }, 
        style_header=headerStyle, 
        style_cell=cellStyle
    )
