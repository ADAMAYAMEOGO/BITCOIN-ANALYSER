from rates_data_manager import get_and_manage_rates_data
from datetime import date, timedelta


date_end_str = date.today()
date_start_str =date.today()-timedelta(150)
assets = "BTC/EUR"


data= get_and_manage_rates_data(assets,date_start_str,date_end_str)
