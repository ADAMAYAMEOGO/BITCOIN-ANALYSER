from coinapi_service import get_all_assets, coinapi_get_exchange_rates, test_response_status
from datetime import date, timedelta
import json


date_today_str = date.today().strftime('%Y-%m-%d')
date_start_str = (date.today()-timedelta(10)).strftime('%Y-%m-%d')
assets = "BTC/EUR"
data_filename = assets.replace("/","_")+".json"



def get_json_rates(rates_data):
    return json.dumps([{ "date":d['time_period_start'][0:10], "Value":int(d['rate_close']) } for d in rates_data])

def save_data_to_json_file(json_data, filename):
    with open(filename, 'w') as file:
        file.write(json_data)
        file.close()

rates = coinapi_get_exchange_rates(assets, date_start_str,date_today_str)

if rates:
    json_data= get_json_rates(rates)
    print(assets, "nombres de cours : ", len(rates))
    save_data_to_json_file(json_data, data_filename)
