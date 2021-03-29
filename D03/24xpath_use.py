from lxml import etree
import requests
from fake_useragent import UserAgent

headers = {
    "User-Agent": UserAgent().random
}
url = "https://www.qidian.com/rank/yuepiao?style=1"

response = requests.get(url, headers=headers)

e = etree.HTML(response.text)
names = e.xpath('//h4/a/text()')
authors = e.xpath("//p/a[@class='name']/text()")

# for num in range(len(names)):
#     print(names[num], ":", authors[num])

for name, author in zip(names, authors):
    print(name, ":", author)
