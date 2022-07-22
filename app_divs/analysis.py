# datastructures manipulation
import pandas as pd
import numpy as np
from scipy import signal
import json

#get finantial data
import yfinance as yf
import requests
from bs4 import BeautifulSoup

#tools
from datetime import datetime,timedelta

#visualization
import plotly.graph_objects as go

from dollar_cop import get_dollar_to_cop

today_date=datetime.now()

#Standar Selections
y5_early_date= today_date-timedelta(days=5*365) # 5años
y1_early_date= today_date-timedelta(days=1*365)  # 1año
m6_early_date= today_date-timedelta(days=6*31)  # 6meses
m3_early_date= today_date-timedelta(days=3*31) # 3meses
m1_early_date= today_date-timedelta(days=1*31)  # 1mes

stock_pd=pd.read_csv("data/top100MC.csv")

def get_start_date(slider_value):
    
    if slider_value == 3:
        start_date=datetime.now()-timedelta(days=6*31)
    elif slider_value == 0:
        start_date=datetime.now()-timedelta(days=5)
    elif slider_value == 1:
        start_date=datetime.now()-timedelta(days=31)
    elif slider_value == 2:
        start_date=datetime.now()-timedelta(days=3*31)
    elif slider_value == 4:
        start_date=datetime.now()-timedelta(days=365)
    elif slider_value == 5:
        start_date=datetime.now()-timedelta(days=365*5)
    else:
        start_date=datetime.now()-timedelta(days=365*20)
    
    return start_date


def get_name_of_stock(stock_code):
    name = stock_pd[stock_pd["code"]==stock_code].iloc[0,1]
    return str(stock_code)+'-'+str(name)

def get_stock_price(stock_code):
    pd=get_data(stock_code)
    l=len(pd)
    return str(round(pd.loc[l-1,"Close"],3)) + ' USD'

def get_stock_price_cop(stock_code):
    pd=get_data(stock_code)
    l=len(pd)
    price=pd.loc[l-1,"Close"]

    Cop_rate=float(get_dollar_to_cop())
 
    return str(round(price*Cop_rate,2)) + ' COP'


def get_data(stock_code):
    """
    retorna dataframe de los principales precios de el stock que se le indique 
    en un periodo de 5 años
    """
    stock_value_df = yf.download(stock_code, 
                      start=y5_early_date,
                      end=today_date, 
                      progress=False,)
    stock_value_df =pd.DataFrame(stock_value_df).reset_index()

    return stock_value_df 

def filtered_by_date(df,start_date,end_date):
    """
    return a filtered a data frame by its column date with a given range of time
    """
    date_filter=(df['Date'] <= pd.to_datetime(end_date)) & (df['Date'] >= pd.to_datetime(start_date))
    df_=df[date_filter].reset_index(drop=True)
    return df_

def minimuns_2nd_order(df,columna):
    """
    return a dataframe with minimus of second order of a diven series(column) of dataframe
    """
    minimums_indexes_1 = signal.argrelextrema(df[[columna]].to_numpy(), np.less)[0]
    minimums_1=[df[columna].iloc[index] for index in minimums_indexes_1]
    minimums_dates_1=[df['Date'].iloc[index] for index in minimums_indexes_1]
    minimums_df_1=pd.DataFrame(dict(Date=minimums_dates_1,y=minimums_1))

    minimums_indexes_2 = signal.argrelextrema(np.array(minimums_1), np.less)[0]
    minimums_2=[minimums_1[index] for index in minimums_indexes_2]
    indexes_dates_2= [minimums_indexes_1[index] for index in minimums_indexes_2]
    minimums_dates_2=[df['Date'].iloc[index] for index in indexes_dates_2]
    minimums_df_2=pd.DataFrame(dict(Date=minimums_dates_2,y=minimums_2))

    return minimums_df_2


def graph_stock(stock,star_date,end_date):

    df=get_data(stock)
    df_period=filtered_by_date(df,star_date,end_date)
    mean_period=df_period['Close'].mean()
    minimuns_data=minimuns_2nd_order(df_period,'Close')
    mean_minimuns=round(minimuns_data['y'].mean(),3)
   
    l=len(df_period)
    stock_price=round(df_period.loc[l-1,"Close"],3)
    growth_potencial= round(mean_minimuns - stock_price,2)
    per_growth_potencial=round((growth_potencial/ stock_price)*100,2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_period["Date"], y=df_period["Close"],mode='lines+markers', name="Year Close Serie"))
    fig.add_trace(go.Scatter(x=minimuns_data["Date"], y=minimuns_data["y"],mode='lines+markers', name="Local Minimuns 2nd Order"))
    fig.add_hline(y=mean_period, name=" Year mean")
    fig.add_hline(y=mean_minimuns, annotation_text="Minimuns mean", line=dict(color='firebrick', width=4, dash='dash'))
    #fig.write_image("chart.png")
    return (fig, stock_price, growth_potencial,per_growth_potencial) 

#Select Stock code
#stock="AAPL"
#Select period of  time to filter de Df
#end_date=today_date
#start_date=m6_early_date



#graph_stock(stock,start_date,end_date)
