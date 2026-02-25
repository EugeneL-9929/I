from curl_cffi import requests
import json
import os
from pathlib import Path

with open(os.path.join(Path(__file__).parent, 'data', 'I_url.json')) as jsonFile:
    data = json.load(jsonFile)
