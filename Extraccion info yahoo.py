import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import plotly.express as px
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL #, ClientsideFunction
import dash_bootstrap_components as dbc


aapl_df = yf.download('AAPL', 
                      start='2020-01-01', 
                      end='2022-04-29', 
                      progress=False,
)
aapl_df = aapl_df.reset_index()

nvda_df = yf.download('NVDA', 
                      start='2020-01-01', 
                      end='2022-04-29', 
                      progress=False,
)
nvda_df = nvda_df.reset_index()


fb_df = yf.download('FB', 
                      start='2020-01-01', 
                      end='2022-04-29', 
                      progress=False,
)

fb_df = fb_df.reset_index()

fig = px.line(aapl_df, x="Date", y=["Close",'Open','Low', 'High'], title='AAPL Stock Close Value')
fig1 = px.line(fb_df, x="Date", y=["Close",'Open','Low', 'High'], title='FB Stock Close Value')
fig2 = px.line(nvda_df, x="Date", y=["Close",'Open','Low', 'High'], title='NVDA Stock Close Value')



app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY],
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

#Create Layout
app.layout = dbc.Container([
    
    dbc.Row([
    html.H2("YahooStocks", id='title'),  #Creates the title of the app])
    dcc.Graph(figure=fig1,id='STOCK 1'),
    dcc.Graph(figure=fig2,id='STOCK 2'),
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)

