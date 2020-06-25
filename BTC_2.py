import requests
import pandas as pd
import json

url = 'https://pro-api.coinmarketcap.com/v1/criptocurrency/listings/'
headers = {'X-CMC_PRO_API_KEY':'3b8c41f4-e22f-4afc-926f-148cefac8d20'}

response = requests.get(url,headers=headers)

headers = {
  'Accepts': 'application/json',
 # 'X-CMC_PRO_API_KEY': '3b8c41f4-e22f-4afc-926f-148cefac8d20',
}

#print(response.json())

print(response.status_code)







