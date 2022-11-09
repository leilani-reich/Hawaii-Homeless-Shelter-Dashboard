# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

app = Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# Reading in data / Preprocessing

# Visualizing map of homeless shelters
shelters_df = pd.read_csv('homeless_shelters.csv')

fig1 = px.scatter_mapbox(shelters_df, lat='latitude', lon='longitude', mapbox_style='open-street-map', width=800, zoom=5.8)
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Visualizing chronic homelessness
chronic_homelessness_df = pd.read_csv('chronic_homelessness__2005_to_2019_-1.csv')
chronic_homelessness_count_cols = ['Oahu', 'Hawaii, Maui, and Kauai', 'Total']


# App
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
                    id='fig1',
                    figure=fig1,
                    style={"color": "white"}
                ),  width=8, style={"margin": "auto", "height": "80%"}
        )
    ]),
    
    dbc.Row([
        dbc.Col(
            width=4
        ),
        dbc.Col(
            dcc.Graph(
            id="fig2"
            ), width=8, style={"padding-top": "50px", "height": "30%"}
        )

    ]),

    dbc.Row([
        dbc.Col(
            width=4
        ),
        dbc.Col(
        dcc.Slider(
               min=chronic_homelessness_df['Year'].min(),
               max=chronic_homelessness_df['Year'].max(),
               step=None,
               value=chronic_homelessness_df['Year'].min(),
               marks={str(year): str(year) for year in chronic_homelessness_df['Year'].unique()},
               id='slider-year',
           ), width=8
        )
    ]),
    
    ], className="dbc", fluid=True)

# def get_updated_chart(year):

#     filtered_df = chronic_homelessness_df[chronic_homelessness_df['Year'] == year]
#     print("filtered_df", filtered_df)
#     print("Year", year)
#     fig2 = px.line(filtered_df, x="Year", y=chronic_homelessness_count_cols, markers=True,
#     color_discrete_map={"Total": "red", "Oahu": "orange", "Hawaii, Maui, and Kauai": "blue"}
#     )

#     fig2.update_layout(legend_title='', title="Chronic Homelessness Counts across Hawaiian Islands", 
#     yaxis_title="Counts of Chronically Homeless", hovermode="x unified",
#     paper_bgcolor="#4e5d6c", font=dict(color="white"))
#     fig2.update_traces(hovertemplate='%{y}',  line=dict(width=3))
#     return fig2


@app.callback(
Output('fig2', 'figure'),
Input('slider-year', 'value'),)
def update_graph(value):
    filtered_df = chronic_homelessness_df[chronic_homelessness_df['Year'] <= value]

    fig2 = px.line(filtered_df, x="Year", y=chronic_homelessness_count_cols, markers=True,
    color_discrete_map={"Total": "red", "Oahu": "orange", "Hawaii, Maui, and Kauai": "blue"}
    )

    fig2.update_layout(legend_title='', title="Chronic Homelessness Counts across Hawaiian Islands", 
    yaxis_title="Counts of Chronically Homeless", hovermode="x unified",
    paper_bgcolor="#4e5d6c", font=dict(color="white"))
    fig2.update_traces(hovertemplate='%{y}',  line=dict(width=3))
    fig2.update_xaxes(tickmode="array", tickvals=list(chronic_homelessness_df['Year']))
    return fig2

#app.run_server(debug=True)
if __name__ == '__main__':
    app.run_server(debug=True)
