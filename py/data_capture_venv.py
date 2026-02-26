from curl_cffi import requests
import json
import os
from pathlib import Path

with open(os.path.join(Path(__file__).parent.parent, 'data', 'I_url.json')) as jsonFile:
    data = json.load(jsonFile)
    print(data)

class Stock():
    def __init__(self, *, stock_code, **kwargs):
        self.url = data['stock_url']
    
    def initiate_data(self):
        session = requests.Session(impersonate='chrome120')
        

print('data_capture.py')