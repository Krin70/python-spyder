from urllib.parse import urlencode
from urllib.request import Request, urlopen
from fake_useragent import UserAgent
from urllib.request import HTTPCookieProcessor,build_opener


login_url = "https://www.zhihu.com/signin?next=%2Fpeople%2Fedit"
headers = {
    "User-Agent": UserAgent().chrome,
}
form_data = {
    "user": "",
    "password": ""
}
f_data = urlencode(form_data).encode()
request = Request(login_url, headers=headers, data=form_data)


# response = urlopen(request)  错误的
handler = HTTPCookieProcessor()
openr = build_opener(handler)
response = openr.open(request)

# print(response.read().decode())

info_url = "https://www.zhihu.com/people/edit"
request = Request(info_url, headers=headers)
response = openr.open(request)
print(response.read().decode())
