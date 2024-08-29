import dash
from dash import dcc
from dash import html


app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'Data':[
                    {'x':[1,2,3], 
                     'y':[4,1,2], 
                     'type': "bar", 
                     'name': 'bar chart'
                    },
                    {'x':[1,2,3], 
                     'y':[4,1,2], 
                     'type': "line", 
                     'name': 'line chart'
                    },
                ],
                'layout': {
                    'title': "graph title",
                    'xaxis': {'title': 'x-axis'},
                    'yaxis': {'title': 'y-axis'}
                }
            }
        )
    ]
)


if __name__ == "__#file_name__":
    app.run_server(debug=True)

