import requests
from api_config import API_KEY
import json


BASE_URL = "https://rest.coinapi.io"
url = BASE_URL + "/v1/exchangerate/BTC/USD"

headers = {"X-CoinAPI-Key" : API_KEY}
response = requests.get(url, headers=headers)

value=response.status_code

def test_response(value):
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


if value==200:
    data= json.loads(response.text)
else:
    print("code erreur: ", value)
    test_response(value)
print()