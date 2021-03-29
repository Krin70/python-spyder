from urllib.request import Request, urlopen
from fake_useragent import UserAgent

base_url = "https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start={}&limit=1"
i = 0
while True:
    headers = {
        "User-Agent": UserAgent().chrome
    }
    url = base_url.format(i * 20)
    request = Request(url, headers=headers)
    reponse = urlopen(request)
    info = reponse.read().decode()
    i+=1
    if info == '[]' or info is None:
        break
    print(info)
