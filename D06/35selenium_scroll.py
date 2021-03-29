from time import sleep

from selenium import webdriver
from lxml import etree

url = "https://search.jd.com/Search?keyword=macbook&enc=utf-8&wq=macbook&pvid=aec614d5ba004f17a26ae472bdb05f41"

chrome = webdriver.Chrome()

chrome.get(url)
num = 1
while True:
    print("-------------------第" + str(num) + "页---------------------")
    js = "document.documentElement.scrollTop=110000"
    chrome.execute_script(js)
    num += 1
    sleep(5)
    html = chrome.page_source
    e = etree.HTML(html)
    prices = e.xpath('//div[@class="p-price"]//i/text()')
    names = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')
    print(len(names))
    for name, price in zip(names, prices):
        print(name.xpath("string(.)"), ":", price)

    if e.xpath('//a[@class="pn-next"]') is not None:
        chrome.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[9]').click()
    else:
        break
