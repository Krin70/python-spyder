from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent
import ssl

context = ssl._create_unverified_context()

url = "https://8owe.com/index.php/action/login?_=50fd655b442d9b46c2a917e540041503"
form_data = {
    "name": "sword_mas_ter@163.com",
    "password": "qwer1234."
}
headers = {
    "User-Agent": UserAgent().chrome
}
f_data = urlencode(form_data)
request = Request(url, headers=headers, data=f_data.encode())
response = urlopen(request, context=context)
print(response.read().decode())
