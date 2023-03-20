import scrapy
from pathlib import Path

class HackerNewsIndexSpider(scrapy.Spider):
    name = "hacker_news_index"
    start_urls = [
        "https://news.ycombinator.com/"
    ]

    def parse(self, response):
        main_table = response.xpath("//table").get()
        page = response.url.split("/")[-2]
        with open(f"../../data/{page}.html", "w") as f:
            f.write(main_table)
            self.log(f"{f} is saved!!!")