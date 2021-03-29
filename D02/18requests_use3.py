from fake_useragent import UserAgent
import requests

url = "httpbin.org/get"

headers = {
    "User-Agent": UserAgent().chrome
}

proxies = {
    "http": "http://user:password@ip:port"
}
resp = requests.get(url, headers=headers, proxies=proxies)
print(resp.text)
