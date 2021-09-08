from dash.dash import Dash
from dash.dependencies import Output, Input, State
from plotly.missing_ipywidgets import FigureWidget
from data.build_layout import *
from data.size_plot_data import *
from plots.categories import *
from conversion import *
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc



def generate_summary_layout(buildLayout: BuildLayout) -> html.Div:
    categoriesData: SizePlotData = get_build_categories_sizes_plot_data(buildLayout)
    
    elements: list = [
        html.P(f"Groups Count: {buildLayout.summary.groupsCount}"), 
            html.P(f"Total Build Size: {bytes_to_readable_size(buildLayout.summary.totalBuildSize)}"), 
            html.P(f"Total MonoScript Size: {bytes_to_readable_size(buildLayout.summary.totalMonoScriptSize)}"), 
            html.P(f"Total AssetBundle Object Size: {bytes_to_readable_size(buildLayout.summary.totalAssetBundleObjectSize)}")
    ]

    if not categoriesData.frame.empty:
        categoriesPie: FigureWidget = plot_categories_sizes_pie(categoriesData)
        categoriesBars: FigureWidget = plot_categories_sizes_bars(categoriesData)

        elements.append(dcc.Graph(figure=categoriesPie))
        elements.append(dcc.Graph(figure=categoriesBars))

    return html.Div([
        dbc.Button("Summary", id="summary-collapse-button", n_clicks=0), 
        dbc.Collapse(elements, id="summary-collapse", is_open=False)
    ])



def generate_summary_callbacks(app: Dash):
    @app.callback(
        Output("summary-collapse", "is_open"), 
        Input("summary-collapse-button", "n_clicks"), 
        State("summary-collapse", "is_open")
    )
    def toggle_summary_collapse(n, isOpen) -> bool:
        if (n):
            return not isOpen

        return isOpen