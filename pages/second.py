import dash
import pandas as pd
from dash import html, dcc
from dash.dependencies import Input, Output

df = pd.read_csv("data/iris.csv")


class SecondPage:
    def __init__(self, parent):
        self.parent = parent

    def redner(self):
        return [html.Div([
            self.parent,
            html.H1('Second Page'),
            html.P('This is an example paragraph for the second page.'),
        ]),
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
                ]
        )
        ]
