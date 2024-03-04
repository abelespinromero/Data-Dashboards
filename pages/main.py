import dash
from dash import html, dcc
from dash.dependencies import Input, Output


class MainPage:
    def __init__(self, parent):
        self.parent = parent

    def redner(self):
        return html.Div([
            self.parent,
            html.Div(
                children=[   
                    html.H1('Dataers TFG 2024', style={'textAlign': 'center'}),
                    html.P('This is an example paragraph for the Main page.', style={'textAlign': 'center'}),
                ]
            )
        ])
