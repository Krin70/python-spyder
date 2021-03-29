from time import sleep

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome import options
from selenium.webdriver.support.ui import WebDriverWait


class TaoBao_infos:
    # 构造方法
    def __init__(self):
        url = 'https://www.taobao.com/'
        self.url = url
        # 此步骤很重要
        # chrome_options 初始化选项
        chrome_options = webdriver.ChromeOptions()

        # 设置浏览器初始 位置x,y & 宽高x,y
        chrome_options.add_argument(f'--window-position={217},{172}')
        chrome_options.add_argument(f'--window-size={1200},{1000}')
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        # 关闭自动测试状态显示 // 会导致浏览器报：请停用开发者模式
        # window.navigator.webdriver还是返回True,当返回undefined时应该才可行。
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])

        self.browser = webdriver.Chrome(options=chrome_options)
        # 通过浏览器的dev_tool在get页面钱将.webdriver属性改为"undefined"
        # 拦截webdriver检测代码
        self.wait = WebDriverWait(self.browser, 10)

    def login_infos(self):
        # 控制浏览器打开网页
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]').click()
        sleep(5)
        if self.browser.find_element_by_xpath('//*[@id="fm-login-id"]') and self.browser.find_element_by_xpath(
                '//*[@id="fm-login-password"]'):
            user = self.browser.find_element_by_xpath('//*[@id="fm-login-id"]')
            user.send_keys('韦麒权')
            sleep(1)

            password = self.browser.find_element_by_xpath('//*[@id="fm-login-password"]')
            password.send_keys('asdf1234.')
            sleep(1)

        submit = self.browser.find_element_by_xpath(
            '/html/body/div/div[2]/div[3]/div/div/div/div[2]/div/form/div[4]/button')
        submit.click()
        sleep(5)

        # TaoBao_index = self.browser.find_element_by_xpath('//*[@id="J_SiteNavHome"]/div/a')
        # TaoBao_index.click()
        # sleep(1)

        search_input = self.browser.find_element_by_xpath('//*[@id="q"]')
        shop_name = input('请输入你想要找搜索得商品名称')
        search_input.send_keys(shop_name)
        sleep(1)
        search_submit = self.browser.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button')
        search_submit.click()

        # 获取商品信息
        page = self.browser.page_source

        soup = BeautifulSoup(page, 'lxml')
        shop_data_list = soup.find('div', class_='grid g-clearfix').find_all_next('div', class_='items')

        # 商品详细信息
        shop_name_list = []
        shop_price_list = []
        shop_people_list = []
        shop_location_list = []

        for shop_data in shop_data_list:
            # 名称
            shop_image_data = shop_data.find_all('div', class_='pic')
            for shop_data_a in shop_image_data:
                shop_data_a = shop_data_a.find_all('a', class_='pic-link J_ClickStat J_ItemPicA')
                for shop_name in shop_data_a:
                    shop_name = shop_name.find_all('img')[0]['alt']
                    shop_name_list.append(shop_name)

            # 金额
            shop_price_data = shop_data.find_all('div', class_='price g_price g_price-highlight')
            for shop_price in shop_price_data:
                shop_price_list.append(shop_price.text.strip())

            # 购买人数
            shop_people_number_data = shop_data.find_all('div', class_='deal-cnt')
            for shop_people_number in shop_people_number_data:
                shop_people_list.append(shop_people_number.text.strip())

            # 店铺地区
            shop_location_data = shop_data.find_all('div', class_='location')
            for shop_location in shop_location_data:
                shop_location_list.append(shop_location.text.strip())

            # for data in shop_data:
            #     print(data)

        for name, price, people, url in zip(shop_name_list, shop_price_list, shop_people_list, shop_location_list):
            print(name+'|'+price+'|'+people+'|'+url)


TaoBao_infos().login_infos()
