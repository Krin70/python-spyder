from fake_useragent import UserAgent
import requests
from lxml import etree
import pymysql

url = "http://datachart.500.com/ssq/"
response = requests.get(url, headers={"User-Agent": UserAgent().random})
e = etree.HTML(response.text)
data_times = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]')
client = pymysql.connect(host="master", port=3306, user='root', password='123456', charset='utf8', db='spyder')
cursor = client.cursor()
sql = 'insert into t_ball values(0,%s,%s,%s)'
select_new_sql = "select * from t_ball where date_time = %s"
data_times.reverse()
# 记录有多少条新数据
index = 0
for data_time in data_times:
    result = cursor.execute(select_new_sql, [data_time])
    if result == 1:
        break
    index += 1
print(index)
trs.reverse()
for data_times, tr in zip(data_times, trs):
    red_ball = "-".join(tr.xpath('./td[@class="chartBall01"]/text()'))
    blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')[0]
    print("第" + data_times + "期，红球是：" + red_ball + "蓝球是：" + blue_ball)
    cursor.execute(sql, [data_times, red_ball, blue_ball])
    client.commit()

# 关闭光标对象
cursor.close()
# 关闭数据库连接
client.close()

# 不完善的地方在于。每次有更新以后都会重复扒曲整个页面的数据。然后记住到数据库当中。
