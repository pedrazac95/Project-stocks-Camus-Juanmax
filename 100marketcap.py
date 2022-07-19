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
df=df[df['country'].str.contains('USA')].reset_index(drop=True)
df.to_csv("data/top100MC.csv",index=False)


