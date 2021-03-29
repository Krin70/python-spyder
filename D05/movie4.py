import requests
from fake_useragent import UserAgent
from random import randint
from time import sleep
import re


def get_html(url):
    headers = {
        "User-Agent": UserAgent().random
    }
    sleep(randint(3, 5))
    response = requests.get(url, headers=headers)

    response.encoding = "utf-8"
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    all_url = set(re.findall(r'<a href="(/films/\d+)"', html))
    return ['https://maoyan.com{}'.format(url) for url in all_url]


def parse_info(html):
    name = re.findall(r'<h1 class="name">(.+)</h1>', html)
    types = '/'.join(re.findall(r'target="_blank"> (.+) </a>', html))
    try:
        actors = set(re.findall(r'li class="celebrity actor.+>\s+<a.+>\s+<img.+>\s+<.+>\s+<div.+>\s+<a.+>\s+(.+)\s+</a>\s+<br.+>\s+', html))
    except Exception as e:
        print(e)
        actors = ''
    return {
        "name": name,
        "types": types,
        "actors": actors
    }




def format_actors(actors_a):
    actors_set = set()
    for a in actors_a:
        actors_set.add(a.text.strip())
    return actors_set


def main():
    index_url = "https://maoyan.com/films?showType=2"
    html = get_html(index_url)
    movie_urls = parse_index(html)
    print(movie_urls)
    for url in movie_urls:
        movie_html = get_html(url)
        movie = parse_info(movie_html)
        print(movie)


if __name__ == '__main__':
    main()
