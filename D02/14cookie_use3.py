from urllib.parse import urlencode
from urllib.request import Request, build_opener, HTTPCookieProcessor
from fake_useragent import UserAgent
from http.cookiejar import MozillaCookieJar

# 登录

url = ""


# 保存
def get_cookie():
    login_url = ""
    headers = {
        "User-Agent": UserAgent().chrome
    }
    form_data = {
        "user": "",
        "password": ""
    }
    f_data = urlencode(form_data).encode()
    request = Request(login_url, headers=headers,data=f_data)
    cookie_jar = MozillaCookieJar()
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    cookie_jar.save("cookie.txt", ignore_expires=True, ignore_discard=True)


def use_cookie():
    info_url = ""
    headers = {
        "User-Agent": UserAgent().chrome
    }
    request = Request(info_url, headers=headers)
    cookie_jar = MozillaCookieJar()
    cookie_jar.load("cookie.txt",ignore_expires=True,ignore_discard=True)
    handler = HTTPCookieProcessor(cookie_jar)
    opener = build_opener(handler)
    response = opener.open(request)
    print(response.read().decode())

# 获取cookie从文件中

# 访问页面
if __name__ == '__main__':
    get_cookie()
    use_cookie()
