from scrapy.cmdline import execute


execute("scrapy crawl maoyan".split())
# execute("scrapy crawl qidian -o books.json".split())
# execute(["scrapy", "crawl", "baidu"])#或者这种写法
