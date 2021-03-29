import requests
from fake_useragent import UserAgent
from lxml import etree
from random import randint
from time import sleep
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        "User-Agent": UserAgent().random
    }
    sleep(randint(3, 10))
    response = requests.get(url, headers=headers)

    response.encoding = "utf-8"
    if response.status_code == 200:
        return response.text
    else:
        return None


def parse_index(html):
    soup = BeautifulSoup(html, "lxml")
    all_a = soup.select(".channel-detail.movie-item-title > a")
    all_url = []
    for a in all_a:
        all_url.append("https://maoyan.com" + a.attrs['href'])
    # e = etree.HTML(html)
    # all_url = e.xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
    # return ['https://maoyan.com{}'.format(url) for url in all_url]
    return all_url


def parse_info(html):
    soup = BeautifulSoup(html, 'lxml')
    name = soup.select(".name")[0].text
    types = soup.select("div[class='movie-hover-title']")[1].text
    actors = soup.select("div[class=movie-hover-title]")[2].text

    # e = etree.HTML(html)
    # name = e.xpath('//h3[@class="name"]/text()')
    # types = e.xpath('//li[@class="ellipsis"][1]/text()')
    # actors = e.xpath('//li[@class="celebrity.actor"]/div[@class="info"]/a/text()')
    # actors = format_actors(actors)
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
