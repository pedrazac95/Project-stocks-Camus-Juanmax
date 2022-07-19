#
import pandas as pd
from datetime import datetime,timedelta
import json

# dash libraries
from turtle import width
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

#visulization
import plotly.express as px

#from app libraries
from app_divs import sidebar, title, charts, analysis
from dollar_cop import get_dollar_to_cop
stock_pd=pd.read_csv("data/top100MC.csv")

#Create the app
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

#Create Layout
app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='NY Stocks', children=[
            dbc.Container([
                dbc.Row([sidebar.sidebar]),
                # dbc.Row([title.title]),
                dbc.Row([charts.stats]),
                dbc.Row(["prueba"]),
            ])
        ],className="ds4a-body",
        ),

        dcc.Tab(label='Col Stocks', children=[
            dcc.Graph(
                figure={
                    'data': [
                        {'x': [1, 2, 3], 'y': [2, 4, 3],
                            'type': 'bar', 'name': 'SF'},
                        {'x': [1, 2, 3], 'y': [5, 4, 3],
                         'type': 'bar', 'name': u'Montréal'},
                    ]
                }
            )
        ]),
    ])
],className="ds4a-app")



#############################################################
# CHARTS : Add sidebar interaction here
#############################################################

@app.callback(
    [
        Output("stock_name", "children"),
        Output("Line", "figure"),
        Output("stock_price", "children"),
        Output("stock_price_cop", "children"),
        Output("growth_pot", "children"),
        Output("per_growth_pot", "children"),
    ],
    [
        Input("stock_dropdown", "value"),
    ],
)
def change_stock(stock_dropdown="Alphabet (Google)"):
    #name = stock_pd[stock_pd["code"]==stock_code].iloc[0,1]
    code = stock_pd[stock_pd["name"]==stock_dropdown].iloc[0,0]
    stock_name=analysis.get_name_of_stock(code)
    price_cop=analysis.get_stock_price_cop(code)
    line_fig,price,gp,pgp=analysis.graph_stock(code, datetime.now()-timedelta(days=6*31), datetime.now())
    
    return [stock_name,line_fig, str(price)+' USD', price_cop, str(gp)+ ' USD', str(pgp)+ '%']



#Initiate the server where the app will work
if __name__ == "__main__":

    app.run_server(host='0.0.0.0', port='8050', debug=True)


