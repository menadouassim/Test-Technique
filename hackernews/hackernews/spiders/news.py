import scrapy


class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = [f"https://news.ycombinator.com/?p={page_num}"for page_num in range(1,6)]
    #start_urls = ["https://news.ycombinator.com"]
    def parse(self, response):
        for news_link in response.css("tr.athing"):
            score_tab=news_link.xpath("following-sibling::tr[1]")
            yield{
                "Titre_de_l’article":news_link.css("span.titleline a::text").get(),
                "source":news_link.css("span.titleline a::attr(href)").get(),
                "Nbr_up_votes":score_tab.css("span.score::text").get()
            }
