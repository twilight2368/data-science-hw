from scrapy.crawler import CrawlerProcess
from spiderman.spiderman.spiders.quotes_v2 import QuotesSpider

process = CrawlerProcess(settings={
    "FEED_EXPORT_ENCODING":  "utf-8",
    "FEEDS": {
        "output.json": {"format": "json"},
        "output.csv": {"format": "csv"},
    },
})
process.crawl(QuotesSpider)
process.start()
