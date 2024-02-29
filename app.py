import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output, ClientsideFunction
from dash import dcc, html, Input, Output, ClientsideFunction
import numpy as np
import pandas as pd
import datetime
from datetime import datetime as dt
import pathlib

# Create dash app
app = dash.Dash(__name__)
app.title = 'Dash App'

server = app.server
app.config.suppress_callback_exceptions = True


df = pd.read_csv('data/iris.csv')

def description_card():
    """
    :return: A Div containing dashboard title & descriptions.
    """
    return html.Div(
        id="description-card",
        children=[
            html.H5("Test Dashboard"),
            html.H3("Welcome to DATAERS"),
            html.Div(
                id="intro",
                children="Ejemplo de como hacer algo.",
            ),
        ],
    )

def generate_control_card():
    """
    :return: A Div containing controls for graphs.
    """
    return html.Div(
        id="control-card",
        children=[
            html.P("Select the species:"),
            dcc.Dropdown(
                id="dropdown-species",
                options=[{"label": i, "value": i} for i in df['variety'].unique()],
                value=df['variety'].unique()[0],
                clearable=False,
            ),
            html.P("Select the x-axis:"),
            dcc.Dropdown(
                id="dropdown-x",
                options=[{"label": i, "value": i} for i in df.columns[:-1]],
                value=df.columns[0],
                clearable=False,
            ),
            html.P("Select the y-axis:"),
            dcc.Dropdown(
                id="dropdown-y",
                options=[{"label": i, "value": i} for i in df.columns[:-1]],
                value=df.columns[1],
                clearable=False,
            ),
        ],
    )
    
def generate_table_row(id, style, col1, col2, col3):
    """ Generate table rows.

    :param id: The ID of table row.
    :param style: Css style of this row.
    :param col1 (dict): Defining id and children for the first column.
    :param col2 (dict): Defining id and children for the second column.
    :param col3 (dict): Defining id and children for the third column.
    """

    return html.Div(
        id=id,
        className="row table-row",
        style=style,
        children=[
            html.Div(
                id=col1["id"],
                style={"display": "table", "height": "100%"},
                className="two columns row-department",
                children=col1["children"],
            ),
            html.Div(
                id=col2["id"],
                style={"textAlign": "center", "height": "100%"},
                className="five columns",
                children=col2["children"],
            ),
            html.Div(
                id=col3["id"],
                style={"textAlign": "center", "height": "100%"},
                className="five columns",
                children=col3["children"],
            ),
        ],
    )


def generate_table_row_helper(department):
    """Helper function.

    :param: department (string): Name of department.
    :return: Table row.
    """
    return generate_table_row(
        department,
        {},
        {"id": department + "_department", "children": html.B(department)},
        {
            "id": department + "wait_time",
            "children": dcc.Graph(
                id=department + "_wait_time_graph",
                style={"height": "100%", "width": "100%"},
                className="wait_time_graph",
                config={
                    "staticPlot": False,
                    "editable": False,
                    "displayModeBar": False,
                },
                figure={
                    "layout": dict(
                        margin=dict(l=0, r=0, b=0, t=0, pad=0),
                        xaxis=dict(
                            showgrid=False,
                            showline=False,
                            showticklabels=False,
                            zeroline=False,
                        ),
                        yaxis=dict(
                            showgrid=False,
                            showline=False,
                            showticklabels=False,
                            zeroline=False,
                        ),
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                    )
                },
            ),
        },
        {
            "id": department + "_patient_score",
            "children": dcc.Graph(
                id=department + "_score_graph",
                style={"height": "100%", "width": "100%"},
                className="patient_score_graph",
                config={
                    "staticPlot": False,
                    "editable": False,
                    "displayModeBar": False,
                },
                figure={
                    "layout": dict(
                        margin=dict(l=0, r=0, b=0, t=0, pad=0),
                        xaxis=dict(
                            showgrid=False,
                            showline=False,
                            showticklabels=False,
                            zeroline=False,
                        ),
                        yaxis=dict(
                            showgrid=False,
                            showline=False,
                            showticklabels=False,
                            zeroline=False,
                        ),
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                    )
                },
            ),
        },
    )


app.layout = html.Div(
    id="app-container",
    children=[
        # Banner
        html.Div(
            id="banner",
            className="banner",
            children=[html.Img(src=app.get_asset_url("plotly_logo.png"))],
        ),
        # Left column
        html.Div(
            id="left-column",
            className="four columns",
            children=[description_card(), generate_control_card()]
            + [
                html.Div(
                    ["initial child"], id="output-clientside", style={"display": "none"}
                )
            ],
        ),
        # Right column
        html.Div(
            id="right-column",
            className="eight columns",
            children=[
                # Patient Volume Heatmap
                dcc.Graph(
                id='scatter-plot',
                figure={
                    'data': [
                        {
                            'x': df['sepal.length'],
                            'y': df['sepal.width'],
                            'mode': 'markers',
                            'marker': {
                                'color': 'blue',
                                'size': 10,
                                'opacity': 0.8
                            }
                        }
                    ],
                    'layout': {
                        'xaxis': {
                            'title': 'Longitud del sépalo'
                        },
                        'yaxis': {
                            'title': 'Ancho del sépalo'
                        },
                        'hovermode': 'closest'
                    }
                }
            )

            ],
        ),
    ],
)


# Run the server
if __name__ == "__main__":
    app.run_server(debug=True)