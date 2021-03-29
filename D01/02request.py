from urllib.request import urlopen
from urllib.request import Request

url = "http://www.baidu.com"

#发送请求
response = urlopen(url)
# 读取内容
info = response.read()
#打印内容
# print(info)

# print(info.decode())


##打印状态
# print(response.getcode())
##查看网页是否重定向
# print(response.geturl())
#打印header
print(response.info())