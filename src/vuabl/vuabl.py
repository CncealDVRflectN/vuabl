from dash import Dash, html
from data.build_layout import BuildLayout
from argparse import ArgumentParser, Namespace
import parsing.build_layout as pblt
import layouts.environment as ltenv
import layouts.summary as ltsum
import layouts.group as ltgr
import layouts.assets as ltasts
import utils.arguments as arguments
import utils.theming as theming
import os


argumentsParser: ArgumentParser = arguments.get_parser()
argumentsValues: Namespace = argumentsParser.parse_args()

theming.theme = argumentsValues.theme

fullPath: str = os.path.abspath(argumentsValues.path)
buildLayout: BuildLayout = pblt.read_build_layout(fullPath)

app: Dash = Dash(__name__)
app.title = f"Visualizer for Unity Addressables build layout"

app.layout = html.Div(children=[
    html.Link(rel="stylesheet", href=theming.get_stylesheet_path()), 
    ltenv.generate_environment_layout(buildLayout.environment), 
    ltsum.generate_summary_layout(buildLayout), 
    ltgr.generate_groups_layout(buildLayout.groups, buildLayout.assetsData), 
    ltasts.generate_assets_layout(buildLayout.assetsData)
])

ltsum.generate_summary_callbacks(app)
ltgr.generate_groups_callbacks(app, buildLayout.groups)
ltasts.generate_assets_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=argumentsValues.d, host=argumentsValues.address, port=argumentsValues.port)
