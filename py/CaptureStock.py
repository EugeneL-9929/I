from curl_cffi import requests
import json
import os
from pathlib import Path
import time

with open(os.path.join(Path(__file__).parent.parent, 'data', 'I_url.json')) as json_file:
    data = json.load(json_file)

class Stock():
    def __init__(self, *, symbol, **kwargs):
        print(f'Stock {symbol}')
        self.url = data['stock_url']
        self.params = {
            'symbol': symbol,
            'resolution': 'D', # 5, 15, 30, 60, 240, 300, D, W, M
            'from_': 0,
            'to': int(time.time())}
        self.params.update(**kwargs)
        self.data = {
            'timestamp': None, 
            'open': None, 
            'close': None, 
            'high': None, 
            'low': None, 
            'volume': None}
    
    def update(self, update_data):
        self.data['timestamp'] = update_data['t']
        self.data['open'] = update_data['o']
        self.data['close'] = update_data['c']
        self.data['high'] = update_data['h']
        self.data['low'] = update_data['l']
        self.data['volume'] = update_data['v']

    def initiate_data(self):
        session = requests.Session(impersonate='chrome120')
        self.params = {**self.params, 'from': self.params.pop('from_')}
        response = session.get(self.url, params=self.params, timeout=30)
        self.params = {**self.params, 'from_': self.params.pop('from')}
        if response.status_code == 200:
            print(f"request status: sucess {response.status_code}")
        else:
            print(f"request status: failed {response.status_code}")
            return
        json_data = response.json()
        self.update(json_data)

    def request_data(self, **kwargs):
        self.params.update(**kwargs)
        session = request.Session(impersonate='chrome120')
        self.params = {**self.params, 'from': self.params.pop('from_')}
        response = session.get(self.url, params=self.params, timeout=30)
        self.params = {**self.params, 'from_': self.params.pop('from')}
        if response.status_code == 200:
            print(f"request status: sucess {response.status_code}")
        else:
            print(f"request status: failed {response.status_code}")
            return
        json_data = response.json()
        self.update(json_data)


stock = Stock(symbol=651)
stock.initiate_data()