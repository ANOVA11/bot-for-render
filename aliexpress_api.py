import requests
from configparser import ConfigParser
import os

class AliexpressAPI:
    def __init__(self):
        self._read_config()

    def _read_config(self):
        file_path = os.path.join(os.path.dirname(__file__), './config.ini')
        config = ConfigParser()
        config.read(file_path)
        self._appkey = config.get('AliExpress', 'appkey')
        self._tracking_id = config.get('AliExpress', 'trackingId')

    def generate_affiliate_link(self, url):
        params = {
            'app_key': self._appkey,
            'tracking_id': self._tracking_id,
            'urls': url
        }
        response = requests.get("https://portals.aliexpress.com/linkgenerate", params=params)
        return response.json()
