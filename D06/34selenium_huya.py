from time import sleep

from selenium import webdriver


def turnToDigist(str):
    if "万" in str:
        return float(str[:-1]) * 10000
    else:
        return int(str)


driver = webdriver.Chrome()
url = "https://www.huya.com/g/lol"
driver.get(url)
num = 1
sum_DJ = 0
sum_audience = 0
while True:
    print("-------------------第" + str(num) + "页---------------------")
    num += 1
    sleep(5)
    html = driver.page_source
    names = driver.find_elements_by_xpath('//i[@class="nick"]')
    counts = driver.find_elements_by_xpath('//i[@class="js-num"]')
    sum_DJ = sum_DJ + len(names)
    for name, count in zip(names, counts):
        print(name.text, ":", count.text)
        sum_audience = sum_audience + turnToDigist(count.text)
    if driver.page_source.find("laypage_next") != -1:
        driver.find_element_by_xpath('//a[@class="laypage_next"]').click()
    else:
        break

print("主播总数为：" + str(sum_DJ))
print("观众总人数为：" + str(sum_audience))
