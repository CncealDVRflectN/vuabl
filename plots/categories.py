from plotly.missing_ipywidgets import FigureWidget
from data.size_plot_data import SizePlotData
import plotly.express as px



def plot_categories_sizes_pie(data: SizePlotData) -> FigureWidget:
    return px.pie(
        data.frame, 
        names="category", 
        values="size", 
        title=f"Size by category ({data.sizePostfix})", 
        labels={
            "category": "Category", 
            "size": f"Size ({data.sizePostfix})"
        }
    )


def plot_categories_sizes_bars(data: SizePlotData) -> FigureWidget:
    return px.bar(
        data.frame, 
        x="category", 
        y="size", 
        color="colors", 
        title=f"Size by category ({data.sizePostfix})", 
        labels={
            "category": "Category", 
            "colors": "Categories", 
            "size": f"Size ({data.sizePostfix})"
        }
    )
