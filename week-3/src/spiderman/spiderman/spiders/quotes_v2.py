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
