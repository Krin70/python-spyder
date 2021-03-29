from bs4 import BeautifulSoup
from bs4 import Comment

str = '''
<title>尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''

soup = BeautifulSoup(str, "lxml")

print(soup.title)
print(soup.div)

print(soup.div.attrs)
print(soup.div['float'])
print(soup.a['href'])
print(soup.div.string)
print(soup.div.text)

print("-------------test---------------")
print(soup.strong.text)  ##不输出东西
print("-------------/test---------------")
print(type(soup.strong.string))
print(soup.strong.string)

print("-------------test2---------------")
if type(soup.strong.string) == Comment:
    print(soup.strong.string)
    print(soup.strong.prettify())  # 原样显示
else:
    print(soup.strong.text)

print("-------------find_out---------------")
print(soup.find_all("title"))
print(soup.find_all(class_='info'))
print(soup.find_all(attrs={'float': 'left'}))
print(soup.find_all("div", attrs={'float': 'left'}))

print("-------------css---------------")

print(soup.select("title"))
# print(soup.select("#title"))#id选择器
print(soup.select(".info"))#类选择器
print(soup.select("div span"))
print(soup.select("div > span"))
print(soup.select("div")[1].select("a"))
print(soup.select("div")[1].select("a")[0].text)

