from urllib.error import URLError
from urllib.request import Request, urlopen
from fake_useragent import UserAgent

url = "https://8owe.com/111page/100/"

headers = {
    "User-Agent":UserAgent().chrome
}
try:
    req = Request(url,headers=headers)
    resp = urlopen(req)
    info = resp.read().decode()
    print(info)
except URLError as e:
    if e.args == ():
        print(e)
    else:
        print(e.args[0].errno)
print("访问完成")