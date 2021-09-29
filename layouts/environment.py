from dash import html
from data.environment import *



def generate_environment_layout(environment: Environment) -> html.Div:
    return html.Div([
        html.H1("Environment"),
        html.P(f"Unity Version: {environment.unityVersion}"), 
        html.P(f"Addressables Version: {environment.addressablesPackageVersion}")
    ])