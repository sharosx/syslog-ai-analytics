import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Syslog AI Analytics Dashboard'),
    dcc.Graph(id='log-graph'),
])

@app.callback(
    Output('log-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    df = pd.read_csv('data/processed/logs.csv')
    figure = {
        'data': [{'x': df.index, 'y': df['log'], 'type': 'line', 'name': 'logs'}],
        'layout': {'title': 'Syslog Data'}
    }
    return figure

if __name__ == '__main__':
    app.run_server(debug=True)
