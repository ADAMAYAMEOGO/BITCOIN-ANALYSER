from coinapi_config import BASE_URL, API_KEY
import json, requests
from datetime import timedelta


headers = {"X-CoinAPI-Key" : API_KEY}



def test_response_status(value):
    match value:
        case 404:
            print("The requested order was not found.")
        case 400:
            print("Bad Request -- There is something wrong with your reques")
        case 401:
            print("Unauthorized -- Your API key is wrong")
        case 403:
            print("Forbidden -- Your API key doesnt't have enough privileges to access this resource")
        case 429:
            print("Too many requests -- You have exceeded your API key rate limits") 
    return value

def get_date_intervalle(date_start, date_end, max_days):
    date_intervals = []
    current_date = date_start

    while current_date < date_end:
        next_date = current_date + timedelta(days=max_days)
        if next_date > date_end:
            next_date = date_end
        date_intervals.append((current_date, next_date))
        current_date = next_date

    return date_intervals


def coinapi_get_exchange_rates(assets, time_start, time_end):
    time_end_str = time_end.strftime('%Y-%m-%d')
    time_start_str = time_start.strftime('%Y-%m-%d')
    url = BASE_URL + f'/v1/exchangerate/{assets}/history?period_id=1DAY&time_start={time_start_str}T00:00:00&time_end={time_end_str}T00:00:00'
    headers = {'X-CoinAPI-Key' : API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        print("Quota restant : ", response.headers["x-ratelimit-remaining"])
        return json.loads(response.text)
    else:
        test_response_status(response.status_code)
        return None


def coinapi_get_exchange_rates_extended(assets, time_start, time_end):
    date_intervals=get_date_intervalle(time_start, time_end, 100)
    rates = []
    if date_intervals:
        for i in date_intervals:
            rates+= coinapi_get_exchange_rates(assets, i[0], i[1])
    
    return rates

def get_all_assets():
    url = BASE_URL + "/v1/assets"
    response = requests.get(url, headers=headers)
    value=response.status_code
    if value==200:
        data= json.loads(response.text)
    else:
        print("code erreur: ", value)
        test_response_status(value)

    for i in range(10):
        print(data[i]["asset_id"], ":", data[i]["name"])


