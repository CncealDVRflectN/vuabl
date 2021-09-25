from plotly.missing_ipywidgets import FigureWidget


def apply_figure_dark_theme(figure: FigureWidget):
    figure.update_layout(paper_bgcolor="rgba(0, 0, 0, 0)")
    figure.update_layout(plot_bgcolor="rgba(0, 0, 0, 0)")
    figure.update_layout(font_color="#d8d4d0")


def apply_figure_theme(figure: FigureWidget):
    apply_figure_dark_theme(figure)



def get_data_table_header_dark_theme() -> dict:
    return {
            "backgroundColor": "rgba(0, 0, 0, 0)", 
            "textAlign": "left"
        }


def get_data_table_header_theme() -> dict:
    return get_data_table_header_dark_theme()


def get_data_table_cell_dark_theme() -> dict:
    return {
            "backgroundColor": "rgba(0, 0, 0, 0)", 
            "whiteSpace": "pre-line", 
            "textAlign": "left"
        }


def get_data_table_cell_theme() -> dict:
    return get_data_table_cell_dark_theme()



def get_plot_colors_dark() -> list:
    return ["#ff7d7d", "#ffc77d", "#fff47d", "#84de81", "#71d8e3", "#84ade8", "#dc8de3", 
        "#ffa47d", "#c1f07a", "#7fcdbb", "#b0acfc", "#d2acfa", "#f086d4", "#f582ac", 
        "#ffb8b8", "#f5ee9f", "#87e8b6", "#a6f6ff", "#b8d1f5", "#ebb6f0"]


def get_plot_colors() -> list:
    return get_plot_colors_dark()
