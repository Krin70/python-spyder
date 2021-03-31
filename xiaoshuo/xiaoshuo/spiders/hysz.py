import scrapy


class HyszSpider(scrapy.Spider):
    name = 'hysz'
    allowed_domains = ['hongyeshuzhai.com']
    start_urls = ['https://www.hongyeshuzhai.com/shuzhai/64755/30324993.html']

    def parse(self, response):
        title = response.xpath("//h1/text()").extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()) \
            .replace('\r\n\r\n\xa0\xa0\xa0\xa0', '\n').replace('    ', '\n')

        yield {
            "title": title,
            "content": content
        }
        next_url = response.xpath('//div[@class="bottem2"]/a[4]/@href').extract_first()
        # base_url = 'https://www.hongyeshuzhai.com{}'.format(next_url)
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
