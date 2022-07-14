from logging import PlaceHolder
import dash
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

from datetime import datetime,timedelta
from datetime import datetime as dt

from app_divs.analysis import graph_stock, get_name_of_stock, get_stock_price

###############################################################
# LINE PLOT
###############################################################

stock_code="GOOG"
stock_name= get_name_of_stock(stock_code)
stock_plot=graph_stock(stock_code, datetime.now()-timedelta(days=6*31), datetime.now())
price=get_stock_price(stock_code)
price_cop=get_stock_price_cop(price)

#################################################################################
# Here the layout for the plots to use.
#################################################################################
#################################################################################

stats = html.Div(
    [
        # Place the different graph components here.
        dbc.Row([
            dbc.Col(
                html.H2(
                    stock_name,
                    id="stock_name")),
            dbc.Col(
                html.H2(
                    price,
                    id="stock_price")),
            ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=stock_plot,
                    id="Line")),
            ]
        ),
    ],
    className="ds4a-body",
)

