from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent

args = {
    "wd": "郑爽",
    "ie": "utf-8"
}

url = "https://www.baidu.com/s?wd={}".format(urlencode(args))
headers = {
    "User-Agent": UserAgent().random
}

request = Request(url, headers=headers)

response = urlopen(request)



print(response.read().decode())
