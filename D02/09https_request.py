from urllib.request import Request,urlopen
from fake_useragent import UserAgent
import ssl

context = ssl._create_unverified_context()

url = "https://www.12306.cn/index/"
headers = {
    "User-Agent":UserAgent().chrome
}
requset = Request(url,headers=headers)
reponse = urlopen(requset,context=context)
info = reponse.read().decode()
print(info)