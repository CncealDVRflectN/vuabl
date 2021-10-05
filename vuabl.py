from dash import Dash, html
from data.build_layout import BuildLayout
import parsing.build_layout as pblt
import layouts.environment as ltenv
import layouts.summary as ltsum
import layouts.group as ltgr
import layouts.assets as ltasts
import os
import sys



buildLayoutPath: str = os.path.abspath(sys.argv[1])
buildLayout: BuildLayout = pblt.read_build_layout(buildLayoutPath)

app: Dash = Dash(__name__)

app.layout = html.Div(children=[
    ltenv.generate_environment_layout(buildLayout.environment), 
    ltsum.generate_summary_layout(buildLayout), 
    ltgr.generate_groups_layout(buildLayout.groups, buildLayout.assetsData), 
    ltasts.generate_assets_layout(buildLayout.assetsData)
])

ltsum.generate_summary_callbacks(app)
ltgr.generate_groups_callbacks(app, buildLayout.groups)
ltasts.generate_assets_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True)
