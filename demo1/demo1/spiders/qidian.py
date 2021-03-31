import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    # start_urls = ['https://www.qidian.com/rank/yuepiao?chn=21/']

    def start_requests(self):
        yield scrapy.Request('https://www.qidian.com/rank/yuepiao?chn=21/')

    def parse(self, response):
        names = response.xpath('//h4/a/text()').extract()
        authors = response.xpath('//p[@class="author"]/a[1]/text()').extract()
        print(names)
        print(authors)
        book = []
        for name, author in zip(names, authors):
            book.append({'name': name, 'author': author})
        return book
