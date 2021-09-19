from plotly.missing_ipywidgets import FigureWidget


def apply_figure_dark_theme(figure: FigureWidget):
    figure.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)")
    figure.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)")
    figure.update_layout(font_color="#d8d4d0")



def get_data_table_header_dark_theme() -> dict:
    return {
            "backgroundColor": "rgba(0, 0, 0, 0)", 
            "textAlign": "left"
        }


def get_data_table_cell_dark_theme() -> dict:
    return {
            "backgroundColor": "rgba(0, 0, 0, 0)", 
            "whiteSpace": "pre-line", 
            "textAlign": "left"
        }
