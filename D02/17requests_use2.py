import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().chrome
}
login_url = ""
params = {
    "user": "",
    "password": ""
}
resp = requests.post(login_url, headers=headers, data=params)

print(resp.text)
