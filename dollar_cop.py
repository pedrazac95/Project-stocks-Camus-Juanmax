import requests
from bs4 import BeautifulSoup
from datetime import datetime,timedelta
import json

site_url='https://www.investing.com/currencies/usd-cop/'
UserAgent= 'Mozilla/5.0' #enmascarando web scrapping


def update_dollar_cop():
    c = requests.get(site_url, headers={'User-Agent': UserAgent})
    s=BeautifulSoup(c.text,'html.parser')
    p_text=s.find_all("span",{'data-test':"instrument-price-last"})[0].text
    cop_rate=p=float(p_text.replace(',',''))
    updated_date=datetime.now().date()
    updated_hour=datetime.now().hour

    dict_price={
        "updated_date":str(updated_date),
        "updated_hour":str(updated_hour),
        "rate_USD_COP":cop_rate
        }
    with open('data/dollar_cop.json', 'w') as json_file:
        json.dump(dict_price, json_file)
    print('updated'+str(dict_price))


def get_dollar_to_cop():
    
    with open('data/dollar_cop.json') as dc:
        dc_update=json.load(dc)

    #dc_update=json.loads(dc_update)

    date_update=datetime.strptime(dc_update["updated_date"], '%Y-%m-%d').date()
    hour_update=int(dc_update["updated_hour"])
    rate=float(dc_update["rate_USD_COP"])

    if date_update == datetime.now().date():
        if hour_update == datetime.now().hour:
            return rate
        else: 
            update_dollar_cop()
            return get_dollar_to_cop()
    else:
        update_dollar_cop()
        return get_dollar_to_cop()
