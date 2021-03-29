from urllib.request import Request
from urllib.request import build_opener
from fake_useragent import UserAgent
from urllib.request import HTTPHandler

url = "https://www.baidu.com/"
headers = {
    "User-Agent": UserAgent().chrome
}
request = Request(url, headers=headers)
handler = HTTPHandler()
opener = build_opener(handler)
response = opener.open(request)
print(response.read().decode())

