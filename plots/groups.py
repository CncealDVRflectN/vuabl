from plotly.missing_ipywidgets import FigureWidget
from data.size_plot_data import SizePlotData
import plotly.graph_objects as go



def plot_groups_sizes_pie(data: SizePlotData) -> FigureWidget:
    figure: FigureWidget = go.Figure(go.Pie(labels=data.frame["group"], values=data.frame["size"], name=""))
    
    figure.update_layout(title_text=f"Size by group ({data.sizePostfix})")
    figure.update_traces(hovertemplate=f"Group: %{{label}}<br>Size: %{{value}}{data.sizePostfix}")

    return figure


def plot_groups_sizes_bars(data: SizePlotData) -> FigureWidget:
    figure: FigureWidget = go.Figure()

    for index, row in data.frame.iterrows():
        figure.add_trace(go.Bar(x=[row["group"]], y=[row["size"]], name=row["group"]))

    figure.update_layout(title_text=f"Size by group ({data.sizePostfix})")
    figure.update_traces(hovertemplate=f"Group: %{{label}}<br>Size: %{{value}}{data.sizePostfix}")
    figure.update_traces(texttemplate=f"%{{y:.2f}}{data.sizePostfix}", textposition="auto")

    return figure
