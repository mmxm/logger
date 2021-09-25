# -*- coding: utf-8 -*-
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import requests
import datetime
import pymongo
import numpy as np

myclient = pymongo.MongoClient("mongodb://localhost:27017/", username='root', password="root")
db = myclient["history"]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__)
app.layout = html.Div(
    html.Div([
        dcc.Graph(id='live-update-text'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
)
@app.callback(Output('live-update-text', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph_live(n):
    # val = db["transfer_cycle"].find_one(sort=[("timestamp", -1)])
    # fig = go.Figure()
    # fig.add_trace(
    #     go.Indicator(
    #         mode="number",
    #         value=val["count"],
    #         title="Cycles",
    #     )
    # )


    fig = make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}
    val = db["transfer_cycle"]\
        .find({"timestamp": {'$gte': datetime.datetime(2021, 9, 25, 00, 46, 00)}}, sort=[("timestamp", -1)])
    data = pd.DataFrame(list(val))
    data = data.groupby(np.arange(len(data)) // 10).mean()

    fig.append_trace({
        'x': data['timestamp'],
        'y': data['count'],
        'name': 'Cycle',
        'mode': 'lines',
        'type': 'scattergl'
    }, 1, 1)
    return fig



if __name__ == '__main__':
    app.run_server(debug=True)