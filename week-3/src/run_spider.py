from scrapy.crawler import CrawlerProcess
from spiderman.spiderman.spiders.quotes import QuotesSpider

process = CrawlerProcess()
process.crawl(QuotesSpider)
process.start()
