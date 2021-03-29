from urllib.request import Request, urlopen
from urllib.parse import urlencode
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        "User-Agent": UserAgent().chrome
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    # print(response.read().decode())
    return response.read()


def save_html(filename, html_byte):
    with open(filename, "wb") as f:
        f.write((html_byte))


def main():
    content = input("请输入要下载的内容: ")
    num = input("请输入要下载多少页: ")
    base_url = "https://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(num)):
        args = {
            "pn": pn * 50,
            "kw": content
        }
        args = urlencode(args)
        # print(args)
        # print(base_url.format(args))
        html_byte = get_html(base_url.format(args))
        filename = "page" + str(pn + 1) + ".html"
        print("downloading " + filename)
        save_html(filename, html_byte)


if __name__ == '__main__':
    main()
