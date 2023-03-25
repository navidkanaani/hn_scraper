import scrapy
from pathlib import Path

class HackerNewsIndexSpider(scrapy.Spider):
    name = "hacker_news_index"
    start_urls = [
        "https://news.ycombinator.com/"
    ]

    def parse(self, response):
        main_table = response.xpath("//table")
        news_titles = main_table.xpath("//tr[@class='athing']")
        news_list = []
        for news in news_titles:
            news_info = {
                "id": news.css("tr[class='athing']::attr(id)").get(),
                "title": news.css("span a::text").get(),
                "source_url": news.css("span a::attr(href)").get(),
                "website_address": news.css("span[class='sitestr']::text").get(),
            }
            news_list.append(news_info)

        news_subtext_list = []    
        news_subtexts = main_table.xpath("//td/span[@class='subline']")
        for subtext in news_subtexts:
            news_subtext_info = {
                "id": subtext.css("span[class='score']::attr(id)").get().split("_")[1],
                "score": subtext.css("span[class='score]::text").get(),
                "comment_count": subtext.css("span a::text").re(r"^\d*")[-1],
                "news_url": "item?id=".join(id)
            }
        page = response.url.split("/")[-2]
        with open(f"../../data/{page}.html", "w") as f:
            f.write(main_table)
            self.log(f"{f} is saved!!!")