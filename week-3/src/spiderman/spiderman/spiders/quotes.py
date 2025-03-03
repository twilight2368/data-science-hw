from pathlib import Path

import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        self.log("Parse method is running...")  # Debug message
        quotes = []
        for quote in response.css("div.quote"):
            quote_data = {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
            quotes.append(quote_data)

        # Save data to a JSON file
        with open("quotes.json", "w", encoding="utf-8") as f:
            json.dump(quotes, f, ensure_ascii=False, indent=4)

        # * Take full html page on response
        # self.log("Saved file: quotes.json")  # Confirm file creation
        # page = response.url.split("/")[-2]
        # filename = f"quotes-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
