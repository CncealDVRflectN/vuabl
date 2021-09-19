from dash import Dash
from parsing.build_layout import *
from layouts.summary import *
from layouts.environment import *
from layouts.group import *
import dash_html_components as html
import os
import sys



buildLayoutPath: str = os.path.abspath(sys.argv[1])
print(f"Build layout path: {buildLayoutPath}")

buildLayout: BuildLayout = read_build_layout(buildLayoutPath)

app: Dash = Dash(__name__)

app.layout = html.Div(children=[
    generate_environment_layout(buildLayout.environment), 
    generate_summary_layout(buildLayout), 
    generate_groups_layout(buildLayout.groups)
])

generate_summary_callbacks(app)
generate_groups_callbacks(app, buildLayout.groups)

if __name__ == "__main__":
    app.run_server(debug=True)
