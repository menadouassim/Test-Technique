import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com"]

    def parse(self, response):
        pass
