from urllib.request import Request, build_opener
from fake_useragent import UserAgent
from urllib.request import ProxyHandler

url = "http://httpbin.org/get"
headers = {
    "User-Agent": UserAgent().chrome
}
request = Request(url, headers=headers)
# handler = ProxyHandler({"http": "username:password@ip:port"})
handler = ProxyHandler({"http": "120.83.108.195:9999"})
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())
