import dash
from dash import html, dcc
from dash.dependencies import Input, Output
from pages import MainPage, SecondPage

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

navbar = html.Div(
    [
        html.Div(  # Container for logo and spacer
            id="banner",
            className="banner",
            children=[
                html.Img(src=app.get_asset_url("uab.png")),
                html.Div(style={"width": "20px"}),  # Space between logo and links
            ],
            style={
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",  # Center logo horizontally
            },
        ),
        html.Div(  # Container for links
            children=[
                dcc.Link('Home', href='/'),
                html.Div(style={"width": "20px"}),  # Spacer between links
                dcc.Link('Data Visualizations', href='/page-1'),
                html.Div(style={"width": "20px"}),  # Spacer between links
                dcc.Link('Conclusions', href='/page-2'),
                html.Div(style={"width": "20px"}),  # Spacer between links
                dcc.Link('FAQ', href='/page-3'),
            ],
            style={
                "display": "flex",
                "flex-direction": "row",
                "align-items": "center",  # Center links vertically
            },
        ),
    ],
    style={  # Style for the entire navbar
        "display": "flex",
        "flex-direction": "row",
        "justify-content": "space-between",  # Distribute links evenly
        "margin-bottom": "10px",
    },
)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return SecondPage(navbar).redner()
    else:
        return MainPage(navbar).redner()


if __name__ == '__main__':
    app.run_server(debug=True)
