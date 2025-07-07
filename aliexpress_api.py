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
        self._tracking_id = config.get('AliExpress', 'tracking_id')

    def generate_affiliate_link(self, url):
        params = {
            'app_key': self._appkey,
            'tracking_id': self._tracking_id,
            'url': url
        }

        try:
            response = requests.get("https://portals.aliexpress.com/open/service/link/generate", params=params)
            print("🔍 URL Requested:", response.url)
            print("📦 Response Content:", response.text)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": str(e), "details": response.text}
