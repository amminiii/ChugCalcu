import os
from binance import Client
import dotenv
import json

dotenv.load_dotenv()

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("SECRET_KEY")

client = Client(api_key, api_secret)

ticker = 'ALGO'
trades = client.get_my_trades(symbol='ALGOUSDT')
orders = client.get_open_orders(symbol=f'{ticker}USDT')
info = client.get_account()
k = json.dumps(trades,indent=4, sort_keys=True)
status = client.get_account_status()
print(status)