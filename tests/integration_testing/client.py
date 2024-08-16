
import requests

def get_council_properties_from_api(url):
    res = requests.get(url)
    if res.status_code == 200:
        return (True, res.json())
    elif res.status_code == 500:
        return (False, f"Status code: {res.status_code}, Internal Server Error")
    elif res.status_code == 404:
        return (False, f"Status code: {res.status_code}, Not Found")
    return (False, f"Status code: {res.status_code}, Error")
        