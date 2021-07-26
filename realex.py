import json
import requests

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

bitcoininfo = response.json()

#print(type(bitcoininfo))

print(bitcoininfo['bpi']['EUR']['rate_float'])
