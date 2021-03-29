import requests
from fake_useragent import UserAgent
from D04.yzm_util import get_code


def get_image():
    img_url = ''
    response = session.get(img_url, headers=headers)
    with open("yzm.jpg", "wb") as f:
        f.write(response.content)
    code = get_code("yzm.jpg")
    print(code)
    return code


def do_login(code):
    login_url = ""
    f_data = {
        "user": "",
        "password": "",
        "utype": "",
        "vcode": code
    }

    response = session.get(login_url, headers=headers, params=f_data)
    print(response.text)


if __name__ == '__main__':
    session = requests.session()
    index_url = ""
    headers = {
        "User-Agent": UserAgent().random
    }
    response = session.get(index_url, headers=headers)
    code = get_image()
    do_login(code)
