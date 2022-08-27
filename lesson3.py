import datetime
import requests

print(datetime.datetime.now())
response = requests.get("https://github.com")
if response.status_code == 200:
    print("github is up & running")


def check(url):
    if requests.get(url).status_code == 200:
        print(url, "is up & running")
    else:
        print("site is down")


check("https://github.com")
