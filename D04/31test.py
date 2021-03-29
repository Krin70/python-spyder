import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://3w.huanqiu.com/a/5e93e2/41le5nPmtXl?agt=20&tt_group_id=6924570254035124749"

headers = {
    "User-Agent":UserAgent().random
}
response = requests.get(url,headers=headers)
e = etree.HTML(response.text)
title = e.xpath("//h1/text()")
content = e.xpath('''string(//div[@class="a-con"]/p)''')
images_url = e.xpath('''//div[@class="news-item"]//img/@src''')
images_names = e.xpath("")
# print(response.text)
