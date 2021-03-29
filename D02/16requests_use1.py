import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().chrome
}
url = "https://www.baidu.com/s"
params = {
    "wd": "郑爽"
}
resp = requests.get(url, headers=headers, params=params)

print(resp.text)
