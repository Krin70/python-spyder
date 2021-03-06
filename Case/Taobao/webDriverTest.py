import time
from random import random

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options, executable_path='D:/anaconda3/Scripts/chromedriver')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
driver.get('http://exercise.kingname.info')

#
# # 手动登录
# def login(extension_path, tmp_path):
#     chrome_options = webdriver.ChromeOptions()
#     # 设置好应用扩展
#     chrome_options.add_extension(extension_path)
#
#     # 添加下载路径
#     prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': tmp_path,
#              "profile.default_content_setting_values.automatic_downloads": 1}  # 允许多个文件下载
#     chrome_options.add_experimental_option('prefs', prefs)
#
#     # 修改windows.navigator.webdriver，防机器人识别机制，selenium自动登陆判别机制
#     chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
#
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     #     drive = webdriver.Chrome(chrome_options=chrome_options)
#     drive = webdriver.Chrome(options=chrome_options)
#     url = 'https://sycm.taobao.com/portal/home.htm'
#     drive.implicitly_wait(10)
#     drive.get(url)
#     input("请手动登录，成功后输入【1】：")
#     # 叉掉页面无关元素后再输入1继续执行
#     drive.maximize_window()  # 窗口最大化
#     tm = random.uniform(1, 2)
#     time.sleep(tm)
#     return drive
#
#
# login('D:/anaconda3/Scripts/chromedriver.exe', '.')
