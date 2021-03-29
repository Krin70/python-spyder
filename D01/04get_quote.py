from urllib.request import Request, urlopen
from urllib.parse import quote


# url = "https://www.baidu.com/s?wd=郑爽"#不转马的话会出现UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)

url = "https://www.baidu.com/s?wd={}".format(quote("郑爽"))

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}

request = Request(url, headers=headers)

response = urlopen(request)

print(response.read().decode())
