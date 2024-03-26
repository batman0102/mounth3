import asyncio
import httpx
from parsel import Selector
from pprint import pprint

class AnimeSpiritCrawler:
    MAIN_URL = "https://animespirit.tv/page/"
    BASE_URL = "https://animespirit.tv/"

    async def get_page(self, url, client: httpx.AsyncClient):
        response = await client.get(url)
        return response.text

    def get_anime_links(self, html):
        selector = Selector(html)
        anime_links = selector.css("div.custom-poster a::attr(href)").getall()
        anime_links = [f"{AnimeSpiritCrawler.BASE_URL}{link}" for link in anime_links]
        return anime_links[:3]

    async def get_anime_data(self):
        async with httpx.AsyncClient() as client:
            tasks = [asyncio.create_task(self.get_page(f"{AnimeSpiritCrawler.MAIN_URL}{i}/", client)) for i in range(2, 12)]
            results = await asyncio.gather(*tasks)

            all_anime_links = []
            for res in results:
                anime_links = self.get_anime_links(res)
                all_anime_links.extend(anime_links)
            return all_anime_links

if __name__ == "__main__":
    crawler = AnimeSpiritCrawler()
    pprint(asyncio.run(crawler.get_anime_data()))



