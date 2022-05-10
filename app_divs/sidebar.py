# Basics Requirements
import pathlib
import os
from re import S
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Data
import json
from datetime import datetime as dt
import pandas as pd
from datetime import datetime,timedelta

# Recall app
#from app import app

####################################################################################
# Add the DS4A_Img
####################################################################################
"""
DS4A_Img = html.Div(
    children=[
        html.Img(
            src=app.get_asset_url("c1_logo_tagline.svg"),
            id="ds4a-image",
        )
    ],
)
"""
#############################################################################
# Stock Dropdown Card
#############################################################################
stock_pd=pd.read_csv("data/top100MC.csv")
stocks_list=stock_pd['name'].to_list()
dropdown=dcc.Dropdown(
        id="stock_dropdown",
        options=stocks_list
        )
##############################################################################
# Date Picker Card
##############################################################################


date_picker=dcc.DatePickerRange(
                id='date_picker',
                min_date_allowed=datetime.now()-timedelta(days=5*365),
                max_date_allowed=datetime.now(),
                start_date=datetime.now()-timedelta(days=3*31),
                end_date=datetime.now()
            )


#############################################################################
# Sidebar Layout
#############################################################################
sidebar = html.Div(
    [
        #DS4A_Img,  # Add the DS4A_Img located in the assets folder
        html.Hr(),html.Hr(),html.Hr(),
        html.H5("Select the stock you want to analyse"),
        dropdown,
        html.Hr(),html.Hr(),html.Hr(),html.Hr(),html.Hr(),html.Hr(),
        html.Hr(),html.Hr(),html.Hr(),html.Hr(),html.Hr(),html.Hr(),
        html.H5("Pick the dates"),
        date_picker,

    ],
    className="ds4a-sidebar",
)