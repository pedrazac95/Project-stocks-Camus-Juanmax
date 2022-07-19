from logging import PlaceHolder
import dash
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc

from datetime import datetime,timedelta
from datetime import datetime as dt

from numpy import set_string_function

from app_divs.analysis import graph_stock, get_name_of_stock, get_stock_price,get_stock_price_cop

###############################################################
# LINE PLOT
###############################################################

stock_code="GOOG"
stock_name= get_name_of_stock(stock_code)
stock_plot, price, growth_potencial, per_gp=graph_stock(stock_code,datetime.now()-timedelta(days=6*31), datetime.now())
price_cop=get_stock_price_cop(stock_code)

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
            dbc.Col([
                dbc.Row(
                    html.H2(
                    str(price) +' USD',
                    id="stock_price")
                    ),
                dbc.Row(
                    html.H2(
                    price_cop,
                    id="stock_price_cop")
                )
            ]),
        ]),
        dbc.Row([
            dbc.Col([html.H3("Growth Potencial:")]),
            dbc.Col(
                html.H3(
                    str(growth_potencial)+' USD',
                    id="growth_pot")
                    ),
            dbc.Col(
                html.H3(
                    str(per_gp) +'%',
                    id="per_growth_pot")
                    )
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    figure=stock_plot,
                    id="Line")),
        ]),
        html.Hr(),
        dbc.Row([
            dbc.Col(
                dcc.Slider(0,6,step=None, value=3,
                marks={
                    0: {'label':'5 days'},
                    1: {'label':'1 Months'},
                    2: {'label':'3 Months'},
                    3: {'label':'6 Months'},
                    4: {'label':'1 Years'},
                    5: {'label':'5 Years'},
                    6: {'label':'All'},
                },
                id="term_slider"
                )
            ),
        ]),
    ],
className="ds4a-body",
)

