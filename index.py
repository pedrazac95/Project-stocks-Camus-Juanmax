# dash libraries
from turtle import width
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

#visulization
import plotly.express as px

#from app libraries
from app_divs import sidebar, title

#Create the app
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

#Create Layout
app.layout = dbc.Container(
    [ 
        dbc.Col([sidebar.sidebar], width=3),
        dbc.Col([
            dbc.Row([title.title]),
            dbc.Row(["prueba"]),
            dbc.Row(["prueba"]),

        ], width=9)
        ],
    className="ds4a-app",  # You can also add your own css files by storing them in the assets folder
)

#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port='8050', debug=True)
