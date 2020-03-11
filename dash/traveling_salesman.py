from math import hypot
from math import factorial
from itertools import permutations


import pandas as pd
import numpy as np
from string import ascii_uppercase

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

np.random.seed(1)
N = 11


def distance(points):
    dist = 0
    last = points[-1]
    for point in points:
        dist += hypot(point['x'] - last['x'], point['y'] - last['y'])
        last = point
    return dist


def solve(points):
    perm = permutations(points)
    shortest_dist = None

    for route in perm:
        dist = distance(route)

        if shortest_dist is None or dist < shortest_dist:
            shortest_dist = dist
            yield shortest_dist, route


def get_data():

    p = np.random.randint(0, 100, (N, 2))
    points = []
    for i, (x, y) in enumerate(p):
        points.append({'name': ascii_uppercase[i], 'x': x, 'y': y})

    return points


points = get_data()
print(factorial(len(points)))
solution = [solve(points)]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

graph = dcc.Graph(
        id='ts-graph',
        style={
            'height': 800
        }
    )

app.layout = html.Div(children=[
    html.H1(children='Traveling Salesman'),
    html.Div(children='''
        Traveling Salesman problem in Dash.
    '''),
    graph,
    html.Button('Reset', id='button'),
    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )

])


def create_figure(solution):
    try:
        d, points_sol = next(solution, [None, None])
    except ValueError:
        return None

    if d is None:
        return None

    print("next")

    df = pd.DataFrame(points_sol)
    figure = {

        'layout': {
            'title': 'Traveling Salesman Visualization'
        }
    }

    data = [
        {'x': df['x'], 'y': df['y'], 'text': df['name'], 'type': 'scatter'},  # 'line': dict(color='red', width=1)
    ]

    figure['data'] = data
    return figure


figure = [create_figure(solution[0])]

@app.callback(
    dash.dependencies.Output('button', 'style'),
    [dash.dependencies.Input('button', 'n_clicks')])
def update_output(n_clicks):
    solution[0] = solve(points)
    print("reset")
    return {}


@app.callback(Output('ts-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    last = figure[0]
    tmp = create_figure(solution[0])
    if tmp is not None:
        figure[0] = tmp
    return last

if __name__ == '__main__':
    app.run_server(debug=True)
