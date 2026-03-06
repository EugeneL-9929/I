from curl_cffi import requests
import os
import json
from pathlib import Path
from bs4 import BeautifulSoup

with open(os.path.join(Path(__file__).parent.parent, 'data', 'I_url.json')) as json_file:
    data = json.load(json_file)

class Ratio():
    def __init__(self, *, ratio_name):
        print(f'Ratio {ratio_name}')
        self.url = data['ratio_url'].replace('${ratio_name}', ratio_name)
        self.data = {
            'pe_ttm': None,
            'pb_mrq': None
        }
    
    def update(self, update_data):
        self.data['pe_ttm'] = update_data['pe_ratio_ttm']['value']
        self.data['pb_mrq'] = update_data['price_to_book_mrq']['value']

    def initiate_data(self):
        session = requests.Session(impersonate='chrome120')
        response = session.get(self.url)
        if response.status_code == 200:
            print(f"request status: sucess {response.status_code}")
        else:
            print(f"request status: failed {response.status_code}")
            return
        soup = BeautifulSoup(response.content, 'html.parser')
        script_tag = soup.find('script', id='__NEXT_DATA__')
        data = json.loads(script_tag.get_text())['props']['pageProps']['state']['dividendsStore']['ratios']['indicators']
        self.update(data)


# ratio = Ratio(ratio_name='intel-corp')
ratio = Ratio(ratio_name='apple-computer-inc')
ratio.initiate_data()
print(ratio.data)