import requests


def get_location():
    url = "https://api.homebuddy.com/api/coordinates-by-ip"
    resp = requests.get(url)
    resp_body = resp.json()
    location = resp_body["data"]["location"]
    return location
