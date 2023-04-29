from coinapi_service import coinapi_get_exchange_rates_extended
from datetime import date, timedelta
import json
from pathlib import Path


date_end_str = date.today()
date_start_str =date.today()-timedelta(150)
assets = "BTC/EUR"
data_filename = assets.replace("/","_")+".json"

rates = coinapi_get_exchange_rates_extended(assets, date_start_str, date_end_str)
print()
def get_json_rates(rates_data):
    return json.dumps([{ "date":d['time_period_start'][0:10], "Value":int(d['rate_close']) } for d in rates_data])


def save_data_to_json_file(json_data, filename):
    with open(filename, 'w') as file:
        file.write(json_data)
        file.close()


def load_json_data_from_file(data_filename_to_load):
    with open(data_filename_to_load, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("Le fichier est vide ou contient des données JSON non valides.")
            return []

if Path(data_filename).is_file():
    #Json File exist
    rates= load_json_data_from_file(data_filename)

if rates:
    save_data_date_start_str = rates[0]["date"]
    save_data_date_end_str = rates[-1]["date"]
    print(save_data_date_end_str, save_data_date_start_str)
else:
    #Json File don't exist
    rates = coinapi_get_exchange_rates_extended(assets, date_start_str,date_end_str)
    if rates:
        json_data= get_json_rates(rates)
        print(assets, "nombres de cours : ", len(rates))
        save_data_to_json_file(json_data, data_filename)

