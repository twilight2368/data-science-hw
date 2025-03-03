# Week 3 - Bài tập crawl dữ liệu và scraping dữ liệu với thư viện Scrapy

- Website trong ví dụ: [https://books.toscrape.com/index.html](https://books.toscrape.com/index.html)

## Hướng dẫn cài đặt

### Tạo môi trường cho với `pip`

- Yêu cầu: Python 3.x.x, pip
- Chạy command line sau:

```bash
python -m venv .venv
```

- Sau khi tạo virtual environment, cần kích hoạt (activate) nó để sử dụng.

```command
.venv\Scripts\activate.bat
```

hoặc

```bash
source .venv/Scripts/activate
```

### Cài đặt Scrapy

- Nên tham khảo [Scrapy documents](https://docs.scrapy.org/en/latest/)

```bash
pip install Scrapy
```

### Init project

- Tạo thư mục `src`

```bash
cd src
scrapy startproject spiderman
```

- Cấu trúc project

```
spiderman/
    scrapy.cfg            # deploy configuration file

    spiderman/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```

## Tạo Spider

- Tạo file với tên `quotes_v2.py` trong thư mục `spiderman\spiderman` của project

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_v2"
    allowed_domains = ["quotes.toscrape.com"]  # Restrict to this domain
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        # Extract quote details
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        # Follow pagination (next page)
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            # Simplified URL handling
            yield response.follow(next_page, callback=self.parse)
```

## Chạy chương trình

### Option 1: Với command line

```bash
cd src/spiderman
```

```bash
scrapy list # List all the spiders
```

```bash
scrapy crawl (name-spider) -o output.json
scrapy crawl (name-spider) -o output.csv
```

### Option 2: Với chương trình python

- Tạo file với tên `run_spider.py` trong thư mục `src` của project

```python
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

```

- Chạy câu lệnh

```bash
python run_spider.py
```
