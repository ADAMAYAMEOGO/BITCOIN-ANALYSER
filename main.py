from coinapi_service import get_all_assets, coinapi_get_exchange_rates
from datetime import date, timedelta


date_today_str = date.today().strftime('%Y-%m-%d')
date_ten_left_str = (date.today()-timedelta(10)).strftime('%Y-%m-%d')

#get_all_assets()
datas = coinapi_get_exchange_rates('BTC', date_ten_left_str,date_today_str)
for d in datas:
    print(f"Date: {d['time_period_start'][0:10]} : {int(d['rate_close'])}")