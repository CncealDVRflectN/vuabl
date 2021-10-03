from networkx import Graph
from plotly.missing_ipywidgets import FigureWidget
import networkx.drawing.nx_pydot as nxdot
import plotly.graph_objects as go
import utils.theming as theming


def build_dependencies_graph(graph: Graph) -> FigureWidget:
    positions: dict = nxdot.graphviz_layout(graph, prog="sfdp")

    for index, position in positions.items():
        graph.nodes[index]["pos"] = position

    graphs: list[FigureWidget] = []

    for node0, node1, data in graph.edges(data=True):
        x0, y0 = graph.nodes[node0]["pos"]
        x1, y1 = graph.nodes[node1]["pos"]
        width = 0.5 * min(graph.nodes[node0]["scale"], graph.nodes[node1]["scale"])
        color = data["color"]
        
        edgeFigure: FigureWidget = go.Scatter(
            x=[x0, x1, None], 
            y=[y0, y1, None], 
            mode="lines", 
            line=dict(width=width, color=color)
        )

        graphs.append(edgeFigure)

    nodeX: list[float] = []
    nodeY: list[float] = []
    labels: list[str] = []
    scales: list[float] = []

    for node in graph.nodes():
        x, y = graph.nodes[node]["pos"]
        scale = graph.nodes[node]["scale"]
        size = graph.nodes[node]["size"]

        nodeX.append(x)
        nodeY.append(y)
        scales.append(scale)
        labels.append(f"{node}<br>{size}")

    nodes: FigureWidget = go.Scatter(
        x=nodeX, 
        y=nodeY, 
        text=labels, 
        mode="markers", 
        hoverinfo="text", 
        marker=dict(size=scales)
    )

    graphs.append(nodes)

    dependenciesGraph: FigureWidget = go.Figure(data=graphs)

    theming.apply_figure_theme(dependenciesGraph)

    dependenciesGraph.update_layout(showlegend=False)
    dependenciesGraph.update_xaxes(showgrid=False, showticklabels=False, zeroline=False)
    dependenciesGraph.update_yaxes(showgrid=False, showticklabels=False, zeroline=False)

    return dependenciesGraph
