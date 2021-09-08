from dash import Dash
from dash.dependencies import Output, Input, State
from plotly.missing_ipywidgets import FigureWidget
from data.group import *
from data.size_plot_data import *
from data.table_data import *
from plots.categories import *
from plots.groups import *
from tables.group import *
from conversion import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc



def generate_group_layout(group: Group) -> html.Div:
    categoriesData: SizePlotData = get_group_categories_sizes_plot_data(group)
    groupID: str = to_layout_id(group.name)
    
    groupElements: list = [
        html.P(f"Total Size: {bytes_to_readable_size(group.totalSize)}")
    ]

    if not categoriesData.frame.empty:
        categoriesPie: FigureWidget = plot_categories_sizes_pie(categoriesData)
        categoriesBars: FigureWidget = plot_categories_sizes_bars(categoriesData)

        groupElements.append(dcc.Graph(figure=categoriesPie))
        groupElements.append(dcc.Graph(figure=categoriesBars))

    assetsTableData: DataFrame = get_group_assets_table_by_size(group)
    assetsTable: DataTable = create_group_assets_by_size_table(group.name, assetsTableData)

    groupElements.append(assetsTable)

    return html.Div([
        dbc.Button(group.name, id=f"group-{groupID}-collapse-button", n_clicks=0), 
        dbc.Collapse(groupElements, id=f"group-{groupID}-collapse", is_open=False)
    ])


def generate_groups_layout(groups: list) -> html.Div:
    groupsData: SizePlotData = get_groups_sizes_plot_data(groups)
    
    elements: list = []

    if not groupsData.frame.empty:
        groupsPie: FigureWidget = plot_groups_sizes_pie(groupsData)
        groupsBars: FigureWidget = plot_groups_sizes_bars(groupsData)

        elements.append(dcc.Graph(figure=groupsPie))
        elements.append(dcc.Graph(figure=groupsBars))

    for group in groups:
        elements.append(generate_group_layout(group))

    return html.Div([
        dbc.Button("Groups", id="groups-collapse-button", n_clicks=0), 
        dbc.Collapse(elements, id="groups-collapse", is_open=False)
    ])



def generate_group_callbacks(app: Dash, group: Group):
    groupID: str = to_layout_id(group.name)
    
    @app.callback(
        Output(f"group-{groupID}-collapse", "is_open"), 
        Input(f"group-{groupID}-collapse-button", "n_clicks"), 
        State(f"group-{groupID}-collapse", "is_open")
    )
    def toggle_group_collapse(n, isOpen) -> bool:
        if (n):
            return not isOpen

        return isOpen


def generate_groups_callbacks(app: Dash, groups: list):
    @app.callback(
        Output(f"groups-collapse", "is_open"), 
        Input(f"groups-collapse-button", "n_clicks"), 
        State(f"groups-collapse", "is_open")
    )
    def toggle_groups_collapse(n, isOpen) -> bool:
        if (n):
            return not isOpen

        return isOpen

    for group in groups:
        generate_group_callbacks(app, group)
