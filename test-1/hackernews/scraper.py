from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from hackernews.spiders.news import NewsSpider

def setup_settings():
    settings = get_project_settings()

    settings.set("FEEDS", {
        "news-articles.csv": {
            "format": "csv",
            "overwrite": True,
            "encoding": "utf-8",
        }
    })

    return settings


def main():
    settings = setup_settings()

    print("Loaded ITEM_PIPELINES:", settings.get("ITEM_PIPELINES"))

    process = CrawlerProcess(settings)
    process.crawl(NewsSpider)
    process.start()


if __name__ == "__main__":
    main()
