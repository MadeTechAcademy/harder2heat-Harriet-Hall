
import requests

def get_council_properties_from_api(url):
    res = requests.get(url)
    if res.status_code == 200:
        return (True, res.json())
    return (False, None)