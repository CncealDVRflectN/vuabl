from plotly.missing_ipywidgets import FigureWidget
from data.size_plot_data import SizePlotData
import plotly.express as px



def plot_groups_sizes_pie(data: SizePlotData) -> FigureWidget:
    return px.pie(
        data.frame, 
        names="group",
        values="size", 
        title=f"Size by group ({data.sizePostfix})", 
        labels={
            "group": "Group", 
            "size": f"Size ({data.sizePostfix})"
        }
    )


def plot_groups_sizes_bars(data: SizePlotData) -> FigureWidget:
    return px.bar(
        data.frame, 
        x="group", 
        y="size", 
        color="colors", 
        title=f"Size by group ({data.sizePostfix})", 
        labels={
            "group": "Groups", 
            "colors": "Groups", 
            "size": f"Size ({data.sizePostfix})"
        }
    )
