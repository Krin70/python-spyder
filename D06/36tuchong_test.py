import requests
from fake_useragent import UserAgent
from lxml import etree

url = "https://tuchong.com/3445009/76985017/"
response = requests.get(url, headers={"User-Agent": UserAgent().random})
e = etree.HTML(response.text)
img_url = e.xpath('//img[@class="multi-photo-image"]/@src')

for url in img_url:
    response = requests.get(url, headers={"User-Agent": UserAgent().random})
    img_name = url[url.rfind("/") + 1:]
    with open("img/" + img_name, 'wb') as f:
        f.write(response.content)
