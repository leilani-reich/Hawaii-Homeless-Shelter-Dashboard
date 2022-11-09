# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


shelters_df = pd.read_csv('homeless_shelters.csv')
#print(hotels_df.head)

fig = px.scatter_mapbox(shelters_df, lat='latitude', lon='longitude', mapbox_style='carto-positron', width=800)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

app.title = 'Hawaii Homelessness Dashboard'

app.layout = dbc.Container(children=[
    html.H1('Homelessness in Hawaii', style={"align": "center"}),

        dbc.Row([
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        "Homelessness is a persisting issue on the Hawaiian Islands."
                    )
                ), width=4
            ),


            dbc.Col(
                dcc.Graph(
                    id='example-graph',
                    figure=fig,
                ),  width=8, style={"margin": "auto"}
        )
    ])], className="dbc", fluid=True)

#app.run_server(debug=True)
if __name__ == '__main__':
    app.run_server(debug=True)
