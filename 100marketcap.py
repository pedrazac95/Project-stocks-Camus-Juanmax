#python data structures
import pandas as pd

#webscrapping
import requests
from bs4 import BeautifulSoup 
#import urllib 


site_url='https://companiesmarketcap.com/'
UserAgent= 'Mozilla/5.0' #enmascarando web scrapping
c = requests.get(site_url, headers={'User-Agent': UserAgent})
s=BeautifulSoup(c.text,'html.parser')

#r=urllib.request.urlopen(site_url)
#c=r.read().decode('utf-8')

#extrae codigo de la compañia
company_code_top100_div=s.find_all("div",{'class':"company-code"})
company_code_top100=[]
for _ in company_code_top100_div:
    company_code_top100.append(_.text)

#extrae nombre de la compañia
company_name_top100_div=s.find_all("div",{'class':"company-name"})
company_name_top100=[]
for _ in company_name_top100_div:
    company_name_top100.append(_.text)

#extrae pais de la compañia
country_top100_div=s.find_all("span",{'class':"responsive-hidden"})
country_top100=[]
for _ in country_top100_div:
    country_top100.append(_.text)
country_top100.remove(country_top100[0])

#crear DataFrame de las 100 copañias

data={'code':company_code_top100,'name':company_name_top100,'country':country_top100 }
df=pd.DataFrame(data)
df=df[df['country'].str.contains('USA')].reset_index()
df.to_csv("data/top100MC.csv",index=False)



"""
import plotly.express as px
from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL #, ClientsideFunction
import dash_bootstrap_components as dbc
"""
"""
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

"""