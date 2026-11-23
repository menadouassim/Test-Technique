
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from hackernews.hackernews.spiders.news import NewsSpider



def Setup_Settings():
    Settings = get_project_settings()

    Settings.set("FEEDS", {
        "news-articles.csv": {
            "format": "csv",
            "overwrite": True,
            "encoding": "utf-8",
        }
    })

    return Settings

def main():

    Settings = Setup_Settings()
    process = CrawlerProcess(Settings)
    process.crawl(NewsSpider)
    process.start()

if __name__ == "__main__":
    main()