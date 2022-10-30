# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


shelters_df = pd.read_csv('homeless_shelters.csv')
#print(hotels_df.head)

fig = px.scatter_mapbox(shelters_df, lat='latitude', lon='longitude', mapbox_style='carto-positron')

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

app.run_server(debug=True)
#if __name__ == '__main__':
#    app.run_server(debug=True)
