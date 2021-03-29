# 案例地址：
# https://blog.csdn.net/m0_49985839/article/details/113354217

import requests
import pandas as pd
from lxml import etree
import re
import os
from fake_useragent import UserAgent

baseUrl = 'http://www.jkl.com.cn/cn/invest.aspx'  # 爬取页面的数据

headers = {
    'User-Agent': UserAgent().random
}
# 1 获取分类模块链接及文件名称
res = requests.get(url=baseUrl, headers=headers).text  # 设置变量接受 基础页的响应数据
# print(res.text)
html = etree.HTML(res)
data_name = html.xpath('//div[@class="infoLis"]//a/text()')  # 投资者列表的名字
data_link = html.xpath('//div[@class="infoLis"]//@href')  # 全部列表的链接
name = [data_name.strip() for data_name in data_name]  # 通过for循环去掉空字符
link = ['http://www.jkl.com.cn/cn/' + data_link for data_link in data_link]  # 拼接拿到列表的各个链接地址
# 合并为字典，方便保存文件
file = dict(zip(name, link))
for name, link in file.items():
    name = name.replace('/', '.')
    name = name.replace('...', '报表')
    # 上面的把文件名带特许字符的 强制转换为我们想要的文本类型
    path = './' + name
    if not os.path.exists(path):
        os.mkdir(path)
        # 建立储存位置
    res_list_url = requests.get(url=link, headers=headers).text
    list_url_html = etree.HTML(res_list_url)
    # print(html_erJi) 解析每个分类的链接
    weiYe = list_url_html.xpath('//a[text()="尾页"]/@href')
    # print(html_weiye)
    # 拿到尾页信息
    if weiYe != []:
        # 正则提取尾页页数
        get_weiYe = re.search("(\d+)'\)", weiYe[0])
        get_yeMa = get_weiYe.group(1)
    else:
        get_yeMa = 1
    # print(get_html_yeMa)  看看是不是提取成功

    for get_yeMa in range(1, int(get_yeMa) + 1):  # 翻页
        yaMa = {
            '__EVENTTARGET': 'AspNetPager1',
            '__EVENTARGUMENT': get_yeMa
        }
        get_erJi_html = requests.get(url=link, headers=headers, params=yaMa).text
        res3 = etree.HTML(get_erJi_html)
        # print(res3)
        pdf_name = res3.xpath('//div[@class="newsLis"]//li/a/text()')
        # print(pdf_name)

        pdf_url = res3.xpath('//div[@class="newsLis"]//li//@href')
        # print(pdf_url)
        pdf_names = [pdf_name.strip() for pdf_name in pdf_name]
        # print(pdf_names)
        """ 处理文件的空数据问题"""
        if all(pdf_url):
            pdf_urls = ['http://www.jkl.com.cn' + pdf_url for pdf_url in pdf_url]
            # print(pdf_url)
            data2 = dict(zip(pdf_names, pdf_urls))
            for s, n in data2.items():
                s = s.replace('/', '.')
                res4 = requests.get(url=n, headers=headers).content
                houzui = n.split('.')[-1]
                pdf_pash = path + '/' + s + '.' + houzui
                # print(pdf_pash)
                with open(pdf_pash, 'wb') as f:
                    f.write(res4)
                    print(s, '下载成功')
