import httpx
from parsel import Selector
from pprint import pprint

class AnimeSpiritCrawler:
    MAIN_URL = "https://animespirit.tv/"

    def get_anime_links(self):
        self.response = httpx.get(AnimeSpiritCrawler.MAIN_URL)
        selector = Selector(self.response.text)
        anime_links = selector.css("div.custom-poster a::attr(href)").getall()
        anime_links = [self.MAIN_URL + link for link in anime_links]
        return anime_links[:3]

if __name__ == "__main__":
    crawler = AnimeSpiritCrawler()
    pprint(crawler.get_anime_links())


