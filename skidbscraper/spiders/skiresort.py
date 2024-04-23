import scrapy

# The scraper for the list of all ski resorts in Europe
class SkiresortSpider(scrapy.Spider):
    name = "skiresort"
    allowed_domains = ["skiresort.info"]

    start_urls = [
        "https://www.skiresort.info/ski-resorts/europe/",
    ]

    def parse(self, response):
        next_page = response.css("#pagebrowser li:nth-of-type(8) a::attr(href)").get()
        yield {
                "resort_link": response.css("div.resort-list-item-img-wrap > a::attr(href)").getall()
            }

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)