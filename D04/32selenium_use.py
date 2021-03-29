from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get("http://www.hao123.com")
chrome.save_screenshot('hao123.png')
html = chrome.page_source
print(html)
chrome.quit()

