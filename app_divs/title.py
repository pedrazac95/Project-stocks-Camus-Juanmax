# Basics Requirements
import pathlib
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL

# Dash Bootstrap Components
import dash_bootstrap_components as dbc

# Recall app
#from app import app


title = dbc.Row(
    className="ds4a-title", children=[html.H1("TOP NY STOCKS")], id="title"
)
