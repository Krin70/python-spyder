from fake_useragent import UserAgent
import requests

url = "https:8owe.cn"

headers = {
    "User-Agent": UserAgent().chrome
}
#关闭警告
requests.packages.urllib3.disable_warnings()
resp = requests.get(url, headers=headers, verify=False)
resp.encoding = "utf-8"
print(resp.text)
