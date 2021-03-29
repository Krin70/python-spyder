from fake_useragent import UserAgent
import requests

session = requests.Session()
headers = {
    "User-Agent": UserAgent().chrome
}
login_url = ""
params = {
    "user": "",
    "password": ""
}
response = session.post(login_url, headers=headers, data=params)
info_url = ""
resp = session.get(info_url,headers=headers)
print(resp.text)

