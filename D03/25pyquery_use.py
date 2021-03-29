from fake_useragent import UserAgent
import requests
from pyquery import PyQuery as pq

url = "https://www.kuaidaili.com/free/"
headers = {
    "User-Agent": UserAgent().random
}
response = requests.get(url, headers=headers)
doc = pq(response.text)
trs = doc("#list tr")
for num in range(1, len(trs)):
    ip = trs.eq(num).find("td").eq(0).text()
    port = trs.eq(num).find("td").eq(1).text()
    type_ = trs.eq(num).find("td").eq(3).text()
    print(ip, ":", port, "-----", type_)
# ips = doc()
# ports = doc()
# types = doc()
