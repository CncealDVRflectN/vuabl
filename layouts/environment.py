from dash_html_components.H2 import H2
from data.environment import *
import dash_html_components as html



def generate_environment_layout(environment: Environment) -> html.Div:
    return html.Div([
        html.H1("Environment"),
        html.P(f"Unity Version: {environment.unityVersion}"), 
        html.P(f"Addressables Version: {environment.addressablesPackageVersion}")
    ])